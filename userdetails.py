from peewee import *

if os.environ.get('DATABASE_URL'):
    db = connect(os.environ.get('DATABASE_URL'))
else:
    db = SqliteDatabase('registers.db')


class Register(Model):
    user_id = IntegerField()
    name = TextField()
    balance = IntegerField()

    class Meta:
        database = db


def add_register(user_id, name, balance):
    user = Register(user_id=user_id, name=name, balance=balance)
    user.save()


def get_register(user_id):
    return Register.get(Register.user_id == user_id)


def add_philcoin(user_id, name, amount):
    try:
        user = get_register(user_id)
        user.balance += amount
        user.save()
    except Register.DoesNotExist:
        add_register(user_id, name, amount)


def get_philcoin_balance(user_id, name):
    try:
        return get_register(user_id).balance
    except Register.DoesNotExist:
        add_register(user_id, name, 0)
        return 0
