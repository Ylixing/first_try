#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/21
# @Filename       : juhe.py
# @Desc           :


import json
import requests
from utils import proxy

def weather(cityname):
    """
    :param cityname: 城市名字
    :return: 返回实况天气
    """
    # key = '9a3e1fa6cb79d69f1594af5cb219a469'
    # api = 'http://v.juhe.cn/weather/index'
    # params = 'cityname=%s&key=%s' % (cityname, key)
    api = 'https://www.tianqiapi.com/api/'

    appid='67233298'
    appsecret='5yz1NQcS'
    ver='v1'
    params = 'appid=%s&appsecret=%s&version=%s&city=%s' % (appid,appsecret,ver,cityname)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url)
    json_data = json.loads(response.text)

    # print(json_data['wea'])
 #  今天
    sk = json_data.get('data')[0]
    print(sk.keys())

    # sk = result.get('sk')
    response = dict()
    response['temperature'] = sk.get('tem')
    # response['wind_direction'] = sk.get('wind_direction')
    response['wind_strength'] = sk.get('win_speed')
    response['humidity'] = sk.get('humidity')  # 湿度
    # response['time'] = sk.get('time')
    print(response)
    return response



def constellation(cons_name):
    '''
    :param cons_name: 星座名字
    :return: json 今天运势
    '''
    ## api权限限制，所以访问返回参数不正确
    # key = '638590d043a54639f3560b5381f5c4f0'
    # api = 'http://web.juhe.cn:8080/constellation/getAll'
    # types = ('today', 'tomorrow', 'week', 'month', 'year')
    # params = 'consName=%s&type=%s&key=%s' % (cons_name, types[0], key)
    # url = api + '?' + params
    # print(url)
    # response = requests.get(url=url, proxies=proxy.proxy())
    # data = json.loads(response.text)

    return {
        'name': cons_name,
        # 'text': data['summary']
        'text': 'I DO NOT CARE!'
    }


def stock(market, code):
    '''
    沪深股票
    :param market: 上交所 = sh, 深交所 = sz
    :param code: 股票编号
    :return:
    '''
    key = 'f887b09847c9bcde9801ca7aaa86513e'
    api = 'http://web.juhe.cn:8080/finance/stock/hs'
    params = 'gid=%s&key=%s' % (market + code, key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    data = data.get('result')[0].get('data')
    response = {
        'name': data.get('name'),
        'now_price': data.get('nowPri'),
        'today_min': data.get('todayMin'),
        'today_max': data.get('todayMax'),
        'start_price': data.get('todayStartPri'),
        'date': data.get('date'),
        'time': data.get('time')
    }
    response['is_rising'] = data.get('nowPri') > data.get('todayStartPri')
    sub = abs(float(data.get('nowPri')) - float(data.get('todayStartPri')))  # 差值
    response['sub'] = float('%.3f' % sub)
    return response


if __name__ == '__main__':
    data = weather('深圳')
