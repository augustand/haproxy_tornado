# # -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement
import datetime
from mongoengine import connect, Document, StringField, DateTimeField, ReferenceField
from settings import MONGODB_SETTINGS

connect(MONGODB_SETTINGS["DB"])
class User(Document):
    name = StringField(max_length=50, required=True)
    password = StringField(max_length=50, required=True)
    email = StringField(max_length=50)
    created_at = DateTimeField(default=datetime.datetime.now, required=True)
