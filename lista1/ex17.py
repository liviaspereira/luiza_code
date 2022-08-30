'''Dada uma equação de segundo grau, calcule suas raízes utilizando a
fórmula de Bhaskara'''

a = int(input("informe o valor de a: "))
b = int(input("informe o valor de b: "))
c = int(input("informe o valor de c: "))

delta = (b**2) - (4*a*c)
x1 = (-b + (delta**0.5)) / (2*a)
x2 = (-b - (delta**0.5)) / (2*a)

print("as raízes da equação são:", x1, x2)