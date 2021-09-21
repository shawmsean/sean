# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib
import os
from selenium import webdriver
from time import sleep

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}

def get_html(url):
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        parse_html(response.text)
    else:
        print('Error',response.status_code)

def parse_html(content):
    soup = BeautifulSoup(content,'lxml')
    h1s = soup.select('#post-list > li> div > h1 > a:nth-child(1)')
    i = 0
    for h in h1s:
        title = h['title']
        href = 'https://www.vmovier.com' + h['href']
        rps = requests.get(href,headers=headers)
        
        print(title,href)
        download_video(href,title)
        i += 1
    print(i)        
def download_video(video_url,filename):
    video_url = get_video_url(video_url)
    # print(video_url)
    suffix = video_url.split('.')[-1]
    # print(suffix)
    dirs = 'C:\\Users\\shawm\\Desktop\\videos'
    if not os.path.exists(dirs):
        dir = os.makedirs(dirs)      
    urllib.request.urlretrieve(video_url,filename=dirs+'\\'+ filename + '.' +suffix)
def get_video_url(url):
    driver = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
    # url = 'https://www.vmovier.com/62797?from=index_new_title'
    driver.get(url)
    sleep(1)
    video = driver.find_element_by_css_selector('#xpcplayer > div > div.xpcplayer-video-wrap > video')
    src = video.get_attribute('src')
    driver.close()
    return src
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
    url = 'https://www.vmovier.com/'
    get_html(url)

   

