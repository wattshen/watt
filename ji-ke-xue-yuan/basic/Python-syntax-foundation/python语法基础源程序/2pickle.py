#!/usr/bin/env python
#coding: utf-8
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:.py  -*-*-
#-*-*-  Date:
#Content:



#pickle����

import pickle

#dumps(object)���������л�
lista=["mingyue","jishi","you"]
listb=pickle.dumps(lista)
#print listb +'\n****'

#loads(string)������ԭ���ָ������Ҷ�������Ҳ�ָ�Ϊԭ���ĸ�ʽ
listc=pickle.loads(listb)
#print listc

#dump(object,file),������洢���ļ��������л�
group1=("bajiu","wen","qingtian")
f1=file('1.pk1','wb')
pickle.dump(group1,f1,True)
f1.close()

#load(object,file)��dump()�洢���ļ���������ݻָ�
f2=file('1.pk1','rb')
t=pickle.load(f2)
print t
f2.close()



