#!/usr/bin/env python
#coding=gbk
#coding=utf-8
#-*- coding: UTF-8 -*- 

#导入urllib2模块,并以之打开URL资源,再以read读取,并交之存到文件
import urllib2
import socket
import sys

host = 'www.google.com'
url = 'http://' + host
ip = socket.gethostbyname_ex(host)    #获取域名对应的IP
#file = socket.getaddrinfo(url,None)
files = socket.gethostbyaddr('183.207.228.120')#183.207.229.146

#socket.gethostbyname(socket.gethostname())    #获取主机名
#socket.gethostbyname_ex(socket.gethostname())    #根据主机名判断出IP


#response = urllib2.urlopen(url)
#html = response.read()
#f = open(r'g:\watt\test\google_0320.html','a')
#f.write(html)
#f.close()

print ip
print files