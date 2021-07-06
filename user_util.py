from db_manager import User


def add_user(user_id, name, balance):
    user = User(user_id=str(user_id), name=name, balance=balance)
    user.save()


def get_user(user_id):
    return User.get(User.user_id == str(user_id))


def add_philcoin(user_id, name, amount):
    try:
        user = get_user(user_id)
        user.balance += int(amount)
        user.save()
    except User.DoesNotExist:
        add_user(user_id, name, amount)


def get_philcoin_balance(user_id, name):
    try:
        return get_user(user_id).balance
    except User.DoesNotExist:
        add_user(user_id, name, 0)
        return 0
