#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/17 17:53 
# @Author : TETE
# @File : 18_多线程.py

#导入日志模块
import _thread
import logging
import threading
from time import sleep,ctime

'''
logging.basicConfig(**kwargs)函数用于指定“要记录的日志级别”、“日志格式”、“日志输出位置”、“日志文件的打开模式”等信息
创建一个level=logging.INFO级别的日志
'''
logging.basicConfig(level=logging.INFO)

#1.先理解线程
# ctime 表示当前时间
# def loop0():
#     logging.info("start loop0 at"+ctime())
#     sleep(4)
#     logging.info("end loop0 at"+ctime())
#
# def loop1():
#     logging.info("start loop1  at" + ctime())
#     sleep(2)
#     logging.info("end loop1 at " + ctime())
#
# def main():
#     logging.info("start all at "+ctime())
#     loop0()
#     loop1()
#     logging.info("end all at "+ctime())
#
# if __name__ == '__main__':
#     main()

#2.添加_thread
# def loop0():
#     logging.info("start loop0 at"+ctime())
#     sleep(4)
#     logging.info("end loop0 at"+ctime())
#
#
# def loop1():
#     logging.info("start loop1  at" + ctime())
#     sleep(2)
#     logging.info("end loop1 at " + ctime())
#
# def main():
#     logging.info("start all at "+ctime())
#     _thread.start_new_thread(loop0,())
#     _thread.start_new_thread(loop1,())
#     sleep(6) #所有线程的总和
#     logging.info("end all at "+ctime())
#
#
# if __name__ == '__main__':
#     main()

#3.加锁,优化代码，使其自动判断子线程所需时间，并释放锁：
# def loop(nloop,nsec,lock):
#     #需要对nloop转格式
#     logging.info("start loop"+str(nloop)+" at "+ctime())
#     sleep(nsec)
#     logging.info("end loop"+str(nloop)+ " at "+ctime())
#     lock.release()
#
# loops=[2,4]
# def main():
#     logging.info("start all at "+ctime())
#     locks = []
#     nloops = range(len(loops))
#     for i in nloops:
#         lock = _thread.allocate_lock()
#         lock.acquire()
#         locks.append(lock)
#     for i in nloops:
#         _thread.start_new_thread(loop,(i,loops[i],locks[i]))
#     for i in nloops:
#         while locks[i].locked():pass
#
#     logging.info("end all at "+ctime())
#
#
# if __name__ == '__main__':
#     main()

#4.优化代码，增加 threading 方法
# def loop(nloop,nsec):
#     #需要对nloop转格式
#     logging.info("start loop"+str(nloop)+" at "+ctime())
#     sleep(nsec)
#     logging.info("end loop"+str(nloop)+ " at "+ctime())
#
# loops=[2,4]
# def main():
#     logging.info("start all at "+ctime())
#     threads = []
#     nloops = range(len(loops))
#     for i in nloops:
#         t = threading.Thread(target=loop,args=(i,loops[i]))
#         threads.append(t)
#     for i in nloops:
#         threads[i].start()
#     for i in nloops:
#         #如果有线程在时会阻塞主线程
#         threads[i].join()
#
#     logging.info("end all at "+ctime())
#
#
# if __name__ == '__main__':
#     main()

#5.继承threading类
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func =func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def loop(nloop,nsec):
    #需要对nloop转格式
    logging.info("start loop"+str(nloop)+" at "+ctime())
    sleep(nsec)
    logging.info("end loop"+str(nloop)+ " at "+ctime())

loops=[2,4]
def main():
    logging.info("start all at "+ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        #如果有线程在时会阻塞主线程
        threads[i].join()

    logging.info("end all at "+ctime())


if __name__ == '__main__':
    main()