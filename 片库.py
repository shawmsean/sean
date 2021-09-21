# -*- coding:utf-8 -*-
from concurrent import futures
from 爬虫练习2 import download_img1
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import socket
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
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
    # lis = soup.select('body > main > div > ul > li')
    imgs = soup.select('body > main > div > ul > li > div.li-img.cover > a > img')
    for img in imgs:
        img_url = img['data-src']
        filename = img['alt']
        print(img_url,filename)
        try:
            download_img(img_url,filename)
        except:
            pass
def download_img(img_url,filename):
    suffix = img_url.split('.')[-1]   
    dirs = 'C:\\Users\\shawm\\Desktop\\3'
    if not os.path.exists(dirs):
        dir = os.makedirs(dirs)
    con = requests.get(img_url).content
    filename = dirs+'\\'+ filename + '.' +suffix
    with open(filename,'wb') as f:
        f.write(con)
    # socket.setdefaulttimeout(5)
    # try:
    #     urlretrieve(img_url,filename=dirs+'\\'+ filename + '.' +suffix)
    # except socket.timeout:
    #     count = 1
    #     while count <= 5:
    #         try:
    #             urlretrieve(img_url,filename=dirs+'\\'+ filename + '.' +suffix)
    #             break
    #         except socket.timeout:
    #             err_info = f'Reloading for {count} time' if count == 1 else f'Reloading for {count}times.'
    #             print(err_info)
    #             count +=1
    #     if count >= 5:
    #         print('download job failed!')
#可以定义一个function，它接受link和{}的list，然后它将遍历list并下载{}，然后为每个list创建一个thread，并使其以{}为目标
# def download_files(url, filenames):
#     for filename in filenames:
#         urlretrieve(os.path.join(url,filename))

# # then create the lists and threads
# url = 'test.url'
# files = [[file1, file2, file3....], [file21, file22, file23...]...]
# for lst in files:
#     threading.Thread(target=download_files, args=(url, lst)).start()
def main():
    with ThreadPoolExecutor(max_workers=5) as t:
        obj_list = []
        begin = time.time()
        base_url = 'https://www.pianku.li/mv/'
        for num in range(1,2):
            url = base_url + '------' + str(num) + '.html'
            obj = t.submit(get_html,url)
            obj_list.append(obj)

        for future in as_completed(obj_list):
            data = future.result()
            print(data)
        times = time.time()-begin
        print(times)


if __name__ == '__main__':
    main()
