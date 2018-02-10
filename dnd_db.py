#!/usr/bin/env python3

from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine('sqlite:///stats.db')
db_name = 'default_dnd'
engine = create_engine('sqlite:///' + db_name + '.db')
metadata = MetaData()
Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50), nullable=False)
    level = Column(Integer, nullable=False)
    race = Column(String(50), nullable=False)
    total_hp = Column(Integer, nullable=False)
    subdual_damage = Column(Integer, nullable=False)
    damage_taken = Column(Integer, nullable=False) 

    def __repr__(self):
        return "<Characters(name='%s', level='%s', race='%s', hp='%s')>" % (self.name, self.level, self.race, self.total_hp)

class Abilities(Base):
    __tablename__ = 'abilities'

    id = Column(Integer, primary_key=True)
    strength = Column(Integer)
    dexterity = Column(Integer)
    constitution = Column(Integer)
    intelligence = Column(Integer)
    wisdom = Column(Integer)
    charisma = Column(Integer)
    appearance = Column(Integer)
    char_id = Column(Integer, ForeignKey('characters.id'))

    def __repr__(self):
        return "Abilities:\n\tSTR = %s\n\tDEX = %s\n\tCON = %s\n\tINT = %s\n\tWIS = %s\n\tCHA = %s" % (self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma)

class Saves_ac(Base):
    __tablename__ = 'saves_ac'

    id = Column(Integer, primary_key=True)
    ac = Column(Integer)
    ref = Column(Integer)
    ref_base = Column(Integer)
    fort = Column(Integer)
    fort_base = Column(Integer)
    will = Column(Integer)
    will_base = Column(Integer)
    init = Column(Integer)
    init_base = Column(Integer)
    bab = Column(Integer)
    char_id = Column(Integer, ForeignKey('characters.id'))

class Weapons(Base):
    __tablename__ = 'weapons'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    damage = Column(String(50), nullable=False)
    threat = Column(Integer, nullable=False)
    range = Column(Integer, nullable=False)
    char_id = Column(Integer, ForeignKey('characters.id'))

class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    item_name = Column(String(50), nullable=False)
    weight = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    carry_weight = Column(Integer, nullable=False)
    char_id = Column(Integer, ForeignKey('characters.id'))

class Skills(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    rank = Column(Integer, nullable=False)
    synergy = Column(Integer, nullable=False)
    misc = Column(Integer, nullable=False)
    char_id = Column(Integer, ForeignKey('characters.id'))

class Languages(Base):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    char_id = Column(Integer, ForeignKey('characters.id'))

class Feats(Base):
    __tablename__ = 'feats'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    char_id = Column(Integer, ForeignKey('characters.id'))

