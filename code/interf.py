import tkinter as tk
from LoginPage import LoginPage

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# 只需要改这里的数据，完成PostgreSQL数据库连接
user = "postgres"
pwd = "huangjiahao"
port = 5432
host = "127.0.0.1"
db_name = "fcgp"

# 先用postgres（管理员）身份打开数据库
conn = psycopg2.connect(database="postgres", port=port, host=host, user=user, password=pwd)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

DATABASE_NAME = 'fcgp'

DB_NAME_EXIST = """
select * from pg_database where datname='{}';
""".format(DATABASE_NAME)

DB_NAME = """
CREATE DATABASE {};
""".format(DATABASE_NAME)

cur = conn.cursor()

cur.execute(DB_NAME_EXIST)

conn.commit()
result = cur.fetchall()
if not result:
    conn.autocommit = True
    cur.execute(DB_NAME)
    conn.autocommit = False
    conn1 = psycopg2.connect(database="fcgp", port=port, host=host, user=user, password=pwd)
    curs = conn1.cursor()
    curs.execute('''create TABLE USEER(
                      U_id varchar NOT NULL,
                      U_password varchar NOT NULL,
                      U_name varchar,
                      U_question1 varchar,
                      U_answer1 varchar,
                      U_question2 varchar,
                      U_answer2 varchar,
                      U_question3 varchar,
                      U_answer3 varchar,
                      U_score int,
                      U_prop1 int,
                      U_prop2 int,
                      U_time int,
                      primary key(U_id))
             ''')

    print("Table created successfully")  # 测试用，可删除
    conn1.commit()
    conn1.close()
else:
    print('{} already exists'.format(DATABASE_NAME))
    cur.close()
    conn.close()

# 正式连接fcgp数据
conn = psycopg2.connect(database="fcgp", user=user,
                        password=pwd, host=host, port=port)
# 生成界面
root = tk.Tk()
root.title('FC Game Platform')
LoginPage(root, conn)
root.mainloop()
