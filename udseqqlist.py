#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 获取双色球历史数据 '

__author__ = 'fslong'
__version__ = '0.0.1'

from spider import Spider
import requests, pyquery
import traceback, asyncio
from lxml import etree


class Udseqq(Spider):
    # 获取页面数据的函数
    def getPage(self):
        self.Url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
        req = requests.get(self.Url, headers=self.headers, timeout=15)
        PQreq = pyquery.PyQuery(req.text)
        pageStr = PQreq('.pg').text()
        pages = pageStr.split('\n')[1]
        num = pageStr.split('\n')[3]
        try:
            pages = int(pages)
            num = int(num)
            return (pages, num)
        except:
            traceback.print_exc()
            return False

    # 获取每个页面的数据:
    def getData(self, page):
        self.Url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%s.html' % page
        req = requests.get('https://www.baidu.com/', headers=self.headers, timeout=15)     
        PQreq=pyquery.PyQuery(req.text)('.s_ipt')   
        print(PQreq.attr.name)
        

if __name__ == '__main__':
    udseqq = Udseqq()
    #print(udseqq.getPage())
    udseqq.getData(1)