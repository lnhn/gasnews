# This file is used for the create the class models

from peewee import *
from os import path
database_dir=path.abspath(__file__)
database_dir=database_dir[:-8]+"news.db"
db = SqliteDatabase(database_dir)
#print(database_dir)

class BaseModel(Model):
    class Meta:
        database = db


class News(BaseModel):
    title = CharField()
    pub = DateTimeField()
    text = TextField()
    lang = CharField()
    source = CharField()
    comment = TextField()
    add_date = DateTimeField()


class TransNews(BaseModel):
    title = CharField()
    pub = DateTimeField()
    text = TextField()
    source = CharField()
    comment = TextField()
    add_date = DateTimeField()


class SearchNews(BaseModel):
    title = CharField()
    link = CharField()
    pub_date = DateTimeField()
    source = CharField()
    add_date = DateTimeField()

class SearchWords(BaseModel):
    word=CharField()
    add_date=DateTimeField()


if not db.table_exists("news"):
    db.create_tables([News,TransNews,SearchNews])
    print('tables created')
