'''Crie um script que leia 10 números inteiros positivos e que irá apresentar:
● A lista dos valores lidos de forma ordenada.
● A contagem de cada item. Por exemplo, se o usuário informou [1,1,1,1,2, 3],
aqui apresentamos:
○ 1: 4x.
○ 2: 1x.
○ 3: 1x.
● Uma saída identificando o número, se o número é par e se é primo. Isto será feito
separando por vírgulas: Por exemplo, se informou [1,2,3,6]. Iremos apresentar aqui:
○ 1,ímpar,não é primo
○ 2,par,é primo
○ 3,ímpar,é primo
○ 6,par,não é primo'''


def numero_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True 

lista = []

for i in range(10):
    numero = int(input("Digite um numero: "))
    lista.append(numero)
lista.sort()

cont = {}
for numero in lista:
    if numero in cont:
        cont[numero] += 1
    else:
        cont[numero] = 1

for numero, quantidade in cont.items():
    print(f'{numero}: {quantidade}x.')

for numero in cont:
    eh_primo = numero_primo(numero)
    resposta = f'{numero}'
    if numero % 2 == 0:
        resposta += ', par'
    else:
        resposta += ', impar'

    if eh_primo:
        resposta += ', é primo'
    else:
        resposta += ', não é primo'

    print(resposta)



    