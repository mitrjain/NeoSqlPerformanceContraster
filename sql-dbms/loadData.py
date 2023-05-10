import mysql.connector
from dotenv import load_dotenv
import os
import csv

load_dotenv()

dbUser = os.environ.get("DB_USER")
dbPwd = os.environ.get("DB_PWD")

mydb = mysql.connector.connect(
  host="localhost",
  user=dbUser,
  password=dbPwd,
  database="MAC"
)

mycursor = mydb.cursor()

print("Loading professionals.csv")
#professionals
insertQ = "INSERT INTO professionals (professionals_id, professionals_location, professionals_industry, professionals_headline, professionals_date_joined) VALUES "
numQueries = 0

with open('professionals.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue
        insert = ''+insertQ
        # print(row[4])
        datetimeVals = row[4].split(' ')
        datetime = datetimeVals[0]+' '+datetimeVals[1]
        for i in range(1,len(row)-1):
            # row[i]=row[i].replace('"','\\"')
            row[i]=row[i].replace("'","\\'")
        
        # print(datetime)
        insert += """('{}','{}','{}','{}','{}');""".format(row[0],row[1],row[2],row[3],datetime)
        # print("Executing Query: ",insert)
        mycursor.execute(insert)
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)

print("Loading students.csv")
#students
insertQ = "INSERT INTO students (students_id,students_location,students_date_joined) VALUES "
numQueries = 0

with open('students.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue

        insert = ''+insertQ
        datetimeVals = row[2].split(' ')
        datetime = datetimeVals[0]+' '+datetimeVals[1]
        for i in range(1,len(row)-1):
            # row[i]=row[i].replace('"','\\"')
            row[i]=row[i].replace("'","\\'")
        
        # print(datetime)
        insert += """('{}','{}','{}');""".format(row[0],row[1],datetime)
        # print("Executing Query: ",insert)
        mycursor.execute(insert)
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)

print("Loading tags.csv")
#tags
insertQ = "INSERT INTO tags (tags_tag_id,tags_tag_name) VALUES "
numQueries = 0

with open('tags.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue
        insert = ''+insertQ
        for i in range(1,len(row)):
            # row[i]=row[i].replace('"','\\"')
            row[i]=row[i].replace("'","\\'")
        
        # print(datetime)
        insert += """({},'{}');""".format(row[0],row[1])
        # print("Executing Query: ",insert)
        mycursor.execute(insert)
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)

print("Loading groups.csv")
# groups_
insertQ = "INSERT INTO groups_ (groups_id,groups_group_type) VALUES "
numQueries = 0

with open('groups.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue

        insert = ''+insertQ
        for i in range(1,len(row)):
            # row[i]=row[i].replace('"','\\"')
            row[i]=row[i].replace("'","\\'")
        
        # print(datetime)
        insert += """('{}','{}');""".format(row[0],row[1])
        # print("Executing Query: ",insert)
        mycursor.execute(insert)
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)

print("Loading questions.csv")
# questions
insertQ = "INSERT INTO questions (questions_id,questions_author_id,questions_date_added,questions_title,questions_body) VALUES "
numQueries = 0

with open('questions.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue
        insert = ''+insertQ
        # print(row[4])
        datetimeVals = row[2].split(' ')
        datetime = datetimeVals[0]+' '+datetimeVals[1]
        for i in range(1,len(row)):
            # row[i]=row[i].replace('"','\\"')
            row[i]=row[i].replace("\\","\\\\'")
            row[i]=row[i].replace("'","\\'")
            
        
        # print(datetime)
        insert += """('{}','{}','{}','{}','{}');""".format(row[0],row[1],datetime,row[3],row[4])
        # print("Executing Query: ",insert)
        mycursor.execute(insert)
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)

print("Loading tag_questions.csv")
# # tag_questions
insertQ = "INSERT INTO tag_questions (tag_questions_tag_id,tag_questions_question_id) VALUES "
numQueries = 0

with open('tag_questions.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue
        insert = ''+insertQ
        for i in range(1,len(row)-1):
            # row[i]=row[i].replace('"','\\"')
            row[i]=row[i].replace("'","\\'")
        
        # print(datetime)
        insert += """({},'{}');""".format(row[0],row[1])
        # print("Executing Query: ",insert)
        mycursor.execute(insert)
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)

print("Loading tag_users.csv")
# # tag_users
insertQ = "INSERT INTO tag_users (tag_users_tag_id,tag_users_user_id) VALUES "
numQueries = 0

with open('tag_users.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue
        insert = ''+insertQ
        for i in range(1,len(row)-1):
            # row[i]=row[i].replace('"','\\"')
            row[i]=row[i].replace("'","\\'")
        
        # print(datetime)
        insert += """({},'{}');""".format(row[0],row[1])
        # print("Executing Query: ",insert)
        mycursor.execute(insert)
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)

print("Loading group_memberships.csv")
# group_memberships
insertQ = "INSERT INTO group_memberships (group_memberships_group_id,group_memberships_user_id) VALUES "
numQueries = 0

with open('group_memberships.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue
        insert = ''+insertQ
        for i in range(1,len(row)-1):
            # row[i]=row[i].replace('"','\\"')
            row[i]=row[i].replace("'","\\'")
        
        # print(datetime)
        insert += """('{}','{}');""".format(row[0],row[1])
        # print("Executing Query: ",insert)
        mycursor.execute(insert)
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)

print("Loading school_memberships.csv")
# school_memberships
insertQ = "INSERT INTO school_memberships (school_memberships_school_id,school_memberships_user_id) VALUES "
numQueries = 0

with open('school_memberships.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue
        insert = ''+insertQ
        for i in range(1,len(row)-1):
            # row[i]=row[i].replace('"','\\"')
            row[i]=row[i].replace("'","\\'")
        
        # print(datetime)
        insert += """({},'{}');""".format(row[0],row[1])
        # print("Executing Query: ",insert)
        mycursor.execute(insert)
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)

print("Loading answers.csv")
# answers
insertQ = "INSERT INTO answers (answers_id,answers_author_id,answers_question_id,answers_date_added,answers_body) VALUES "
numQueries = 0

with open('answers.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue
        insert = ''+insertQ
        # print(row[4])
        datetimeVals = row[3].split(' ')
        datetime = datetimeVals[0]+' '+datetimeVals[1]
        for i in range(1,len(row)):
            # row[i]=row[i].replace('"','\\"')
            row[i]=row[i].replace("\\","\\\\'")            
            row[i]=row[i].replace("'","\\'")
        
        # print(datetime)
        insert += """('{}','{}','{}','{}','{}');""".format(row[0],row[1],row[2],datetime,row[4])
        # print("Executing Query: ",insert)
        mycursor.execute(insert)
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)


print("Loading comments.csv")
# comments
insertQ = "INSERT INTO comments (comments_id,comments_author_id,comments_parent_content_id,comments_date_added,comments_body) VALUES "
numQueries = 0

with open('comments.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue
        insert = ''+insertQ
        # print(row[4])
        datetimeVals = row[3].split(' ')
        datetime = datetimeVals[0]+' '+datetimeVals[1]
        for i in range(1,len(row)):
            # row[i]=row[i].replace('"','\\"')
            row[i]=row[i].replace("\\","\\\\'")            
            row[i]=row[i].replace("'","\\'")
        
        # print(datetime)
        insert += """('{}','{}','{}','{}','{}');""".format(row[0],row[1],row[2],datetime,row[4])
        # print("Executing Query: ",insert)
        mycursor.execute(insert)
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)


print("Loading emails.csv")
# emails
insertQ = "INSERT INTO emails (emails_id,emails_recipient_id,emails_date_sent,emails_frequency_level) VALUES "
numQueries = 0

with open('emails.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue
        insert = ''+insertQ
        # print(row[4])
        datetimeVals = row[2].split(' ')
        datetime = datetimeVals[0]+' '+datetimeVals[1]
        for i in range(1,len(row)):
            # row[i]=row[i].replace('"','\\"')
            row[i]=row[i].replace("'","\\'")
        
        # print(datetime)
        insert += """({},'{}','{}','{}');""".format(row[0],row[1],datetime,row[3])
        # print("Executing Query: ",insert)
        mycursor.execute(insert)
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)

print("Loading matches.csv")
# matches
insertQ = "INSERT INTO matches (matches_email_id,matches_question_id) VALUES "
numQueries = 0

with open('matches.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue        
        insert = ''+insertQ
        for i in range(1,len(row)-1):
            # row[i]=row[i].replace('"','\\"')
            row[i]=row[i].replace("'","\\'")
        
        # print(datetime)
        insert += """({},'{}');""".format(row[0],row[1])
        # print("Executing Query: ",insert)
        mycursor.execute(insert)
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)


print("Loading question_scores.csv")
#question_scores
insertQ = "INSERT INTO question_scores (id, score) VALUES "
numQueries = 0
ignored=0
import csv
with open('question_scores.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue
        insert = ''+insertQ
        insert += """('{}',{});""".format(row[0],row[1])
        try:
            mycursor.execute(insert)
        except:
            ignored+=1
            continue
        numQueries +=1
mydb.commit()
print("No. of rows inserted = ",numQueries)


print("Loading answer_scores.csv")
# answer_scores
insertQ = "INSERT INTO answer_scores (id, score) VALUES "
numQueries = 0
ignored=0

with open('answer_scores.csv', newline='') as csvfile:
    readerObj = csv.reader(csvfile, delimiter=',')
    # print("Building insert query")
    for row in readerObj:
        if numQueries==0:
            numQueries +=1
            continue
        insert = ''+insertQ
        insert += """('{}',{});""".format(row[0],row[1])
        try:
            mycursor.execute(insert)
        except:
            ignored+=1
            print("Row ignored: ",numQueries)
            continue
        numQueries +=1
        # print("Row inserted: ",numQueries)
mydb.commit()
print("No. of rows inserted = ",numQueries)
