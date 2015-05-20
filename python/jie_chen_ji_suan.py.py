#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Filename: wei_di_gui.py
#Date: - - 
#Content:阶乘计算的尾递归算法测试。结论是：python不支持尾递归,当数字到1000时就会出错
'''
本脚本重点在于对中文录入的研究，print打印格式的试验，尾递归的尝试。
字符串解码与重编码方法 .decode('utf-8').encode('gbk')
unicode字符串使用"u.'我是中国人'"
'''
import cmath

name = raw_input('你是谁？'.decode('utf-8').encode('gbk'))
print 'Hello %s, 让我们一起做几个关于数字的游戏吧！'.decode('utf-8').encode('gbk')% name

print u'以下是对数X的阶乘计算，采用了尾递归算法，但是数据大于999时，会报错，内存溢出，下面我们一起试一下吧。'
n = int(raw_input('请输入一个数字，最好小于999:...\n'.decode('utf-8').encode('gbk')))

def wei_di_gui(n,a=1):
	if n == 1:
		return a
	else:
		return wei_di_gui(n-1, a*n)


print u'\
您所输入的数字是：%d\n\
它的阶乘是：%s\n\
它的平方根是：%s\n\
2的%d 次方除以7的余数是：%d，\n\
2的%d 次方等于：%d\n' % (n, wei_di_gui(n), str(cmath.sqrt(n)), n, pow(2,n,7), n, pow(2,n))


raw_input('以下将打印help函数的内容，请留意查看，请按回车键开始...'.decode('utf-8').encode('gbk'))
help()
raw_input('\n当您再次按下回车键，程序将结束...\n'.decode('utf-8').encode('gbk'))
print 'GOODBYE!'