from db_manager import User


def add_user(user_id, name, balance):
    user = User(user_id=str(user_id), name=name)
    user.save()


def get_user(user_id):
    return User.get(User.user_id == str(user_id))
