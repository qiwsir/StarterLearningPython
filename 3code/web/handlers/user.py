#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.readdb as mrd

class UserHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("user")
        print self.get_secure_cookie(username)
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        self.render("user.html", users = user_infos)
