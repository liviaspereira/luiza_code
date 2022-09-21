"""Este programa irá calcular a área de um
triângulo. Peça para a pessoa informar a medida numérica da base do triângulo, depois
colete o valor da altura. Apresente o valor da área do triângulo"""

lado = float(input("Digite o lado do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
area = lado * altura / 2
print(f"A área é: {area} ")
