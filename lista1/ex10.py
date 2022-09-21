"""Crie o seguinte programa Python no arquivo lista03_02.py: Colete o nome da
pessoa, a cidade de nascimento dela, e o ano em que ela nasceu. Depois você irá mostrar
os dados coletados em linhas diferentes. E também, deverá informar quantos anos a
pessoa terá no ano 2030"""

nome = input("Qual o seu nome? ")
cidade_nascimento = input("Em que cidade nasceu? ")
ano = int(input("Qual o ano de nascimento? "))
idade = 2022 - ano

print(f"{nome}, {cidade_nascimento} , {ano}, {idade} anos")
