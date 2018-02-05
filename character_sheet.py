#!/usr/bin/env python3

#TODO: add support to do things 3.5 and 5 going to start with 3.5
import dice
from sqlalchemy import *
#import dnd_db
db_connection = None

def init(db_name):
    engine = create_engine('sqlite:///' + db_name + '.db')
    db_connection = engine.connect()

def create_character(name,level,race,total_hp,subdual_hp,effective_hp):
    pass

def delete_character(user_id):
    pass

def take_damage(damage, user_id):
    pass

def take_subdual_damage(damage, user_id):
    pass

def receive_healing(damage, user_id):
    pass

def receive_subdual_healing(damage, user_id):
    pass

def set_hp(user_id):
    pass

def get_hp(user_id):
    pass

def set_current_hp(user_id):
    pass

def get_current_hp(user_id):
    pass

def set_subdual_hp(user_id):
    pass

def get_subdual_hp(user_id):
    pass

def add_feat(user_id):
    pass

def remove_feat(user_id):
    pass

def add_language(user_id):
    pass

def get_languages(user_id):
    pass

def remove_language(user_id):
    pass

def set_skill(skill, user_id):
    pass

def get_skill(skill, user_id):
    pass

def set_init(user_id):
    pass

def get_init(user_id):
    pass

def set_stat(stat,value, user_id):
    if stat is 'str':
        pass
    elif stat is 'dex':
        pass
    elif stat is 'con':
        pass
    elif stat is 'int':
        pass
    elif stat is 'wis':
        pass
    elif stat is 'cha':
        pass
    elif stat is 'app':
        pass

def get_stat(stat, user_id):
    if stat is 'str':
        pass
    elif stat is 'dex':
        pass
    elif stat is 'con':
        pass
    elif stat is 'int':
        pass
    elif stat is 'wis':
        pass
    elif stat is 'cha':
        pass
    elif stat is 'app':
        pass

