__author__ = 'willowcheng'

from peewee import *
import datetime

DATABASE = SqliteDatabase('social.db')

class User(Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at')
