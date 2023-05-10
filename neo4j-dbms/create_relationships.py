from neo4j import GraphDatabase
from dotenv import load_dotenv
load_dotenv()

import os

uri = "bolt://localhost:7687"
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')

try:
    driver = GraphDatabase.driver(uri, auth=(user, password))
    driver.verify_connectivity()
    print('|------------------------------------------------------------|')
    print(" Connection successful!")
except Exception as e:
    print(f"Error: {e}")

def create_professionals_emails(tx):
    tx.run("""
    MATCH
    (a:Professionals),(b:Emails)
    WITH a, b
    WHERE a.professionals_id = b.emails_recipient_id
    CREATE (a)-[r:GOT_EMAIL]->(b)
    """)

def create_professionals_schools(tx):
    tx.run("""
    MATCH
    (a:Professionals),
    (b:SchoolMemberships)
    WHERE a.professionals_id = b.school_memberships_user_id
    CREATE (a)-[r:MEMBER_IN]->(b)
    """)
def create_professionals_comments(tx):
    tx.run("""
    MATCH
    (a:Professionals),
    (b:Comments)
    WITH a, b
    WHERE a.professionals_id = b.comments_author_id
    CREATE (a)-[r:AUTHOR_OF]->(b)
    """)

def create_professionals_answers(tx):
    tx.run("""
    MATCH
    (a:Professionals),
    (b:Answers)
    WITH a, b
    WHERE a.professionals_id = b.answers_author_id
    CREATE (a)-[r:AUTHOR_OF]->(b)
    """)

def create_professionals_questions(tx):
    tx.run("""
    MATCH
    (a:Professionals),
    (b:Questions)
    WITH a, b
    WHERE a.professionals_id = b.questions_author_id
    CREATE (a)-[r:AUTHOR_OF]->(b)
    """)

def create_professionals_tags(tx):
    tx.run("""
    MATCH
    (a:Professionals),
    (b:TagUsers),
    (c:Tags)
    WITH a, b, c
    WHERE a.professionals_id = b.tag_users_user_id
    AND b.tag_users_tag_id = c.tags_tag_id
    CREATE (a)-[r:HAS_TAG]->(c)
    """)

def create_professionals_groups(tx):
    tx.run("""
    MATCH
    (a:Professionals),
    (b:GroupMemberships),
    (c:Groups)
    WITH a, b, c
    WHERE a.professionals_id = b.group_memberships_user_id
    AND b.group_memberships_group_id = c.groups_id
    CREATE (a)-[r:MEMBER_IN]->(c)
    """)

def create_comments_questions(tx):
    tx.run("""
    MATCH
    (a:Comments),
    (b:Questions)
    WITH a, b
    WHERE a.comments_parent_content_id = b.questions_id
    CREATE (a)-[r:IS_REPLY_TO]->(b)
    """)

def create_comments_answers(tx):
    tx.run("""
    MATCH
    (a:Comments),
    (b:Answers)
    WITH a, b
    WHERE a.comments_parent_content_id = b.answers_id
    CREATE (a)-[r:IS_REPLY_TO]->(b)
    """)

def create_questions_emails(tx):
    tx.run("""
    MATCH
    (a:Questions),
    (b:Matches),
    (c:Emails)
    WITH a, b, c
    WHERE a.questions_id = b.matches_questions_id
    AND b.matches_email_id = c.emails_id
    CREATE (a)-[r:IS_IN]->(c)
    """)

def create_questions_tags(tx):
    tx.run("""
    MATCH
    (a:Questions),
    (b:TagQuestions),
    (c:Tags) 
    WITH a, b, c
    WHERE a.questions_id = b.tag_questions_question_id
    AND b.tag_questions_tag_id = c.tags_tag_id
    CREATE (a)-[r:HAS_TAG]->(c)
    """)

def create_answers_questions(tx):
    tx.run("""
    MATCH
    (a:Answers),
    (b:Questions)
    WITH a, b
    WHERE a.answers_question_id = b.questions_id
    CREATE (a)-[r:IS_REPLY_TO]->(b)
    """)

def create_students_answers(tx):
    tx.run("""
    MATCH
    (a:Students),
    (b:Answers) 
    WITH a, b
    WHERE a.students_id = b.answers_author_id
    CREATE (a)-[r:AUTHOR_OF]->(b)
    """)

def create_students_comments(tx):
    tx.run("""
    MATCH
    (a:Students),
    (b:Comments) 
    WITH a, b
    WHERE a.students_id = b.comments_author_id
    CREATE (a)-[r:AUTHOR_OF]->(b)
    """)

def create_students_questions(tx):
    tx.run("""
    MATCH
    (a:Students),
    (b:Comments) 
    WITH a, b
    WHERE a.students_id = b.questions_author_id
    CREATE (a)-[r:AUTHOR_OF]->(b)
    """)

def create_students_schools(tx):
    tx.run("""
    MATCH
    (a:Students),
    (b:SchoolMemberships)
    WITH a, b
    WHERE a.students_id = b.school_memberships_user_id 
    CREATE (a)-[r:MEMBER_IN]->(b)
    """)

def create_students_tags(tx):
    tx.run("""
    MATCH
    (a:Students),
    (b:TagUsers),
    (c:Tags) 
    WITH a, b, c
    WHERE a.students_id = b.tag_users_user_id
    AND b.tag_users_tag_id = c.tags_tag_id
    CREATE (a)-[r:HAS_TAG]->(c)
    """)

def create_students_groups(tx):
    tx.run("""
    MATCH
    (a:Students),
    (b:GroupMemberships),
    (c:Groups) 
    WITH a, b, c
    WHERE a.students_id = b.group_memberships_user_id
    AND b.group_memberships_group_id = c.groups_id
    CREATE (a)-[r:MEMBER_IN]->(c)
    """)
def main():

    relationship_functions = [
        create_professionals_emails,
        create_professionals_schools,
        create_professionals_comments,
        create_professionals_answers,
        create_professionals_questions,
        create_professionals_tags,
        create_professionals_groups,
        create_comments_questions,
        create_comments_answers,
        create_questions_emails,
        create_questions_tags,
        create_answers_questions,
        create_students_answers,
        create_students_comments,
        create_students_questions,
        create_students_schools,
        create_students_tags,
        create_students_groups
    ]

    for func in relationship_functions:
        with driver.session(database="sample2") as session:
            try:
                print('|------------------------------------------------------------|')
                session.execute_write(func)
                print(f' Successfully created {func.__name__} Relationship')
                print('|------------------------------------------------------------|')
                session.close()
            except Exception as e:
                print(f"Error: {e}")
    driver.close()

if __name__ == "__main__":
    main()
