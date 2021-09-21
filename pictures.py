# -*- coding:utf-8 -*-
import sqlite3
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
from concurrent.futures import ThreadPoolExecutor
import time
import json
from 片库copy import download_img,main_multi_download
conn = sqlite3.connect('test.db')
cur = conn.cursor()
sql = 'select title,backdrop_path,poster_path from discover_movies where vote_average >= 7'
cur.execute(sql)
results = cur.fetchall()
base_url = 'https://www.themoviedb.org/t/p/original'
titles =[]
backdrop_paths = []
poster_paths = []
for result in results:
    title = result[0]
    backdrop_path = base_url+result[1]
    poster_path = base_url+result[2]
    titles.append(title)
    backdrop_paths.append(backdrop_path)
    poster_paths.append(poster_path)
main_multi_download(download_img,backdrop_paths,titles)
main_multi_download(download_img,poster_paths,titles,[i for i in range(len(titles))])