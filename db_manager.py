from peewee import SqliteDatabase, TextField, IntegerField, Model
from playhouse.db_url import connect

import os


if os.environ.get("DATABASE_URL"):
    db = connect(os.environ.get("DATABASE_URL"))
else:
    db = SqliteDatabase("users.db")
    db.connect()
    db.create_tables(["User"])


class User(Model):
    user_id = TextField()
    name = TextField()

    class Meta:
        database = db
