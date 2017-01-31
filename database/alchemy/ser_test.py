#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from database.alchemy.load_seq import *
from database.alchemy.load_bh import *
from py_scripts.helpers.parse_dicts import *

db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito_all.db'
engine = create_engine(db_path)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

Sequence
