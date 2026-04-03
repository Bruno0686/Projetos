
from database import Usuario, db

db. connect(Usuario)

lista_usuarios = Usuario.select()
for u in lista_usuarios:
    print("Esse são os dados que o banco esta armazenando: ")
    print("-", u.id, u.agencia, u.senha, u.nome, u.saldo, "\n")

# delete =input("Dgite a agencia que vc deseja exculir: ")
# usuario=Usuario.delete().where(Usuario.agencia==delete)
# usuario.execute()
# print("Usuário excluído com sucesso!")


