# # -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement
from tornado.options import define, options
import tornado.web
from handlers.home import HomeHandler
from handlers.user import UserHandler
from handlers.admin import AdminHandler
import tornado.httpserver
import tornado.ioloop
import settings
define("port", default=8881, help="run on the given port", type=int)
define("debug", default=True, type=bool)

class Application(tornado.web.Application):
    def __init__(self):

        handlers = [
            tornado.web.URLSpec(r"/", HomeHandler, name="home"),
            tornado.web.URLSpec(r"/user", UserHandler, name="user"),
            tornado.web.URLSpec(r"/user/(.*)", UserHandler, name="user1"),
            tornado.web.URLSpec(r"/admin", AdminHandler, name="admin")
        ]

        tornado.web.Application.__init__(self, handlers, **dict(
            debug=options.debug,
            static_path=settings.STATIC_PATH,
            template_path=settings.TEMPLATE_PATH,
            xsrf_cookies=True,
            cookie_secret="!e@hal9f3z2cg!@!f5uu9^-=e3gc$&azo!avfj9s+-g1fk)+y3",
        ))


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
