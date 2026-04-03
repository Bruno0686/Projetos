from peewee import *

db = SqliteDatabase('senhas e agencias.db')

class Usuario(Model):
    nome = CharField()
    agencia = IntegerField(unique=True)
    numero = IntegerField()
    senha = IntegerField()
    saldo = FloatField(default=0.0)

    class Meta:
        database = db