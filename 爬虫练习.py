# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib.request
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}

def get_html(url):
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        parse_html(response.text)
    else:
        print('Error',response.status_code)

def parse_html(content):
    soup = BeautifulSoup(content,'lxml')
    # print(soup.text.strip())
    ass = soup.find_all('div',class_ = 'play-box')
    for a in ass:
        print(a.text)
    
    video_ = soup.select_one('div.play-box video')
    print(ass,video_)
    
if __name__ == '__main__':
    url = 'https://www.vmovier.com/62797?from=index_new_title'
    get_html(url)
   