from datetime import date
from db_manager import Pet
from random_word import RandomWords
from random import randint

import time

CURRENT_PET_PRICE = 100
MAX_PETS = 10


def generate_pet(user_id):
    new_name = generate_name()
    if new_name == None:
        return
    pet = Pet(
        owner_id=user_id,
        name=new_name,
        iv=generate_iv(),
        level=1,
        exp=0,
        lastPickup=date(2021, 1, 1),
    )
    pet.save()
    return new_name


def create_pet(user_id, pet_name):
    pet = Pet(
        owner_id=user_id,
        name=pet_name,
        iv=generate_iv(),
        level=1,
        exp=0,
        lastPickup=date(2021, 1, 1),
    )
    pet.save()


def generate_name():
    r = RandomWords()
    return r.get_random_word(
        hasDictionaryDef="true", includePartOfSpeech="noun, adj", minCorpusCount=10
    )


def generate_iv():
    return randint(1, 10)


def get_num_pets(user_id):
    return len(Pet.select().where(Pet.owner_id == str(user_id)))


def get_pets(user_id):
    pet_list = "Your pets:\n"
    query = Pet.select().where(Pet.owner_id == str(user_id))
    for pet in query:
        pet_list += f"[{pet.name} phil - Level: {pet.level}, Exp: {pet.exp}]\n"
    return pet_list


def get_pet(name):
    return Pet.get(Pet.name == name)


def get_pickup(pet):
    print(pet.lastPickup)
    print(date.today())
    if pet.lastPickup.day < date.today().day:
        pet.lastPickup = date.today()
        pet.save()
        return compute_pickup(pet.iv, pet.level)
    else:
        return False


def compute_pickup(iv, level):
    return int(round((randint(1, 10) + iv) * (1 + 0.1 * (level - 1)), 0))


def fuse_pets(pet1, pet2):
    total_exp = sigma(pet2.level) + pet2.exp
    while total_exp > 0:
        exp_to_level = pet1.level - pet1.exp
        if total_exp >= exp_to_level:
            total_exp -= exp_to_level
            pet1.exp += exp_to_level
        else:
            pet1.exp += total_exp
            total_exp = 0
        if pet1.exp == pet1.level:
            pet1.level += 1
            pet1.exp = 0
    pet1.save()
    pet2.delete_instance()


def sigma(n):
    sum = 1
    for i in range(n):
        sum += i
    return sum


def delete_pet(pet):
    pet.delete_instance()