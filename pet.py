from datetime import date
from db_manager import Pet
from random_word import RandomWords
from random import randint

import time


def generate_pet(user_id):
    new_name = generate_name()
    if new_name == None: 
        return 
    pet = Pet(owner_id=user_id, name=new_name, iv=generate_iv(), level=1, exp=0, lastPickup=date(2021, 1, 1))
    pet.save()
    return new_name


def generate_name():
    r = RandomWords()
    return r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun, adj", minCorpusCount=10)


def generate_iv():
    return randint(1, 10)


def get_pets(user_id):
    pet_list = "Your pets:\n"
    query = Pet.select().where(Pet.owner_id == str(user_id))
    for pet in query:
        pet_list += f"[{pet.name} phil - Level: {pet.level}, Exp: {pet.exp}]\n"
    return pet_list
    

def get_pickup(name):
    try:
        pet = Pet.get(Pet.name == name)
        if pet.lastPickup.day < date.today().day:
            pet.lastPickup = date.today()
            pet.save()
            return compute_pickup(pet.iv, pet.level)
        else:
            return False
    except:
        return False

def compute_pickup(iv, level):
    return int(round((randint(1, 10) + iv) * (1 + 0.1*(level-1)), 0))