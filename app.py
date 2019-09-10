# -*- coding: utf-8 -*- 
# @Time : 2019/9/10 14:25 
# @Author : 赵金林
# @Site :  
# @File : app.py

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    return '<h1>Hello Totoro! </h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
    return 'User:%s' % name


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='zhaojinlin'))
    print(url_for('user_page', name='greyli'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'
