#!/usr/bin/env python3

#TODO: add support to do things 3.5 and 5 going to start with 3.5
import dice
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import dnd_db

#db_name = 'default_db'
session = None

def init_database(db_name):
    engine = create_engine('sqlite:///' + db_name + '.db')
    dnd_db.Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
    

def create_character(name, level, race, total_hp):#,subdual_hp,effective_hp):
    #TODO: check bounds of level and total_hp
    #TODO: add class to database
    character = dnd_db.Characters(name=name, level=level, race=race, total_hp=total_hp, subdual_damage=0, damage_taken=0)
    session.add(character)
    session.commit()

def full_sheet(user_id):
    character = session.query(dnd_db.Characters).filter_by(id=user_id).one()
    abilities = session.query(dnd_db.Abilities).filter_by(char_id=user_id).one()
    #feats = session.query(dnd_db.Feats).filter_by(char_id=user_id).all()
    #languages = session.query(dnd_db.Languages).filter_by(char_id=user_id).all()

    current_hp = get_current_hp(user_id)

    print('%s\nlvl=%s\n%s CLASS\nHP=%s/%s' % (character.name,character.level, character.race, current_hp, character.total_hp))
    print(abilities)

def get_characters():
    characters = session.query(dnd_db.Characters).all()

    for char in characters:
        print(char)

    return characters

def delete_character(user_id):
    try:
        character = session.query(dnd_db.Characters).filter_by(id = user_id).one()
        session.delete(character)
    except NoResultFound:
        pass

def take_damage(damage, user_id):
    try:
        character = session.query(dnd_db.Characters).filter_by(id = user_id).one()
        character.damage_taken += damage
        session.commit()
        return character.total_hp - character.subdual_damage - character.damage_taken
    except NoResultFound:
        pass

def take_subdual_damage(damage, user_id):
    try:
        character = session.query(dnd_db.Characters).filter_by(id = user_id).one()
        character.subdual_damage += damage
        session.commit()
        return character.total_hp - character.subdual_damage - character.damage_taken
    except NoResultFound:
        pass

def receive_healing(healing, user_id):
    try:
        character = session.query(dnd_db.Characters).filter_by(id = user_id).one()
        character.damage_taken -= healing if healing < character.damage_taken else character.damage_taken
        session.commit()
    except NoResultFound:
        pass

def receive_subdual_healing(healing, user_id):
    try:
        character = session.query(dnd_db.Characters).filter_by(id = user_id).one()
        if character.subdual_damage <= healing:
            diff = healing - character.subdual_damage
            character.subdual_damage = 0
            return diff
        else:
            character.subdual_damage -= healing 
            return 0
        session.commit()
    except NoResultFound:
        pass

def set_hp(hp, user_id):
    try:
        character = session.query(dnd_db.Characters).filter_by(id = user_id).one()
        if hp < 1:
            raise ValueError
        character.total_hp = hp
        session.commit()
    except NoResultFound:
        pass
    except ValueError:
        pass #negative value

def get_total_hp(user_id):
    try:
        character = session.query(dnd_db.Characters).filter_by(id = user_id).one()
        return character.total_hp
    except NoResultFound:
        pass

def set_current_hp(user_id):
    pass #probably won't use this function

def get_current_hp(user_id):
    try:
        character = session.query(dnd_db.Characters).filter_by(id = user_id).one()
        return character.total_hp - character.subdual_damage - character.damage_taken
    except NoResultFound:
        pass

def get_subdual_hp(user_id):
    try:
        character = session.query(dnd_db.Characters).filter_by(id = user_id).one()
        return character.total_hp - character.subdual_damage
    except NoResultFound:
        pass

def add_feat(feat, user_id):
    try:
        name = session.query(dnd_db.Feats).filter_by(char_id = user_id).one()
    except NoResultFound:
        name = dnd_db.Feats()
        name.char_id = user_id

    name.name = feat

    session.add(name)
    session.commit()

def get_feats(user_id):
    try:
        return session.query(dnd_db.Feats).filter_by(char_id = user_id).all()
    except NoResultFound:
        return 'error none found'

def delete_feat(feat, user_id):
    try:
        name = session.query(dnd_db.Characters).filter_by(char_id = user_id).all()
        session.delete(name)
    except NoResultFound:
        pass

def add_language(language, user_id):
    try:
        name = session.query(dnd_db.Languages).filter_by(char_id = user_id).one()
    except NoResultFound:
        name = dnd_db.Languages()
        name.char_id = user_id

    name.name = language

    session.add(name)
    session.commit()

def get_languages(user_id):
    try:
        return session.query(dnd_db.Languages).filter_by(char_id = user_id).all()
    except NoResultFound:
        return 'error none found'

def remove_language(language, user_id):
    try:
        language = session.query(dnd_db.Languages).filter_by(char_id = user_id).one()
    except NoResultFound:
        return 'error none found'

    session.delete(language)

def set_skill(skill, user_id):
    pass

def get_skill(skill, user_id):
    pass

def set_init(init, user_id):
    pass

def get_init(init, user_id):
    pass

def set_abilities(abilities, user_id):
    try:
        set_stat('str',abilities[0],user_id)
        set_stat('dex',abilities[1],user_id)
        set_stat('con',abilities[2],user_id)
        set_stat('int',abilities[3],user_id)
        set_stat('wis',abilities[4],user_id)
        set_stat('cha',abilities[5],user_id)
    except IndexError:
        print("array too small")

def set_stat(stat, value, user_id):
    try:
        ability = session.query(dnd_db.Abilities).filter_by(char_id = user_id).one()
    except NoResultFound:
        ability = dnd_db.Abilities()
        ability.char_id = user_id
        #TODO: add checks to make sure that user_id exists


    if stat is 'str':
        ability.strength = value
    elif stat is 'dex':
        ability.dexterity = value
    elif stat is 'con':
        ability.constitution = value
    elif stat is 'int':
        ability.intelligence = value
    elif stat is 'wis':
        ability.wisdom = value
    elif stat is 'cha':
        ability.charisma = value
    """
    elif stat is 'app':
        ability = session.query(dnd_db.Abilities).filter_by(char_id = user_id).one()
        ability.appearance = value
    """

    session.add(ability)
    session.commit()

def get_stat(stat, user_id):
    ability = session.query(dnd_db.Abilities).filter_by(char_id = user_id).one()
    if stat is 'str':
        return ability.strength
    elif stat is 'dex':
        return ability.dexterity
    elif stat is 'con':
        return ability.constitution
    elif stat is 'int':
        return ability.intelligence
    elif stat is 'wis':
        return ability.wisdom
    elif stat is 'cha':
        return ability.charisma
    elif stat is 'app':
        pass

