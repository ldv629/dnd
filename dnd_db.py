#!/usr/bin/env python3

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
        Column('str_mod', Integer),
        Column('dex', Integer),
        Column('dex_mod', Integer),
        Column('con', Integer),
        Column('con_mod', Integer),
        Column('int', Integer),
        Column('int_mod', Integer),
        Column('wis', Integer),
        Column('wis_mod', Integer),
        Column('cha', Integer),
        Column('cha_mod', Integer),
        Column('app', Integer),
        Column('app_mod', Integer),
        Column('char_id', Integer, ForeignKey('characters.char_id'), nullable=False))

    saves_ac = Table('saves_ac', metadata,
        Column('saves_id', Integer, primary_key=True),
        Column('ac', Integer),
        Column('ref', Integer),
        Column('ref_base', Integer),
        Column('fort', Integer),
        Column('fort_base', Integer),
        Column('will', Integer),
        Column('will_base', Integer),
        Column('init', Integer),
        Column('init_base', Integer),
        Column('bab', Integer),
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
