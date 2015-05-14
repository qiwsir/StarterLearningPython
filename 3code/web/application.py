#!/usr/bin/env python
# coding=utf-8

from url import url

import tornado.web
import os

setting = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "statics")
    )

application = tornado.web.Application(
    handlers = url,
    **setting
    )
