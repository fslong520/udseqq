#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 获取双色球历史数据 '

__author__ = 'fslong'
__version__ = '0.0.1'

import asyncio
import traceback, time, os

import pyquery
import requests, random
from lxml import etree

from spider import Spider
from dict2MySql import MySQLConnection


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
            return [pages, num]
        except:
            traceback.print_exc()
            return False

    # 获取每个页面的数据:
    def getData(self, page):
        print('\n开始下载第%s页数据....' % page)
        self.Url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%s.html' % page
        #req = requests.get(self.Url, headers=self.headers, timeout=15)
        #print(req.text.replace(' ',''))
        PQreq = pyquery.PyQuery(url=self.Url)('tr').items()
        data = []
        for i in PQreq:
            num = ''
            for j in i('td em').items():
                num += '-' + j.html()

            datastr = ''
            for k in i('td').items():
                if '-' in k.text():
                    datastr += k.text() + '~'
                if len(k.text()) == 7:
                    try:
                        int(k.text())
                        datastr += k.text() + '~'
                    except:
                        pass
            if datastr != '' and ' ' not in datastr:
                datastr = datastr + num[1:]
                data.append(datastr)
        udseqqList = []
        for i in data:
            print(i)
            udseqqList.append({
                'id': i.split('~')[1],
                'date': i.split('~')[0],
                'udseqq': i.split('~')[2],
                'url': self.Url,
            })
            self.results.append({
                'id': i.split('~')[1],
                'date': i.split('~')[0],
                'udseqq': i.split('~')[2],
                'url': self.Url,
            })
        print('第%s页数据下载完毕。\n' % page)
        return udseqqList

    # 异步IO的方式存入数据库，首次使用:
    async def saveUdseqqData2sql(self, page):
        url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%s.html' % page
        mysql = MySQLConnection(dbName='UDSEQQ', tabName='udseqq')
        
        a = mysql.selectData('url', url)
        if a==None:
            a=()            
        if a != ():
            print('第%s页的数据已经存过了!' % page)
        else:
            data = self.getData(page)
            print('开始存储第%s页数据...\n' % page)
            for i in data:
                #mysql.createTable(i)
                #print(mysql.selectData('id',i['id']))
                if mysql.selectData('id', i['id']) != ():
                    print('第%s期的双色球数据已经在数据库当中啦，别再存了哟！' % i['id'])
                else:
                    mysql.insertData(i)
            print('第%s页数据存储完毕。\n' % page)

    # 后续数据更新使用：
    def saveUdseqqData2sql1(self, page):
        mysql = MySQLConnection(dbName='UDSEQQ', tabName='udseqq')
        data = self.getData(page)
        print('开始存储第%s页数据...\n' % page)
        for i in data:
            #mysql.createTable(i)
            #print(mysql.selectData('id',i['id']))
            if mysql.selectData('id', i['id']) != ():
                print('从第%s期往前的双色球数据已经在数据库当中啦，别再存了哟！如发现有遗漏，请多次执行本程序，谢谢。' %
                      i['id'])
                os._exit(0)
            else:
                mysql.insertData(i)
        print('第%s页数据存储完毕。\n' % page)


if __name__ == '__main__':
    udseqq = Udseqq()
    dataNum = udseqq.getPage()
    print('总共有%s页%s条数据。\n' % (dataNum[0], dataNum[1]))
    a = input('数据更新(u)还是重新抓取(a)所有数据？\n')
    if a == 'a':
        print('\n开始尝试抓取所有双色球的数据，请多次执行直到不再报错且不在显示新下载的数据...\n')
        loop = asyncio.get_event_loop()
        tasks = [udseqq.saveUdseqqData2sql(i + 1) for i in range(dataNum[0])]
        loop.run_until_complete(asyncio.wait(tasks))
        print('数据下载完毕，请前往数据库查看。')
    else:
        for i in range(dataNum[0]):
            udseqq.saveUdseqqData2sql1(i + 1)
