#!/usr/bin/env python
#coding: utf-8 
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:.py  -*-*-
#-*-*-  Date:  
#content:
import re
import sys
import copy
import datetime
'''
	新增对搜索关键字的处理
	编码过程中碰到了计数器导致的超出列表范围、仅返回最后一个值等问题
	遇到了将“返回值”作为参数传给其它函数，引发的“变量未定义”错误
'''
start_time = datetime.datetime.now()
#创建字典的4种方法
#1
keys_a = [("name","tom"),("age",35)]
content_a = dict(keys_a)
#2
content_b = dict(a= 1,b=2)
#3 本例情况，此法最方便
keys = ["SESSION_ID","F_DATE","F_TIME","F_MOBILE","F_CITY","F_BRAND","F_KEYWORD","SYSTEM_ID","CATEGORY_ID","F_ID","F_USER_AGENT","F_TOTAL","F_OFFSET","F_URL","F_TITLE","F_DESC","F_BACK_KEYWORD"]
content_c = {}.fromkeys(keys)
#4 此法最清晰
content = {
	"SESSION_ID":None,
	"F_DATE":None,
	"F_TIME":None,
	"F_MOBILE":None,
	"F_CITY":None,
	"F_BRAND":None,
	"F_KEYWORD":None,
	"SYSTEM_ID":None,
	"CATEGORY_ID":None,
	"F_ID":None,
	"F_USER_AGENT":None,
	"F_TOTAL":None,
	"F_OFFSET":None,
	"F_URL":None,
	"F_TITLE":None,
	"F_DESC":None,
	"F_BACK_KEYWORD":None
}

f = open(r'G:\watt\python\log_ana\20150707.csv','r+')
def split_line(file):
	'''
		将文件划分为行列表
		每行转化为一个字典，并返回；注意：字典是无序的。
		将多个单行字典，转化为一个大字典，（后期可以考虑返回一个迭代器)
		字典的追加赋值要用Ｋ＝Ｖ的格式，而不是Ｄ＝{K:v}重新定义字典
	'''
	p = 0
	content_he = {}
	while True:
		j = 0
		line = file.readline()
		if not line: break
		#line = line.strip('^"')
		#line = line.strip('"')
		#unit = line.split('","')
		pat = r'"(.*?)"'
		unit = re.findall(pat,line)
		content_he[p] = {}
		for k in keys:#如果将keys换成content，生成的字典键值将是混乱的，因为字典无序
			#content[k] = unit[j]
			content.update({k:unit[j]})#这里必须用update
			#content = dict([(k,unit[j])])
			#print "%s is %s" % (keys[j], content[k])
			#content_he[p] = dict([(k,unit[j])])
			j += 1
		content_he[p].update(content)
		p += 1
	return content_he
	f.close()

content_he = split_line(f)
print 'line:80 print content_he is ' + str(len(content_he))
#print "*************"
#print content_he


def save_file(dict_name):
	'''
		将字典存盘为指定格式
	'''
	i = 0
	f_out = open(r'G:\watt\python\log_ana\f_out.txt', 'a+')
	for k, v in dict_name.iteritems():
		f_out.write(str(k) + '   is   ' + str(v) + ',        ')#逗号分隔，也可以一行一个
		f_out.write('\n')
	f_out.close()
save_file = save_file(content_he)
print "\n"


def same_sid_click(dict_name):#传入的字典结构：dict_name{int:{"key":"value"}}
	'''
		1,查找字典中SID相同的项，并打印出这个SID，结果项被点击总次数，及每一次点击时间和ＵＲＬ
		2,在将点击时间与ＵＲＬ匹配时，使用SET处理了相同SID下的ＵＲＬ的重复和时间排序两个问题
	'''
	sid = []
	dict_name_2 = copy.deepcopy(dict_name)#为了查找相同ＳＩＤ的项，深复制了传入的字典
	for k in dict_name:
		'''
			在这里定义列表，可在每次外层循环时重置列表，这与打印相应内容的时间节点相关，及时清空，避免重复打印，如果是返回值就又不同了
		'''
		order_time = []
		urls = []
		urls_1 = []
		urls_2 = []
		if dict_name[k]["SESSION_ID"] not in sid:#用in来避免重复
			sid.append(dict_name[k]["SESSION_ID"])#更新SID
			for k1 in dict_name_2:
				'''
					保障时间ＵＲＬ对应关系，所以联合F_TIME F_URL判断
					必须以时间ＵＲＬ对的形式来去重
				'''
				if dict_name[k]["SESSION_ID"] == dict_name_2[k1]["SESSION_ID"] and str([dict_name[k]["SESSION_ID"], dict_name_2[k1]["F_TIME"],dict_name_2[k1]["F_URL"]]) not in urls:
					urls.append(str([dict_name[k]["SESSION_ID"], dict_name_2[k1]["F_TIME"], dict_name_2[k1]["F_URL"]]))#更新url
					'''
						使用urls_1系列在输出F_BACK_KEYWORD时会乱码
						#urls_1.append(str([dict_name_2[k1]["F_TIME"], dict_name_2[k1]["F_URL"], dict_name_2[k1]["F_BACK_KEYWORD"]]))
					
						#if not dict_name_2[k1]["F_TIME"]:
							#dict_name_2[k1]["F_TIME"] = None
					'''
					if not dict_name_2[k1]["F_URL"]:
						dict_name_2[k1]["F_URL"] = None
					if not dict_name_2[k1]["F_BACK_KEYWORD"]:
						dict_name_2[k1]["F_BACK_KEYWORD"] = None
					urls_2.append(dict_name[k]["SESSION_ID"])
					urls_2.append(dict_name_2[k1]["F_TIME"])
					urls_2.append(dict_name_2[k1]["F_URL"])
					urls_2.append(dict_name_2[k1]["F_BACK_KEYWORD"])
					
					order_time.append(dict_name_2[k1]["F_TIME"])
					s_time = set(order_time)

			'''
					到此，已将dict_name{int:{"key":"value"}}中的"key"和"{"key":"value"}"转成了两个按SID归总的set
					s 里面存储了去重后的符合条件的整数型的时间
					s_time 里面存储了去重后的符合条件的字符型的“时间——ＵＲＬ对”
					下面的思路是将s转化为列表Ａ并重新排序，再按Ａ的顺序去s_1里面找ＵＲＬ（需要先将s_1l分割成列表)
					打印结果
			'''

			#print '%s, 来自  市 %s 的用户 %s 共点击了 %s 次搜索结果，分别如下:' % (dict_name[k]["F_DATE"],dict_name[k]["F_CITY"],dict_name[k]["F_MOBILE"],len(urls))
			each_url = []
			'''以url_２替换
			for url in urls_1:#分割源列表每项为一个新列表
				#pat = r"'([0-9]{6})', '(.*?)'"#正则的基本功不够，加强
				pat = r"'(.*?)'[,]?"# url的格式['032819', 'service.js.10086.cn/bcma.jsp#DSYX_BL@id=1463']
				each_url.append(re.findall(pat, url))
			'''
			F_BACK_KEYWORD = []
			F_URL = []
			F_DATE = []
			SESSION_ID = []

			for url in urls_2:#分割源列表每项为一个新列表
				if (urls_2.index(url) + 1) % 4 == 0: 
					F_BACK_KEYWORD.append(url)
				elif (urls_2.index(url) + 1) % 4 == 1:
					SESSION_ID.append(url)
				elif (urls_2.index(url) + 1) % 4 == 2:
					F_DATE.append(url)
				else:
					F_URL.append(url)

			order_time = list(s_time)#用集合的目的在于去重，目标已达成，恢复列表身份，排序后从小到大顺序输出结果
			order_time.sort()
			
			print dict_name[k]["SESSION_ID"]
			if dict_name[k]["F_CITY"] and dict_name[k]["F_MOBILE"]:
				print '%s, 来自 ***%s市*** 的用户 ***%s*** 共点击了搜索结果 %s 次，分别如下:' % (dict_name[k]["F_DATE"], dict_name[k]["F_CITY"], dict_name[k]["F_MOBILE"], len(urls))
			else:
				print '%s, 来自 ***未知城市*** 的 ***无号码用户*** 点击了 %s 次搜索结果，分别如下:' % (dict_name[k]["F_DATE"], len(urls))
			out_test = []
			for h_m_s in order_time:
				for dt in F_DATE:#此处的双循环带来了重复输出，需处理
					if h_m_s == dt and str([F_URL[order_time.index(h_m_s)], dt]) not in out_test :
						out_test.append(str([F_URL[order_time.index(h_m_s)], dt]))
						print '     在北京时间%s，搜索了***  %s   *** ,点击了 %s' % (dt, F_BACK_KEYWORD[order_time.index(h_m_s)], F_URL[order_time.index(h_m_s)])





					'''
						if (each_url.index(e) + 1) % 2 == 0:
							F_URL = e 
						else:
							F_DATE = e 
						#if str(F_DATE[each_url.index(e)%2] + F_URL[each_url.index(e)%2]) in out_test and h_m_s == F_DATE[each_url.index(e)%2]:
							#out_test.append(str(F_DATE[each_url.index(e)] + F_URL[each_url.indx(e)]))
							#print '     在北京时间%s，搜索了***  %s   *** ,点击了 %s' % (F_DATE[each_url.index(e)%2], F_BACK_KEYWORD, F_URL[each_url.index(e)%2])
					'''


					'''
					if len(e) >=3 and str([e[0], e[1]]) not in out_test and h_m_s == e[0] :
						print isinstance(e[2], unicode)
						print sys.getdefaultencoding() 
						out_test.append(str([e[0], e[1]]))
						print '     在北京时间%s，搜索了***  %s   *** ,点击了 %s' % (e[0], e[1], e[1])
					'''
			print "-----------------------------------------------------------------------\n"


same_sid_click(content_he)

end_time = datetime.datetime.now()
print "本次处理开始于%s，结束于%s" % (start_time, end_time)
