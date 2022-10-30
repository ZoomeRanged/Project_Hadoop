import psycopg2
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine
data_property = pd.read_csv('D:/Project_Hadoop/dataset/dataset/TR_PropertyInfo.csv')
data_user = pd.read_csv('D:/Project_Hadoop/dataset/dataset/TR_UserInfo.csv')

conn = psycopg2.connect(database="postgres",
                        user='postgres',
                        password='admin', 
                        host='127.0.0.1',
                        port='5432')

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE UserInfo(user_id int,\
user_sex varchar(20),\
user_device varchar(30))
;'''

sql = '''CREATE TABLE Property_Info(Prop_ID int,\
Property_City varchar(20),\
Property_State varchar(30))
;'''

#cursor.execute(sql)

sql2 = '''COPY UserInfo(user_id,user_sex,\
user_device)
FROM 'D:/Project_Hadoop/dataset/dataset/TR_UserInfo.csv'
DELIMITER ','
CSV HEADER;'''


cursor.execute(sql2)

sql3 = '''select * from UserInfo;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)

conn.commit()
conn.close()