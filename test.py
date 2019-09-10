# -*- coding: utf-8 -*- 
# @Time : 2019/9/10 16:49 
# @Author : 赵金林
# @Site :  
# @File : test.py

from app import User, Movie, db

user = User.query.first()
print(user.name)
