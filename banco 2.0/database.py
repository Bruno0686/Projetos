from peewee import *
import streamlit as st 

 

db = SqliteDatabase("banco.db")  

 

class Usuario(Model): 

    nome = CharField() 

    agencia = IntegerField(unique=True) 

    senha = CharField() 

    saldo = FloatField(default=0.0) 

 

    class Meta: 

        database = db 
Usuario.create_table()