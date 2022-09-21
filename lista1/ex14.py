"""Colete a idade de duas pessoas.
E informe se a primeira idade é maior do que a da primeira. Neste aqui, basta responder
True para informar que a primeira idade é maior que a primeira."""

pessoa1 = int(input(("Qual a idade da primeira pessoa? ")))
pessoa2 = int(input(("Qual a idade da segunda pessoas? ")))

if pessoa1 > pessoa2:
    print("True")
else:
    print("False")
