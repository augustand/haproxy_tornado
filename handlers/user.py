# # -*- coding: utf-8 -*-
import tornado.web
from handlers import BaseHandler


class UserHandler(BaseHandler):
    def get(self, user=None):
        if not self.current_user:
            self.redirect("/")
            return
        self.write("Hello UserHandler %s"%user)

    def post(self):
        self.set_secure_cookie("user", self.get_argument("username"))
        self.redirect(self.reverse_url("user1", self.get_argument("username")))