#!/usr/bin/env python
#coding: utf-8 
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:index.py  -*-*-
#-*-*-  Date:  
#Content:

import web

urls = (
	'/(.*)/', 'redirect',
	'/.?','index',
	'/404','h404',
	'aaa','h301'
)

class index:
    def GET(self):
        return "Hello, world!"

class redirect:
	def GET(self, path):
		web.seeother('/' + path)
class h404:
	def GET(self):
		return 'this page is not exit, please check it and try again!'
class SomePage:
	def POST(self):
		raise web.seeother('/(.*)/')
class h301():
	def POST(self):
		raise web.redirect('/(.*)/')
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()