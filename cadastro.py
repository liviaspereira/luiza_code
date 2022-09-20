'''Crie um sistema de cadastro de pessoas, pelo nome e idade, o sistema deve ter as seguintes opções:
- cadastrar pessoas
- listar pessoas
- sair'''


usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    idade_valida = False
    while idade_valida == False:
        try:
            idade = int(input("Digite sua idade: "))
            idade_valida= True
        except (ValueError, TypeError):
            print("Digite um valor inteiro")
        
    usuarios.append({"nome": nome, "idade": idade})
    
    print("\nUsuário cadastrado com sucesso!")
    
def listar_usuarios():
    print("\n")
    for user in usuarios:
        print("{} - {} anos".format(user["nome"], user["idade"]))

while True:
    option = int(input("\nDigite a opção desejada:\n 1 - Cadastrar pessoas\n 2 - Listar pessoas\n 3 - Sair\n"))
    
    if option == 1:
        cadastrar_usuario()
    elif option == 2:
        listar_usuarios()
    elif option == 3:
        exit()
    else:
        print("Opção inválida!")

