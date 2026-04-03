from database import db, Usuario

db.connect()
db.create_tables([Usuario])

def criar_conta():
    print("\n=== CRIAÇÃO DE CONTA ===")
    nome = input("Digite seu nome: ")
    try:
        numero = int(input("Digite o número da Conta (somente números): "))
        agencia = int(input("Digite o numero da sua agencia: "))
        senha = int(input("Digite a sua senha: "))
    except ValueError:
        print("Erro: Número da conta, agência ou senha deve ser um número inteiro.")
        return None

    usuario = Usuario.create(
        nome=nome, 
        agencia=agencia, 
        senha=senha,
        numero=numero,
        saldo=0.00
    )
    
    print("Conta criada para :", usuario.nome)
    return usuario
    
def login_system(login_agencia, login_senha):
    try:
        usuario_encontrado = Usuario.get(
            (Usuario.agencia == login_agencia) & (Usuario.senha == login_senha)
        )
        print(f"Login bem-sucedido! Bem-vindo(a), {usuario_encontrado.nome}")
        return usuario_encontrado
        
    except Usuario.DoesNotExist:
        print("Login falhou! Agência ou senha incorretos.")
        return None

def saque(usuario):
    saldo_atual = usuario.saldo
    
    try:
        saque_valor = float(input("Digite o valor do saque desejado: "))
    except ValueError:
        print("Valor de saque inválido. Por favor, digite um número.")
        return
        
    if saque_valor <= 0:
        print("O valor de saque deve ser positivo.")
    elif saque_valor > saldo_atual:
        print("Saldo insuficiente.")
    else:
        novo_saldo = saldo_atual - saque_valor
        
        usuario.saldo = novo_saldo
        
        usuario.save()
        
        print(f"Saque de R${saque_valor:.2f} efetuado com sucesso.")
        print(f"O seu saldo atual é R${novo_saldo:.2f}")

def deposito(usuario):
    saldo_atual = usuario.saldo
    
    try:
        deposito_valor = float(input("Digite o valor do deposito desejado: "))
    except ValueError:
        print("Valor de depósito inválido. Por favor, digite um número.")
        return
        
    if deposito_valor <= 0:
        print("O valor de depósito deve ser positivo.")
    else:
        novo_saldo = saldo_atual + deposito_valor
        
        usuario.saldo = novo_saldo
        
        usuario.save()
        
        print(f"Depósito de R${deposito_valor:.2f} efetuado com sucesso.")
        print(f"O seu saldo atual é R${novo_saldo:.2f}")

def mostrar(usuario):
    print("------------------------")
    print(f"O dono da conta é: {usuario.nome}")
    print(f"Número da conta: {usuario.numero}")
    print(f"Agência: {usuario.agencia}")
    print(f"O saldo atual é: R${usuario.saldo:.2f}") 
    print("------------------------")

def menu_principal(usuario):
    while True:
        print("\n========================")
        print("     Conta do Banco     ")
        print("1. Efetuar um saque     ")
        print("2. Efetuar um depósito  ")
        print("3. Mostrar Conta        ") 
        print("4. Finalizar programa   ")
        print("========================")
        try:
            n = int(input("Digite o número para escolher a função: "))
        except ValueError:
            print("Por favor, digite um número válido (1, 2, 3 ou 4).")
            continue
        if n == 1:
            saque(usuario)
        elif n == 2:
            deposito(usuario)
        elif n == 3:
            mostrar(usuario)
        elif n == 4:
            print("Programa finalizado. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2, 3 ou 4.")

def main():
    print("bem-vindo ao Banco BDS")
    print("------------------------")
    resposta = input("Você tem conta no Banco BDS? (S/N) ").upper()
    
    if resposta == "S":
        login_agencia = input("Digite o número da sua agência para login: ")
        login_senha = input("Digite a sua senha para login: ")
        
        usuario_logado = login_system(login_agencia, login_senha) 
        
        if usuario_logado:
            print("Iniciando menu...")
            menu_principal(usuario_logado) 
            return
        
    elif resposta == "N":
        novo_usuario = criar_conta() 
        
        if novo_usuario:
            print("Conta criada com sucesso!")
            menu_principal(novo_usuario)
            return 
        
    else:
        print("Resposta inválida. Por favor, digite S para Sim ou N para Não.")
    

if __name__ == "__main__":
    main()