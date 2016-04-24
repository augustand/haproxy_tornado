# # -*- coding: utf-8 -*-
import tornado.web
from handlers import BaseHandler


class AdminHandler(BaseHandler):

    def get(self):
        self.write("Hello AdminHandler")