import json

philbank = {}


class Register:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def set_name(self, name):
        self.name = name

    def set_balance(self, balance):
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"User: {self.get_name()}, Balance: {self.get_balance()}"


def register_exists(user_id):
    if str(user_id) in philbank:
        return True
    else:
        return False


def add_register(user_id, register):
    philbank[str(user_id)] = register


def get_register(user_id):
    return philbank[str(user_id)]


def get_philbank():
    philbank_arr = []
    for register in philbank:
        philbank_arr.append(register)
    return philbank_arr


def add_philcoin(user_id, amount):
    if register_exists(user_id):
        philbank[str(user_id)].set_balance(philbank[str(user_id)].get_balance()+amount)
        save_philbank()
        return True
    else:
        return False


def get_philcoin_balance(user_id):
    if register_exists(user_id):
        return int(philbank[str(user_id)].get_balance())
    else:
        return None


def save_philbank():
    with open('data/philbank.json', 'w') as f:
        json.dump(philbank, f, default=lambda x: x.__dict__)


def start_bank():
    global philbank
    loaded_philbank = json.load(open("data/philbank.json"))
    for user in loaded_philbank:
        philbank[user] = Register(loaded_philbank[user].get("name"), loaded_philbank[user].get("balance"))
    return "PhilBank opened successfully"
