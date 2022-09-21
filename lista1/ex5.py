"""Resolva estes problemas em Python, guardando os valores e seus resultados em
variáveis diferentes.
a. Calcule a área de um quadrado cujo lado seja 2 cm.
b. Uma mala custa R$120,00. Esta recebeu 5% de desconto. Quanto você irá pagar
por ela.
c. Um carro está viajando a uma velocidade média de 100 Km/h, o trecho de viagem
será 200 Km. Quantas horas irá demorar a viagem.
d. João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e
sua média.
e. Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a
verificação se a idade de Davi é maior que a idade de sua irmã."""

lado = 2
area = lado * lado
print(f"A área do quadrado é {area} cm²")


vel_media = 100
distancia_total = 200
tempo_total = distancia_total / vel_media
print(f"A viagem irá demorar {tempo_total} horas")

joao_pirulito = 2
maria_pirulito = 3
sofia_pirulito = 1
total_pirulito = joao_pirulito + maria_pirulito + sofia_pirulito
media_pirulito = total_pirulito / 3
print(f"O total de pirulitos é {total_pirulito} e a média é {media_pirulito}")

davi_idade = 13
irma_idade = 7
eh_mais_velho = davi_idade > irma_idade
print(f"Davi é mais velho que a irmã: {eh_mais_velho}")
