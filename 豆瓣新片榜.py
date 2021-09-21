# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}

def get_html(url):
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        parse_html(response.text)
    else:
        print('Error',response.status_code)

def parse_html(content):
    soup = BeautifulSoup(content,'lxml')
    h1s = soup.select('div#content tr.item td>a')
    abstract = soup.select('div#content tr.item td p')
    rating_nums = soup.select('div#content tr.item span.rating_nums')
    pls = soup.select('div#content tr.item span.pl')
    # print(abstract)
    for a,ab,rating_num,pl in zip(h1s,abstract,rating_nums,pls):
        title = a['title']
        print(title)
        print(ab.text)
        print(rating_num.text,pl.text+'\n')
        print()
    
if __name__ == '__main__':
    url = 'https://movie.douban.com/chart'
    get_html(url)