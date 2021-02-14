from peewee import *
from playhouse.db_url import connect

import os


if os.environ.get('DATABASE_URL'):
    db = connect(os.environ.get('DATABASE_URL'))
else:
    db = SqliteDatabase('registers.db')
    db.connect()
    db.create_tables(['Register'])


class Register(Model):
    user_id = TextField()
    name = TextField()
    balance = IntegerField()

    class Meta:
        database = db


class Pet(Model):
    owner_id = TextField()
    name = TextField()
    iv = IntegerField()
    level = IntegerField()
    exp = IntegerField()
    lastPickup = DateField()

    class Meta:
        database = db
