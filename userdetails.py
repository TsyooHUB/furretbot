from db_manager import Register


def add_register(user_id, name, balance):
    user = Register(user_id=str(user_id), name=name, balance=balance)
    user.save()


def get_register(user_id):
    return Register.get(Register.user_id == str(user_id))


def add_philcoin(user_id, name, amount):
    try:
        user = get_register(user_id)
        user.balance += int(amount)
        user.save()
    except Register.DoesNotExist:
        add_register(user_id, name, amount)


def get_philcoin_balance(user_id, name):
    try:
        return get_register(user_id).balance
    except Register.DoesNotExist:
        add_register(user_id, name, 0)
        return 0
