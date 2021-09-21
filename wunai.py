# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
def get_video_url(url):
    driver = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
    # url = 'https://www.vmovier.com/62797?from=index_new_title'
    driver.get(url)
    sleep(1)
    video = driver.find_element_by_css_selector('#xpcplayer > div > div.xpcplayer-video-wrap > video')
    src = video.get_attribute('src')
    driver.close()
    return src