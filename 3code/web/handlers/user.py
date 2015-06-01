#!/usr/bin/env python
# coding=utf-8

import tornado.web
import tornado.escape
import methods.readdb as mrd
from base import BaseHandler

class UserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        #username = self.get_argument("user")
        username = tornado.escape.json_decode(self.current_user)
        print username
        print type(username)
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        print user_infos
        self.render("user.html", users = user_infos)
