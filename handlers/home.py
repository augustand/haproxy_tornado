# # -*- coding: utf-8 -*-
"""
Home app
"""
from __future__ import absolute_import, division, print_function, with_statement
from tornado.options import options
import tornado.web
from handlers import BaseHandler


class HomeHandler(BaseHandler):
    def get(self):
        self.render("home.html")