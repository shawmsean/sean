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
def generate_urls():
    urls = []
    for id in range(630000,1000000):
        url = 'https://api.themoviedb.org/3/movie/{}?api_key=4961df668a94cc4f5c85729c24e1303d'.format(id)
        urls.append(url)
    return urls

def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}
    response = requests.session().get(url=url,headers=headers)
    if response.status_code == 200:
        json_data =response.text
    else:
        pass
        # print('Failed,{}'.format(response.status_code))
    # print(json_data)
    json_dict = json.loads(json_data)
    id = json_dict['id']
    adult = json_dict['adult']
    belongs_to_collection = json_dict['belongs_to_collection']
    budget = json_dict['budget']
    genres = json_dict['genres']
    backdrop_path = json_dict['backdrop_path']
    homepage = json_dict['homepage']
    imdb_id = json_dict['imdb_id']
    original_language = json_dict['original_language']
    original_title = json_dict['original_title']
    overview = json_dict['overview']
    overview = overview.replace('\"','')
    popularity = json_dict['popularity'] 
    poster_path = json_dict['poster_path']
    production_companies = json_dict['production_companies']
    production_countries = json_dict['production_countries']
    release_date = json_dict['release_date']
    revenue = json_dict['revenue']
    runtime = json_dict['runtime']
    spoken_languages = json_dict['spoken_languages']
    status = json_dict['status']
    tagline = json_dict['tagline']
    title = json_dict['title']
    video = json_dict['video']
    vote_average = json_dict['vote_average']
    vote_count = json_dict['vote_count']
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    sql ='''INSERT INTO movie_detail(id, adult,belongs_to_collection,budget, backdrop_path,imdb_id, genres, original_language, original_title, \
                                overview, popularity, poster_path, release_date, title, video, vote_average,production_companies,production_countries,\
                                vote_count,revenue,runtime,spoken_languages,status,tagline,homepage) \
                    VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",
                            "%s")'''% \
                                (id, adult,belongs_to_collection,budget, backdrop_path,imdb_id, genres, original_language, original_title, \
                                overview, popularity, poster_path, release_date, title, video, vote_average,production_companies,production_countries,\
                                vote_count,revenue,runtime,spoken_languages,status,tagline,homepage)                            
    cur.execute(sql)
    conn.commit()
if __name__ == "__main__":
    urls = generate_urls()
    begin = time.time()
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(get_data,urls)
    times = time.time()-begin
    print(times)
    # for url in urls:
    #     get_data(url)