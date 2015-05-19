#!/usr/bin/env python
#coding=gbk
#coding=utf-8
#-*- coding: UTF-8 -*- 

#������
import web
#�������ݿ����model���Ժ󴴽���
import model
#URLӳ��
urls = (
        '/', 'Index',
        '/view/(/d+)', 'View',
        '/new', 'New',
        '/delete/(/d+)', 'Delete',
        '/edit/(/d+)', 'Edit',
        '/login', 'Login',
        '/logout', 'Logout',
        )
app = web.application(urls, globals())
#ģ�幫������
t_globals = {
    'datestr': web.datestr,
    'cookie': web.cookies,
}
#ָ��ģ��Ŀ¼�����趨����ģ��
render = web.template.render('templates', base='base', globals=t_globals)
#������¼����
login = web.form.Form(
                      web.form.Textbox('username'),
                      web.form.Password('password'),
                      web.form.Button('login')
                      )
#��ҳ��
class Index:
    def GET(self):
        login_form = login()
        posts = model.get_posts()
        return render.index(posts, login_form)
    def POST(self):
        login_form = login()
        if login_form.validates():
            if login_form.d.username == 'admin' \
                and login_form.d.password == 'admin':
                web.setcookie('username', login_form.d.username)
        raise web.seeother('/')
#�鿴������
class View:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.view(post)
#�½�������
class New:
    form = web.form.Form(
                         web.form.Textbox('title',
                         web.form.notnull,
                         size=30,
                         description='Post title: '),
                         web.form.Textarea('content',
                         web.form.notnull,
                         rows=30,
                         cols=80,
                         description='Post content: '),
                         web.form.Button('Post entry'),
                         )
    def GET(self):
        form = self.form()
        return render.new(form)
    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.title, form.d.content)
        raise web.seeother('/')
#ɾ��������
class Delete:
    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/')
#�༭������
class Edit:
    def GET(self, id):
        post = model.get_post(int(id))
        form = New.form()
        form.fill(post)
        return render.edit(post, form)
    def POST(self, id):
        form = New.form()
        post = model.get_post(int(id))
        if not form.validates():
            return render.edit(post, form)
        model.update_post(int(id), form.d.title, form.d.content)
        raise web.seeother('/')
#�˳���¼
class Logout:
    def GET(self):
        web.setcookie('username', '', expires=-1)
        raise web.seeother('/')
#����404������ʾ����
def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")
    
app.notfound = notfound
#����
if __name__ == '__main__':
    app.run()