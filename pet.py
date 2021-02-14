from db_manager import Pet

import random

def generate_pet(user_id):
    new_name = generate_name()
    pet = Pet(owner_id=user_id, name=new_name, iv=generate_iv(), level=1, exp=0)
    pet.save()
    return new_name


def generate_name():
    r = RandomWords()
    return r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun, adj", minCorpusCount=10)


def generate_iv():
    return random.randint(1,10)
