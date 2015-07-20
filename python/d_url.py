<<<<<<< HEAD
#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:
#Filename: 
#Content:

=======
>>>>>>> master
import urllib
import httplib
import re
import urlparse
import json
def ip(host_addr,format="dot"):
    '''
    describe:
        function try to find the ip addr of the given host addr
    params:
        host_addr:the format like www.baidu.com or http://www.baidu.com
        format:the format of return value
                dot=&gt;ip string like 123.121.121.21,
                num=&gt;number format like 327382483
    return :IP string list or number list when num specified
    '''
    query_url='http://ip.chinaz.com/?'
    if host_addr.startswith("http"):
        req_url=urlparse.urlsplit(host_addr).netloc
    else:
        req_url=host_addr
    r=urllib.urlopen(query_url+"IP="+req_url)
    ipRex=r':\s+([\d\.]*)\s'
    try:
        if r !=None:
            context=r.read()
            rst=re.findall(ipRex,context)          
            if rst!=None:
                if format=="num":
                    rss=[]
                    for rs in rst:                    
                        sum=0
                        for  f in enumerate(rs.split('.')):
                            sum += int(f[1])&lt
                        rss.append(str(sum))
                    del rst
                    rst=rss
                print rst
				#return rst
        return None
    except :
        return None
ip
