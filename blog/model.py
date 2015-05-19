#!/usr/bin/env python
#coding=gbk
#coding=utf-8
#-*- coding: UTF-8 -*- 

import web
import datetime
#���ݿ�����
db = web.database(dbn = 'mysql', db = 'test', user = 'root', pw = '123456')
#��ȡ��������
def get_posts():
    return db.select('entries', order = 'id DESC')
    
#��ȡ��������
def get_post(id):
    try:
        return db.select('entries', where = 'id=$id', vars = locals())[0]
    except IndexError:
        return None
#�½�����
def new_post(title, text):
    db.insert('entries',
        title = title,
        content = text,
        posted_on = datetime.datetime.utcnow())
#ɾ������
def del_post(id):
    db.delete('entries', where = 'id = $id', vars = locals())
    
#�޸�����
def update_post(id, title, text):
    db.update('entries',
        where = 'id = $id',
        vars = locals(),
        title = title,
        content = text)