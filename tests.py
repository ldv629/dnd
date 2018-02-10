#!/usr/bin/env python3

import character_sheet as cs
import os

if os.path.isfile('./test.db'):
    os.remove('./test.db')
engine = cs.create_engine('sqlite:///test.db')
cs.dnd_db.Base.metadata.create_all(engine)
Session = cs.sessionmaker(bind=engine)
session = Session()

cs.session = cs.init_database('test')

def create_test_characters():
    cs.create_character('Bob',1,'Human',20)
    cs.create_character('Bob',2,'Human',20)
    cs.create_character('Bob',3,'Human',20)
    cs.create_character('Bob',4,'Human',20)
    cs.create_character('Alice',5,'Human',20)
    cs.create_character('Eve',9,'Human',20)
    #TODO: add tests to make sure level and hp are with in bounds

    cs.add_feat('foo',1)
    cs.add_feat('foo',2)
    cs.add_feat('foo',3)
    cs.add_feat('foo',4)
    cs.add_feat('bar',1)
    cs.add_feat('bar',5)
    cs.add_feat('bar',4)
    #TODO: ^^ needs to be relational in some manner to allow for multiple feats per character right now
    #one to many?

    #TODO: check to make sure not adding duplicate feat/language

    cs.add_language('common',1)
    cs.add_language('common',2)
    cs.add_language('elvin',3)
    cs.add_language('dwarven',4)
    cs.add_language('Infernal',1)
    cs.add_language('Abyssal',5)
    cs.add_language('Draconic',4)


def tests():
    cs.get_feats(1)
    cs.get_languages(1)
