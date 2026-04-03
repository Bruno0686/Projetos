from peewee import *
import streamlit as st

dbs = SqliteDatabase("Conta.dbs")

class Conta(Model):
    nome= CharField()
    email= CharField(unique=True)
    senha= CharField()
    class Meta():
        database = dbs
Conta.create_table(safe=True)

dba = SqliteDatabase('videos.db')

class Video(Model):
    Nome = CharField()
    Url = CharField() 

    class Meta:
        database = dba

dba.connect()
dba.create_tables([Video])