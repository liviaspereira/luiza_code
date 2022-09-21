"""Faça um programa que leia a nota de um aluno. Garanta que a nota seja um
valor inteiro entre zero e 100. Se o valor não estiver neste intervalo, informe que a
nota é inválida. Se a nota for maior que 60, informa que o aluno foi aprovado; caso
contrário, informa que ele foi reprovado."""

nota = int(input("Digite a nota do aluno: "))
if nota < 0 or nota > 100:
    print("Nota inválida")
elif nota >= 60:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
