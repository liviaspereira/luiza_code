'''Crie um programa para calcular o valor a ser pago para um determinado produto para a
empresa NaoQueroMuitoSeuDinheiro. O pessoal desta empresa pediu o seguinte:
● Vamos coletar três valores:
○ O valor inicial da parcela.
○ O valor percentual de cada parcela.
○ A quantidade de parcelas.
● Para cada parcela a ser paga, o cálculo é o seguinte:
valor_parcela = valor_anterior + (valor_anterior *
percentual)
● No caso da primeira parcela, o valor anterior é o valor inicial.
Crie um programa que irá mostrar cada parcela e o seu valor. Por exemplo: se o valor inicial
for $100,00, o valor do percentual for 0,10, e a quantidade de parcelas for 2; logo nosso
programa irá mostrar:
Parcela 1: $ 110.0
Parcela 2: $ 121.0'''

valor_inicial = float(input('Digite o valor inicial da parcela: '))
percentual = float(input('Digite o valor percentual de cada parcela: '))
quantidade_parcelas = int(input('Digite a quantidade de parcelas: '))

for i in range(quantidade_parcelas):
    if i == 0:
        valor_anterior = valor_inicial
    else:
        valor_anterior = valor_parcela
    valor_parcela = valor_anterior + (valor_anterior * percentual)
    print(f'Parcela {i + 1}: {valor_parcela}')