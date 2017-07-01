#!/usr/bin/env python3

import dice
from sqlalchemy import *

def create_db():
    engine = create_engine('sqlite:///stats.db')
    metadata = MetaData()

    characters = Table('characters', metadata,
        Column('char_id', Integer, primary_key=True),
        Column('char_name', String(50), nullable=False),
        Column('char_level', Integer, nullable=False),
        Column('char_race', String(50), nullable=False),
        Column('char_total_hp', Integer, nullable=False),
        Column('char_subdual_hp', Integer, nullable=False),
        Column('char_effective_hp', Integer, nullable=False))

    ability_scores = Table('ability_scores', metadata,
        Column('stat_id', Integer, primary_key=True),
        Column('str', Integer),
        Column('dex', Integer),
        Column('con', Integer),
        Column('int', Integer),
        Column('wis', Integer),
        Column('cha', Integer),
        Column('app', Integer),
        Column('char_id', Integer, ForeignKey('characters.char_id'), nullable=False))

    saves_ac = Table('saves_ac', metadata,
        Column('saves_id', Integer, primary_key=True),
        Column('ac', Integer),
        Column('ref', Integer),
        Column('fort', Integer),
        Column('will', Integer),
        Column('init', Integer),
        Column('bab', Integer),
        #add in base
        Column('char_id', Integer, ForeignKey('characters.char_id'), nullable=False))

    weapons = Table('weapons', metadata,
        Column('weapon_id', Integer, primary_key=True),
        Column('weapon_name', String(50), nullable=False),
        Column('weapon_damage', String(50), nullable=False),
        Column('weapon_threat', Integer, nullable=False),
        Column('weapon_range', Integer, nullable=False),
        Column('char_id', Integer, ForeignKey('characters.char_id'), nullable=False))

    inventory = Table('inventory', metadata,
        Column('inventory_id', Integer, primary_key=True),
        Column('inventory_name', String(50), nullable=False),
        Column('weight', String(50), nullable=False),
        Column('quantity', Integer, nullable=False),
        Column('carry_weight', Integer, nullable=False),
        Column('char_id', Integer, ForeignKey('characters.char_id'), nullable=False))

    skills = Table('skills', metadata,
        Column('skill_id', Integer, primary_key=True),
        Column('skill_name', String(50), nullable=False),
        Column('skill_rank', Integer, nullable=False),
        Column('skill_synergy', Integer, nullable=False),
        Column('skill_misc', Integer, nullable=False),
        Column('char_id', Integer, ForeignKey('characters.char_id'), nullable=False))

    languages = Table('languages', metadata,
        Column('language_id', Integer, primary_key=True),
        Column('language_name', String(50), nullable=False),
        Column('char_id', Integer, ForeignKey('characters.char_id'), nullable=False))

    feats = Table('feats', metadata,
        Column('feat_id', Integer, primary_key=True),
        Column('feat_name', String(50), nullable=False),
        Column('char_id', Integer, ForeignKey('characters.char_id'), nullable=False))
    
    characters.create(engine, checkfirst=True)
    ability_scores.create(engine, checkfirst=True)
    saves_ac.create(engine, checkfirst=True)
    weapons.create(engine, checkfirst=True)
    inventory.create(engine, checkfirst=True)
    languages.create(engine, checkfirst=True)
    feats.create(engine, checkfirst=True)
    
def take_damage(user_id,damage):
    pass

def take_subdual_damage(user_id,damage):
    pass

def receive_healing(user_id,damage):
    pass

def roll_skill(user_id,skill):
    pass
    return dice.roll(1,20) # + skill

def add_feat(user_id):
    pass

def remove_feat(user_id):
    pass

def add_language(user_id):
    pass

def remove_language(user_id):
    pass

def roll_save(user_id,save):
    if save is 'ref':
        pass
        return dice.roll(1,20) # + ref
    elif save is 'fort':
        pass
        return dice.roll(1,20) # + fort
    elif save is 'will':
        pass
        return dice.roll(1,20) # + will

def roll_init(user_id):
    pass
    return dice.roll(1,20) # + init

def set_stat(stat,value):
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
