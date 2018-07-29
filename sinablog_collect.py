'''
验证运行环境: python 3.6.5
执行该python文件,然后按照提示输入需要开始下载的新浪博客文章的界面,然后回车执行,会自动下载当前博主此篇文章之前的所有博文

程序思路：从博客目录批量下载文件到本地，不做进一步的解析，只存储

获取所有博文思路：
1. 可以通过每篇博文中的前一篇的方式循环获取直到所有下载完毕 （本版采用该思路）
2. 读取页面关于总页数
3. 下载完目录列表中一页自然分页，读取下一页，直到没有下一页
'''

import urllib.request
from bs4 import BeautifulSoup

import os
import time

import http.client
 
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

# 根据url读取html界面
def getHtml(url_str):
    # 读取页面内容
    html_data = urllib.request.urlopen(url_str).read()
    return html_data

def getNowTimeStr():
    # 获取当前时间
    time_now = int(time.time())

    # 转换成localtime
    time_local = time.localtime(time_now)

    # 转换成新的时间格式(2016-05-09 18:59:20)
    time_str = time.strftime("%Y%m%d_%H%M%S", time_local)
    return time_str

def createDownloadDir():
    timestamp = getNowTimeStr()
    relative_path = "./" + timestamp

    # 采用相对路径，在当前目录创建下载任务所在的目录
    os.mkdir(relative_path)

    # 进入到下载目录中，后续操作都在这个目录下
    os.chdir(relative_path)

    # debug get to know whether in the right place
    # print(os.getcwd())

# 输入一个地址，完成解析博客标题名称，并按照该名称存储，同时需要判断并解析上一篇博客的地址，并返回
def resloveAndDownloadBlog(blog_url_str):
    blog_html = getHtml(blog_url_str)

    # 根据url地址创建bs对象，用于博客内容中的解析
    bs_obj = BeautifulSoup(blog_html, "lxml")
    # debug
    # print(bs_obj.prettify())

    # 获取当前博客标题，用于下载生成文件
    blog_title = bs_obj.find("h2", class_="titName SG_txta").string

    # 下载当前博客 str()用于解决字符串可能有符号的问题
    path = "./" + str(blog_title) + ".html"

    # path 出现一些特殊的符号会出现问题
    path = path.replace('\"', '“')
    path = path.replace('?', '？')
    path = path.replace('<', ' ')
    path = path.replace('>', ' ')
    path = path.replace(':', '：')
    path = path.replace('"', '“')
    path = path.replace('|', ' ')

    urllib.request.urlretrieve(blog_url_str, path)
    print("已完成下载博客%s篇" %(count_finished))

    try:
        # 获得下一篇博客的超链接， 用于接龙再紧接着下载另外一篇
        previous_blog_url = bs_obj.find("span", text="前一篇：").parent.a.get("href")
    except:
        print("下载完成！")
        exit()

    # 返回下一篇的地址
    return previous_blog_url


# main program logic

bloger_latest_url = input("请输入需要下载的最新博客地址：")

# 创建整个下载任务的单独目录，目录的当前程序所在目录，目录名为时间戳，创建完成后并进入目录
createDownloadDir()

next_blog_addr = bloger_latest_url

# 计数
count_finished = 1

while True:
    # 解析下载文件并接龙处理
    next_blog_addr = resloveAndDownloadBlog(next_blog_addr)
    count_finished += 1
