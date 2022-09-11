'''Em vendedor ganha uma comissão de uma venda da seguinte forma: Se a
venda for ...
● menor que R$1000,00, o vendedor não ganha nenhuma comissão;
● entre R$1.000,00 e R$5.000,00, o vendedor ganha uma comissão de 10% da
venda;
● entre R$5.000,00 e R$10.000,00, a comissão será de 20% da venda;
● entre R$10.000,00 e R$50.000,00 a comissão será de 25% da venda;
● acima de R$50.000,00 a comissão será de 30% da venda.
Faça um programa que informe o valor da comissão do vendedor para uma venda.'''



venda = float(input('Digite o valor da venda: '))
if venda < 1000:
    comissao = 0
elif venda < 5000:
    comissao = venda * 0.1
elif venda < 10000:
    comissao = venda * 0.2
elif venda < 50000:
    comissao = venda * 0.25
else:
    comissao = venda * 0.3
print(f'Comissão: {comissao}')


