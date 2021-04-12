# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 15:57
# @Author  : TeTe
# @File    : 33.文件操作.py
'''
读：open(path/filename,'rt') --->返回值：stream（管道），如果不指定模式，默认的模式是’rt‘
stream.read() --->读取管道中的内容
注意：
1.如果传递的path/filename有误，则会报错：FileNotFoundError
2.如果是图片，则不能使用默认的读取方式，mode = ’rb‘
3.方法总结：
read()：读取所有内容
readline():每次读取一行内容
readlines()：读取所有的行，保存到列表中
readable()：判断是否可读
'''
# stream = open(r'D:\hello.txt')

# container = stream.read()
# print(container)

# result = stream.readable() #判断是否可以读取， True False
# print(result)

# while True:
#     line = stream.readline()  #每次读行时会自动加换行符
#     print(line)
#     if  not line:
#         break

# lines = stream.readlines()  #返回值是列表
# print(lines)
# for i in lines:
#     print(i,end='')

# stream = open(r'D:\桌面文件\风景图片\timg (1).jpg','rb')
#
# container = stream.read()
# print(container)

'''
mode=’w‘，表示就是写操作
方法：
write(内容)  每次都会将原来的内容清空，然后写当前的部分
writelines(Iterable) :没有换行效果，可以自己加 \n 进行换行。

如果mode=’a‘,在原有基础上进行追加。
 
'''

# stream = open(r'D:\桌面文件\风景图片\aa.txt','w')
#
# result = stream.write('花花')
#
# stream.write('tete')
#
# stream.writelines(['赌神\n','赌圣','赌侠'])


# stream = open(r'D:\桌面文件\风景图片\aa.txt','a')
#
# result = stream.write('\n花花02')
#
# stream.write('tete02')
#
# stream.writelines(['赌神02\n','赌圣02','赌侠02'])
#
# stream.close()  #释放资源

'''
原文件：r'D:\桌面文件\风景图片\timg (3).jpg'
目标文件：r'E:\上传的资料\timg (3)-2.jpg'

with 结合open使用，可以帮助我们自动释放资源
'''

# with open(r'D:\桌面文件\风景图片\timg (3).jpg','rb') as stream:
#     container = stream.read()  #读取文件内容
#
#     with open(r'E:\上传的资料\timg (3)-2.jpg','wb') as wstream:
#         wstream.write(container)
#
# print('文件复制完成！')


'''
批量复制（复制文件夹）：
原文件夹：r'D:\桌面文件\风景图片'
目标文件夹：r'E:\上传的资料'

结合使用模块os（操作系统模块）:
os.path:
os.path.dirname(__file__) :获取当前文件所在的文件目录（绝对路径）
os.path.join(path,'')：返回的是一个拼接后的新的路径。
'''
import os

# os.path.dirname(__file__)： #获取当前文件夹的绝对路径
src_path = r'D:\桌面文件\风景图片'
target_path = r'E:\上传的资料'

#封装成函数
def copy(src,target):
    if os.path.isdir(src) and os.path.isdir(target): #判断是否是文件夹
        filelist = os.listdir(src)  #文件列表

        #遍历目录下的所有文件，file 是文件名称，例如aa.txt
        for file in filelist:
            #生成一个新的目录
            path = os.path.join(src,file)

            #进行读取
            with open(path,'rb') as rstream:
                container = rstream.read()
                path1 = os.path.join(target,file)
                with open(path1,'wb') as wstream:
                    wstream.write(container)

        else:
            print('复制完毕！')

#调用当前函数
copy(src_path,target_path)
