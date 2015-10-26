#!/usr/bin/env python
#coding: utf-8 
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:.py  -*-*-
#-*-*-  Date:  

def init(data):
	data['frist'] = {}
	data['middle'] = {}
	data['last'] = {}

def lookup(data, label, name):
	return data[label].get(name)
	
def store(data, *full_name):
	for f in full_name:
		names = f.split()
		if len(names)  == 2 :names.insert(1,'')
		labels = 'frist', 'middle', 'last'
		for label, name in zip(labels, names):
			people = lookup(data, label, name)
			if people:
				people.append(f)#这边竟然修改了data列表本身，难以理解
				'''
					这样理解吧，get 返回多个结果时用的是列表
					people 就是这个列表
					列表是可以被修改的，改people，就是改原列表
					原列表又是字典的字典的值
					说是说通了，理解并运用就难了，哪能搞得清呢？这么多弯弯绕
				'''
			else:
				data[label][name] = [f]#高明，用一个列表来作字典的字典的value，高明，

mynames = {}
#mynames = {'frist': {'frist_name': ['','']}, 'last': {1: ['xu xiao wen']}, 'middle': {1: ['xu xiao wen']}}
init(mynames)

store(mynames, 'shen qing long', 'zhu jian qiang', 'shen lian')
store(mynames, 'xu xiao wen')
store(mynames, 'xu da wen')
store(mynames, 'zhang xiao wen')


print mynames
print lookup(mynames, 'frist', 'xu')


s = raw_input("请输入一个句子……")
screen_width = 80
s_width = len(s)
b_w = s_width + 6
left = (screen_width - s_width)//2
print ' '*left + '+' + '-'*(b_w-2) + '+'
print ' '*left + '|  ' + ' '*s_width + '  |'
print ' '*left + '|  ' + s + '  |'
print ' '*left + '|  ' + ' '*s_width + '  |'
print ' '*left + '+' + '-'*(b_w-2) + '+'

users = ('watt','jim','tom')
while raw_input("please input your name...") in users:
	print True
	