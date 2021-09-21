#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import requests
import re
import json
qqmusic_api = 'http://music.jsososo.com/apiQ'
cookie = 'tvfe_boss_uuid=9d234bd1a9516dc7; pgv_pvid=3957925100; RK=iMrcO1erZ0; ptcz=775aa3e19ebd2250828f53fb922a85a23899097db36385f77fd11c63288d4ee4; o_cookie=565095659; pac_uid=1_565095659; ts_uid=8064105479; fqm_pvqid=26c363e8-ac47-43e0-b312-0c01ed41159f; fqm_sessionid=f69940fe-aeab-43a0-85fd-dc2e884f8bca; pgv_info=ssid=s2256061375; ts_refer=jsososo.github.io/; _qpsvr_localtk=0.9789204053656209; login_type=1; euin=7KCkoeEk7w4q; wxopenid=; qm_keyst=Q_H_L_24KgW460ea55dun-ttTAnLlXI-6J6s9yU1h4jsJz3wkL4rVkK5_r3LLpRdL3rzF; psrf_musickey_createtime=1629530433; psrf_qqaccess_token=A7485E42EC0AC2C81B3E960747DE3E85; wxrefresh_token=; psrf_qqrefresh_token=D855A3277E6965C229769B8FDA180D30; qqmusic_key=Q_H_L_24KgW460ea55dun-ttTAnLlXI-6J6s9yU1h4jsJz3wkL4rVkK5_r3LLpRdL3rzF; psrf_qqopenid=8CFD378C27D1451ADE27A64CBAC0F56E; tmeLoginType=2; wxunionid=; uin=565095659; qm_keyst=Q_H_L_24KgW460ea55dun-ttTAnLlXI-6J6s9yU1h4jsJz3wkL4rVkK5_r3LLpRdL3rzF; psrf_qqunionid=; psrf_access_token_expiresAt=1637306433; ts_last=y.qq.com/n/ryqq/player'
def get_html(url,cookie=cookie):
    headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               'Host':'zhannei.baidu.com',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    if cookie != '':
        h = headers
        h['cookie'] = cookie
        r = requests.get(url,headers=h)
    else:
        r = requests.get(url,headers=headers)
    return r.text
def qqtuijiangedan():
    
    gedans = []
    r = get_html(qqmusic_api + '/recommend/playlist/')
    j = json.loads(r)
    glist = j['data']['list']
    for index in range(len(glist)):
        gd ={}
        gd['name'] = glist[index]['title']
        gd['thumb'] = glist[index]['cover_url_big']
        gd['url'] = 'https://y.qq.com/n/yqq/playlist/' + str(glist[index]['tid']) + '.html'
        gd['info'] = {'plot':zh(glist[index]['access_num']) + ' 播放量'}
        gd['info']['cast']= [glist[index]['creator_info']['nick']]
        gedans.append(gd)
    return gedans

########################################### 歌单详细信息api ###########################################
def one63playlist(id):
    gedans = []
    r = get_html(netease_api + '/playlist/detail?id=' + str(id))
    j = json.loads(r)
    glist = j['playlist']['trackIds']
    songs = ''
    for index in range(len(glist)):
        if index == 0:
            songs += str(glist[index]['id'])
        else:
            songs += ',' + str(glist[index]['id'])
    #mp3详情
    r1 = get_html(netease_api + '/song/detail?ids=' + songs)
    j1 = json.loads(r1)
    mp3detail = j1['songs']
    # #mp3 url
    # r2 = get_html(netease_api + '/song/url?id=' + songs)
    # j2 = json.loads(r2)
    # mp3urls = j2['data']
    # pDialog = xbmcgui.DialogProgress()
    # pDialog.create('网易云音乐', '努力从母猪厂的土豆服务器偷mp3中...(0%)')
    for index in range(len(mp3detail)):
        # pDialog.update(int(100*(float(index)/float(len(mp3detail)))), '努力从母猪厂的土豆服务器偷mp3中...('+str(int(100*(float(index)/float(len(mp3detail)))))+'%)')
        # #r2 = get_html(netease_api + '/song/url?id=' + str(mp3detail[index]['id']))
        # #j2 = json.loads(r2)
        gd ={}
        gd['name'] = mp3detail[index]['name']
        gd['thumb'] = mp3detail[index]['al']['picUrl']
        # gdurl = ''
        # for i in range(len(mp3urls)):
        #     if int(mp3urls[i]['id']) == int(mp3detail[index]['id']):
        #         gdurl = mp3urls[i]['url']
        # if gdurl == '':
        #     gd['name'] += ' - [无版权]'
        # gd['url'] = gdurl
        if xbmcplugin.getSetting(int(sys.argv[1]), 'httpswitch') == 'true':
            gd['url'] = 'http'
        else:
            gd['url'] = 'https'
        gd['url'] += '://music.163.com/song/media/outer/url?id=' + str(mp3detail[index]['id']) + '.mp3'
        gd['info'] = {'title':mp3detail[index]['name'],'album':mp3detail[index]['al']['name'],'artist':mp3detail[index]['ar'][0]['name'],'mediatype':'song'}
        #gd['url'] = j2['data'][0]['url']
        gedans.append(gd)
    return gedans

def qqplaylist(id):
    id = '2429907335'
    gedans = []
    r = get_html(qqmusic_api + '/songlist?id=' + str(id))
    j = json.loads(r)
    # print(j)
    glist = j['data']['songlist']
    print('--------------------------------------------------------------------------------------------------------------')
    songs= ''
    for index in range(len(glist)):
        if index == 0:
            songs += glist[index]['songmid']
        else:
            songs += ',' + glist[index]['songmid']
        url = qqmusic_api + '/song/urls?id=' + songs
        # print(url)
    r1 = get_html(url)
    # print(r1)
    j1 = json.loads(r1)
    # print(j1)
    mp3urls = j1['data']

    for index in range(len(glist)):
        
        if glist[index]['songmid'] in mp3urls:
            gd ={}
            gd['name'] = glist[index]['songname']
            gd['thumb'] = 'http://y.gtimg.cn/music/photo_new/T002R300x300M000' + glist[index]['albummid'] + '.jpg'
            gd['url'] = mp3urls[glist[index]['songmid']]
            gd['info'] = {'title':glist[index]['songname'],'album':glist[index]['albumname'],'artist':glist[index]['singer'][0]['name'],'mediatype':'song'}
            gedans.append(gd)
    return gedans
gedans = qqplaylist(34)
print(gedans)