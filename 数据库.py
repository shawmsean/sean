# -*- coding:utf-8 -*-
import sqlite3
conn = sqlite3.connect('test.db')

# 创建游标
cs = conn.cursor()

# # 创建表
# cs.execute('''CREATE TABLE person
#        (id varchar(20) PRIMARY KEY,
#         name varchar(20));''')

# # 提交当前事务
# conn.commit()



# cs.execute("INSERT INTO person (id, name) VALUES ('6', '张三')")
# cs.execute("INSERT INTO person (id, name) VALUES ('7', '李四')")
# cs.execute("INSERT INTO person (id, name) VALUES ('8', '王五')")
# cs.execute("INSERT INTO person (id, name) VALUES ('9', '赵六')")
# cs.execute("INSERT INTO person (id, name) VALUES ('10', '朱七')")

# conn.commit()



# 查询
# cs.execute("SELECT id, name FROM person")
# # 获取查询结果集中的下一行
# print(cs.fetchone())
# # 获取查询结果集中的下几行
# print(cs.fetchmany(2))
# 获取查询结果集中剩下的所有行
# print(cs.fetchall())
conn = sqlite3.connect('test.db')
cur = conn.cursor()
# sql = "DROP TABLE IF EXISTS 'bilibili_user_info';"
# cur.execute(sql)
cur.execute('''CREATE TABLE IF NOT EXISTS discover_movies
(id integer PRIMARY KEY,
adult varchar(20),
backdrop_path varchar(20), 
genre_ids varchar(20),
original_language varchar(50),
original_title varchar(50),
overview varchar(250),
popularity varchar(50), 
poster_path varchar(50), 
release_date varchar(50), 
title varchar(50),
video, varchar(50),
vote_average varchar(50), 
vote_count varchar(50)
);''')
# sql ='''CREATE TABLE movie_detail (
#             id                INTEGER       PRIMARY KEY,
#             adult             BOOLEAN (20),
#             belongs_to_collection VARCHAR (500),
#             budget            INTEGER,
#             genres            VARCHAR (50),
#             backdrop_path     VARCHAR (20),
#             homepage          VARCHAR (20),
#             imdb_id           VARCHAR (20),
#             original_language VARCHAR (50),
#             original_title    VARCHAR (50),
#             popularity        NUMERIC (50),
#             poster_path       VARCHAR (50),
#             production_companies  ARCHAR (50),
#             production_countries  ARCHAR (50),
#             release_date      VARCHAR (50),
#             revenue           INTEGER,
#             runtime           INTEGER,
#             spoken_languages  VARCHAR (50),
#             status            VARCHAR (50),
#             tagline           VARCHAR (50),
#             title             VARCHAR (50),
#             video             VARCHAR (10),
#             vote_average      VARCHAR (50),
#             vote_count        VARCHAR (50),
#             overview          VARCHAR (500) 
#         );'''

# cs.execute(sql)
# print(cs.fetchone())
cs.close()
conn.close()

