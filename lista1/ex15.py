"""Em uma casa, uma família decidiu dividir
o valor da conta de energia entre os moradores da casa. No programa eles informam o
valor da conta de energia e quantos que irão pagar a conta no mês. O programa calculará
quanto cada um deverá contribuir com a conta de energia."""

valor_conta = float(input("Informe o valor da conta: "))
quantidade_pagantes = int(input("informe a quantidade de pagantes: "))
valor_cada_pessoa = valor_conta / quantidade_pagantes
print(f"O valor que cada um irá pagar será de: {valor_cada_pessoa} ")
