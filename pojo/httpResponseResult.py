#-*- coding:utf8 -*-
# 作者 tailai01
# 创建时间 2018/01/19 22:36
# github https://github.com/tailai01
class HttpResponseResult:
    def __init__(self):
        self.status_code=None
        self.body=None
        self.cookies=None
        self.headers=None