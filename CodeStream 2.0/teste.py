from database import Video, dba

dba. connect(Video)

lista_usuarios = Video.select()
for u in lista_usuarios:
    print("-", u.Nome, u.Url)

# delete =input("Dgite o nome do Video que vc deseja exculir: ")
# usuario=Video.delete().where(Video.Nome==delete)
# usuario.execute()
# print("Video excluído com sucesso!")
