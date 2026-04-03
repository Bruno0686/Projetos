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