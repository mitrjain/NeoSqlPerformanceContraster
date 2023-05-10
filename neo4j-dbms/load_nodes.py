import csv
from neo4j import GraphDatabase
import sys
from dotenv import load_dotenv

load_dotenv()

import os

uri = "bolt://localhost:7687"
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
try:
    driver = GraphDatabase.driver(uri, auth=(user, password))
    with driver.session() as session:
        session.close()
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

def create_emails_node(tx, rows):
    tx.run("""
    UNWIND $rows AS row
    CREATE (e:Emails {
        emails_id: row.emails_id,
        emails_recipient_id: row.emails_recipient_id,
        emails_date_sent: row.emails_date_sent,
        emails_frequency_level: row.emails_frequency_level
    })
    """, {"rows": rows})

def create_professionals_nodes(tx, rows):
    tx.run("""
    UNWIND $rows AS row
    CREATE (p:Professionals {
        professionals_id: row.professionals_id,
        professionals_location: row.professionals_location,
        professionals_industry: row.professionals_industry,
        professionals_headline: row.professionals_headline,
        professionals_date: row.professionals_date
    })
    """, {"rows": rows})

def create_school_memberships_nodes(tx, rows):
    tx.run("""
    UNWIND $rows AS row
    CREATE (sm:SchoolMemberships {
        school_memberships_school_id: row.school_memberships_school_id,
        school_memberships_user_id: row.school_memberships_user_id
    })
    """, {"rows": rows})

def create_comments_nodes(tx, rows):
    tx.run("""
    UNWIND $rows AS row
    CREATE (c:Comments {
        comments_id: row.comments_id,
        comments_author_id: row.comments_author_id,
        comments_parent_content_id: row.comments_parent_content_id,
        comments_date_added: row.comments_date_added,
        comments_body: row.comments_body
    })
    """, {"rows": rows})

def create_question_nodes(tx, rows):
        tx.run("""
    UNWIND $rows AS row
    CREATE (q:Questions {
        questions_id: row.questions_id,
        questions_author_id: row.questions_author_id,
        questions_date_added: row.questions_date_added,
        questions_title: row.questions_title,
        questions_body: row.questions_body
    })
    """, {"rows": rows})


def create_tags_nodes(tx, rows):
    tx.run("""
    UNWIND $rows AS row
    CREATE (t:Tags {
        tags_tag_id: row.tags_tag_id,
        tags_tag_name: row.tags_tag_name
    })
    """, {"rows": rows})

def create_answers_node(tx, rows):
    tx.run("""
    UNWIND $rows AS row
    CREATE (a:Answers {
        answers_id: row.answers_id,
        answers_author_id: row.answers_author_id,
        answers_question_id: row.answers_question_id,
        answers_date_added: row.answers_date_added,
        answers_body: row.answers_body
    })
    """, {"rows": rows})

def create_students_node(tx, rows):
    tx.run("""
    UNWIND $rows AS row
    CREATE (s:Students {
        students_id: row.students_id,
        students_location: row.students_location,
        students_date_joined: row.students_date_joined
    })
    """, {"rows": rows})

def create_groups_node(tx, rows):
    tx.run("""
    UNWIND $rows AS row
    CREATE (g:Groups {
        groups_id: row.groups_id,
        groups_group_type: row.groups_group_type
    })
    """, {"rows": rows})

def create_group_memberships_node(tx, rows):
    tx.run("""
    UNWIND $rows AS row
    CREATE (g:GroupMemberships {
        group_memberships_group_id: row.group_memberships_group_id,
        group_memberships_user_id: row.group_memberships_user_id
    })
    """, {"rows": rows})

def create_tag_users_node(tx, rows):
    tx.run("""
    UNWIND $rows AS row
    CREATE (g:TagUsers {
        tag_users_tag_id: row.tag_users_tag_id,
        tag_users_user_id: row.tag_users_user_id
    })
    """, {"rows": rows})
def create_matches_node(tx, rows):
    tx.run("""
    UNWIND $rows AS row
    CREATE (g:Matches {
        matches_email_id: row.matches_email_id,
        matches_question_id: row.matches_question_id
    })
    """, {"rows": rows})
def create_tag_questions_node(tx, rows):
    tx.run("""
    UNWIND $rows AS row
    CREATE (g:TagQuestions {
        tag_questions_tag_id: row.tag_questions_tag_id,
        tag_questions_question_id: row.tag_questions_question_id
    })
    """, {"rows": rows})

def execute_transaction(session,batch,file_name):
    try:
        if file_name == 'emails':
            session.execute_write(create_emails_node, batch)
        elif file_name == 'professionals':
            session.execute_write(create_professionals_nodes, batch)
        elif file_name == 'school_memberships':
            session.execute_write(create_school_memberships_nodes, batch)
        elif file_name == 'comments':
            session.execute_write(create_comments_nodes, batch)
        elif file_name == 'questions':
            session.execute_write(create_question_nodes, batch)
        elif file_name == 'tags':
            session.execute_write(create_tags_nodes, batch)
        elif file_name == 'answers':
            session.execute_write(create_answers_node, batch)
        elif file_name == 'students':
            session.execute_write(create_students_node, batch)
        elif file_name == 'groups':
            session.execute_write(create_groups_node, batch)
        elif file_name == 'group_memberships':
            session.execute_write(create_group_memberships_node, batch)
        elif file_name == 'matches':
            session.execute_write(create_matches_node, batch)
        elif file_name == 'tag_questions':
            session.execute_write(create_tag_questions_node, batch)
        elif file_name == 'tag_users':
            session.execute_write(create_tag_users_node, batch)
    except Exception as e:
        print(f"Error while executing transaction for {file_name}: {e}")
        sys.exit(1)

def process_csv(file_path,file_name, batch_size=1000):
    print('|------------------------------------------------------------|')
    print(f'Now creating nodes for the {file_name}.csv file')
    print('|------------------------------------------------------------|')
    
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        batch = []
        for row in reader:
            batch.append(row)
            if len(batch) >= batch_size:
                with driver.session(database="sample2") as session:
                    execute_transaction(session,batch,file_name)
                    session.close()
                batch = []

        # Create any remaining nodes from the last batch
        if batch:
            with driver.session(database="sample2") as session:
                execute_transaction(session,batch,file_name)
                session.close()
    print('|------------------------------------------------------------|')
    print(f'Woohoo! Finished creating nodes for the {file_name}.csv file')
    print('|------------------------------------------------------------|')

driver.close()

csv_file_paths = [
    "/Users/cajeeeeeeee/Workspace/CS-257/DBSPProject/dataset/emails.csv",
    "/Users/cajeeeeeeee/Workspace/CS-257/DBSPProject/dataset/professionals.csv",
    "/Users/cajeeeeeeee/Workspace/CS-257/DBSPProject/dataset/school_memberships.csv",
    "/Users/cajeeeeeeee/Workspace/CS-257/DBSPProject/dataset/comments.csv",
    "/Users/cajeeeeeeee/Workspace/CS-257/DBSPProject/dataset/questions.csv",
    "/Users/cajeeeeeeee/Workspace/CS-257/DBSPProject/dataset/tags.csv",
    "/Users/cajeeeeeeee/Workspace/CS-257/DBSPProject/dataset/answers.csv",
    "/Users/cajeeeeeeee/Workspace/CS-257/DBSPProject/dataset/students.csv",
    "/Users/cajeeeeeeee/Workspace/CS-257/DBSPProject/dataset/groups.csv",
    "/Users/cajeeeeeeee/Workspace/CS-257/DBSPProject/dataset/group_memberships.csv",
    "/Users/cajeeeeeeee/Workspace/CS-257/DBSPProject/dataset/matches.csv",
    "/Users/cajeeeeeeee/Workspace/CS-257/DBSPProject/dataset/tag_questions.csv",
    "/Users/cajeeeeeeee/Workspace/CS-257/DBSPProject/dataset/tag_users.csv"
]
for csv_file_path in csv_file_paths:
    print(csv_file_path.split('/')[-1].split('.')[0])
    process_csv(csv_file_path,csv_file_path.split('/')[-1].split('.')[0])