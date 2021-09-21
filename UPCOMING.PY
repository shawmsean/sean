# -*- coding:utf-8 -*-
import sqlite3
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
from concurrent.futures import ThreadPoolExecutor
import time
import json
# base_url = 'https://api.themoviedb.org/3/movie/popular'
# params = {}
# params['api_key'] = '4961df668a94cc4f5c85729c24e1303d'
# params['language'] = ''
# params['page'] = 100
# params['region'] = 'CN'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}
urls = []
for i in range(100):
    page = i
    region = 'CN'
    url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=4961df668a94cc4f5c85729c24e1303d&page={}&region={}'.format(page,region)
    urls.append(url)
def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}
    response = requests.session().get(url=url,headers=headers)
    if response.status_code == 200:
        json_data =response.text
    else:
        print('Failed,{}'.format(response.status_code))
    # print(json_data)
    json_dict = json.loads(json_data)
    results = json_dict['results']
    for result in results:
        adult = result['adult']
        id = result['id']
        print(id)
        backdrop_path = result['backdrop_path']
        genre_ids = result['genre_ids']
        # for id in genre_ids:
        #     genre_ids = ''.join(id)
        original_language= result['original_language']
        original_title= result['original_title']
        overview = result['overview']
        overview = overview.replace('\"','')
        # print(overview)
        popularity = result['popularity'] 
        poster_path = result['poster_path']
        release_date = result['release_date']
        title = result['title']
        video = result['video']
        vote_average = result['vote_average']
        vote_count = result['vote_count']
        conn = sqlite3.connect('test.db')
        cur = conn.cursor()
        sql ='''INSERT INTO top_rated(id, adult, backdrop_path, genre_ids, original_language, original_title, \
                                    overview, popularity, poster_path, release_date, title, video, vote_average, \
                                    vote_count) \
                        VALUES ("%s","%s","%s","%s","%s","%s","%s","%s",\
                                "%s","%s","%s","%s","%s", "%s")'''% \
                                    (id, adult, backdrop_path, genre_ids, original_language, original_title, \
                                    overview, popularity, poster_path, release_date, title, video, vote_average, \
                                    vote_count)                            
        cur.execute(sql)
        conn.commit()
if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(get_data,urls)