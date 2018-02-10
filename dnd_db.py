#!/usr/bin/env python3

from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import pdb

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
        current_hp = self.total_hp - self.subdual_damage - self.damage_taken
        return "Name=%s level=%s race=%s total_hp=%s current_hp= %s" % (self.name, self.level, self.race, self.total_hp, current_hp)

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

    def __repr__(self):
        return "AC = %s, Relfex = %s, Fortitude = %s, Will = %s, Initiative = %s, Base Attack Bonus = %s" % (self.ac, self.ref, self.fort, self.will, self.init, self.bab)

class Weapons(Base):
    __tablename__ = 'weapons'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    damage = Column(String(50), nullable=False)
    threat = Column(Integer, nullable=False)
    range = Column(Integer, nullable=False)
    char_id = Column(Integer, ForeignKey('characters.id'))

    def __repr__(self):
        return "Weapon = %s, Damage = %s, Threat = %s, Range = %s" % (self.name, self.damage, self.threat, self.range)

class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    weight = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    carry_weight = Column(Integer, nullable=False)
    char_id = Column(Integer, ForeignKey('characters.id'))

    def __repr__(self):
        return "Item = %s, Weight = %s, quantity = %s" %s (self.name, self.weight, self.quantity)

class Skills(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    rank = Column(Integer, nullable=False)
    synergy = Column(Integer, nullable=False)
    misc = Column(Integer, nullable=False)
    char_id = Column(Integer, ForeignKey('characters.id'))

    def __repr__(self):
        return "Skill = %s, Rank = %s, Synergy = %s, Misc = %s" % (self.name, self.rank, self.synergy, self.misc)

class Languages(Base):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    char_id = Column(Integer, ForeignKey('characters.id'))

    def __repr__(self):
        return "Language = %s" % (self.name)

class Feats(Base):
    __tablename__ = 'feats'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    char_id = Column(Integer, ForeignKey('characters.id'))

    def __repr__(self):
        return "Feat = %s" % (self.name)
