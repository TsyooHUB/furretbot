from peewee import SqliteDatabase, TextField, IntegerField, Model
from playhouse.db_url import connect

import os


if os.environ.get("DATABASE_URL"):
    db = connect(os.environ.get("DATABASE_URL"))
else:
    db = SqliteDatabase("registers.db")
    db.connect()
    db.create_tables(["Register"])


class User(Model):
    user_id = TextField()
    name = TextField()
    balance = IntegerField()

    class Meta:
        database = db
