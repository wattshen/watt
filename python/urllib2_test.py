#!/usr/bin/env python
#coding=gbk
#coding=utf-8
#-*- coding: UTF-8 -*- 

#����urllib2ģ��,����֮��URL��Դ,����read��ȡ,����֮�浽�ļ�
import urllib2
import socket
import sys

host = 'www.google.com'
url = 'http://' + host
ip = socket.gethostbyname_ex(host)    #��ȡ������Ӧ��IP
#file = socket.getaddrinfo(url,None)
files = socket.gethostbyaddr('183.207.228.120')#183.207.229.146

#socket.gethostbyname(socket.gethostname())    #��ȡ������
#socket.gethostbyname_ex(socket.gethostname())    #�����������жϳ�IP


#response = urllib2.urlopen(url)
#html = response.read()
#f = open(r'g:\watt\test\google_0320.html','a')
#f.write(html)
#f.close()

print ip
print files