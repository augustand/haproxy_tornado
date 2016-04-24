# # -*- coding: utf-8 -*-
import os

MONGODB_SETTINGS = dict({
    "DB": "test",
    "HOST": "localhost",
    "PORT": 27017,
    'ALIAS': 'default',
})

BASE_DIR = os.path.dirname(__file__)
STATIC_PATH = os.path.join(BASE_DIR, "static")
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
XSRF_COOKIES = True
COOKIES_SECRET = "!e@hal9f3z2cg!@!f5uu9^-=e3gc$&azo!avfj9s+-g1fk)+y3"
