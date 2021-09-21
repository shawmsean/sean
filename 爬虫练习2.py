# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib
import os
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}

def get_html(url):
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        parse_html(response.text)
    else:
        print('Error',response.status_code)

def parse_html(content):
    soup = BeautifulSoup(content,'lxml')
    imgs = soup.select('div.foucebox > div.hd > ul > li img')
    titles = soup.select(' div.foucebox > div.hd > ul > li div.title')
    print('start downloading-----')
    start_time = time.time()
    for img_url,title in zip(imgs,titles):
        download_img(img_url['src'],title.text+'.jpg')
        download_img1(img_url['src'],title.text+'.jpg')
    end_time = time.time()
    # print(end_time)
    print(f'downloaded in {start_time-end_time}!')
def download_img(img_url,filename):
    dirs = 'C:\\Users\\shawm\\Desktop\\pics\\a'
    if not os.path.exists(dirs):
        dir = os.makedirs(dirs)      
    urllib.request.urlretrieve(img_url,filename=dirs+'\\'+ filename)
def download_img1(img_url,filename):
    dirs = 'C:\\Users\\shawm\\Desktop\\pics\\b'
    if not os.path.exists(dirs):
        dir = os.makedirs(dirs)
    con = requests.get(img_url).content
    filename=dirs+'\\'+ filename
    with open(filename,'wb') as f:
        f.write(con)


if __name__ == '__main__':
    # url = 'https://www.pianku.li/'
    # get_html(url)
    download_img('https://ks-xpc4.xpccdn.com/d1f777be-b1f6-43f3-b30e-cfbb68ea53d1.mp4','测试.mp4')
    download_img1('https://ks-xpc4.xpccdn.com/d1f777be-b1f6-43f3-b30e-cfbb68ea53d1.mp4','测试.mp4')
