#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 将双色球的数据从数据库中导出成json，现阶段用起来方便 '

__author__ = 'fslong'
__version__ = '0.0.1'

from dict2MySql import MySQLConnection
import json

if __name__ == '__main__':
    mysql = MySQLConnection(dbName='UDSEQQ', tabName='udseqq')
    data = mysql.selectData()
    dataList = []
    for i in data:
        dataList.append({
            'id': int(i[0]),
            'date': i[1],
            'red': i[2].split('-')[0:-1],
            'blue': int(i[2].split('-')[-1])
        })
    with open('udseqq.json', 'w', encoding='utf-8') as f:
        print('打开文件成功，尝试写入双色球数据...')
        json.dump(dataList, f, ensure_ascii=False)
        print('双色球数据写入完毕，请打开json文件查看。')
