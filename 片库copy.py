# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
from concurrent.futures import ThreadPoolExecutor
import time
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}

def get_html(url):
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        download_dicts = parse_html(response.text)
        return download_dicts
    else:
        print('Error',response.status_code)

def parse_html(content):
    soup = BeautifulSoup(content,'lxml')
    # lis = soup.select('body > main > div > ul > li')
    imgs = soup.select('body > main > div > ul > li > div.li-img.cover > a > img')
    dicts = {}
    for img in imgs:
        img_url = img['data-src']
        filename = img['alt']
        dicts[filename] = img_url
    # print(dicts)
    return dicts
def download_img(img_url,filename,type=''):
    suffix = img_url.split('.')[-1]
    try:   
        dirs = 'C:\\Users\\shawm\\Desktop\\test\\pics'
        if not os.path.exists(dirs):
            dir = os.makedirs(dirs)
    except FileExistsError:
        print('File existed!')
    try:
        con = requests.get(img_url).content
    except:
        pass
    filename = dirs+'\\'+ filename + str(type) +'.' +suffix
    try:
        with open(filename,'wb') as f:
            f.write(con)
    except:
        pass
def get_url_and_filename_list():
    base_url = 'https://www.pianku.li/mv/'
    pages = int(input('请问你要几页的数据\n'))
    print('开始获取……………………………………')
    url_list = []
    begin = time.time()
    for num in range(1,pages+1):
        url = base_url + '------' + str(num) + '.html'
        url_list.append(url)
    # print(url_list)
    list_url = []
    list_filename = []
    #get filename and file'url with multi-thread
    with ThreadPoolExecutor(max_workers=8) as executor_get_list:
        try:
            for list_dict in executor_get_list.map(get_html,url_list):
                for filename,img_url in list_dict.items():
                    list_url.append(img_url)
                    list_filename.append(filename)
        except:
            pass
    endtime_getfilename_url = time.time()-begin
    print(f'get url list and filename list in {endtime_getfilename_url}s with {len(list_url)} items!')
    filename = 'url.json'
    filename_name = 'name.json'
    with open(filename,'w') as f:
        json.dump(list_url,f)  
    with open(filename_name,'w') as f:
        json.dump(list_filename,f)  
    with open(filename) as f:
        dict_re =json.load(f)
        # print(dict_re)
    return list_url,list_filename

def main_multi_download(func,*list):
    # download file with multi-thread
    begin = time.time()
    # executor = ThreadPoolExecutor(max_workers=20)  #使用with操作符，使得当任务执行完成之后，自动执行shutdown函数，而无需编写相关释放代码
    i = 1
    with ThreadPoolExecutor(max_workers=20) as executor:
        for result in executor.map(func, *list):
            try:
                print("task{}:下载完成！".format(i))
                i += 1
            except:
                pass
    times = time.time()-begin
    print(times)

if __name__ == '__main__':
    list_url1,list_filename1 = get_url_and_filename_list()
    # main_multi_download(download_img,list_url1,list_filename1)
