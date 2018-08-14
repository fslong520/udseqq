#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 多进程、多线程、异步io学习 '

__author__ = 'fslong'
__version__ = '0.0.1'

import asyncio
import multiprocessing
import threading, time, queue


def job(j):
    print('子线程/子进程:%s' % (j + 1))
    print('线程数量:', threading.active_count())
    #print('线程:', threading.current_thread())
    for i in range(1000000):
        j += i
    #time.sleep(3)
    return j


def job1(j, q):
    print('子线程/子进程:%s' % (j + 1))
    print('线程数量:', threading.active_count())
    #print('线程:', threading.current_thread())
    for i in range(1000000):
        j += i
    #time.sleep(3)
    q.put(j)
    return j


async def yibu(j, result):
    print('子线程/子进程:%s' % (j + 1))
    print('线程数量:', threading.active_count())
    #print('线程:', threading.current_thread())
    for i in range(1000000):
        j += i
    result.append(j)


def mp():
    pool = multiprocessing.Pool()
    result = []
    for i in range(100):
        res = pool.apply_async(job, args=(i, ))
        result.append(res.get())
    pool.close()
    pool.join()
    return result


def loop():
    q = queue.Queue()
    result = []
    threads = []
    for i in range(100):
        t = threading.Thread(
            target=job1, args=(
                i,
                q,
            ))
        t.start()
        threads.append(t)
    for i in threads:        
        i.join()
        result.append(q.get())
    return result


def yibuIo():
    result = []
    loop = asyncio.get_event_loop()
    task = [yibu(i, result) for i in range(100)]
    loop.run_until_complete(asyncio.wait(task))    
    return result


if __name__ == '__main__':
    
    start1 = time.time()
    i = 0
    while i < 10:
        i += 1
        result = []
        for j in range(100):
            result.append(job(j))
        #print(result)
    end1 = time.time()    

    start2 = time.time()
    i = 0
    while i < 10:
        i += 1
        mp()
        #print(mp())
    end2 = time.time()
    
    
    start3 = time.time()
    i = 0
    while i < 10:
        i += 1
        loop()
        #print(loop())
    end3 = time.time()
    

    start4 = time.time()
    i = 0
    while i < 10:
        i += 1
        yibuIo()
        #print(yibuIo())
    end4 = time.time()
    print('采用单线程执行了10次耗时：%s' % (end1 - start1))
    print('采用多线程执行了10次耗时：%s' % (end3 - start3))
    print('采用多进程执行了10次耗时：%s' % (end2 - start2))    
    print('采用异步IO执行了10次耗时：%s' % (end4 - start4))
    #input()
