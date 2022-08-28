'''Considere as seguintes variáveis:
ovo = 3.4
caju = 12.4
Qual será o valor de resposta em cada linha:
resposta = ovo if 1 > 2 else caju
resposta = ovo if ovo > caju else caju
resposta = ovo if ovo < caju else caju
resposta = 100 if ovo + caju > 15 else 200
resposta = 100 if ovo == 3 else 0'''

ovo = 3.4
caju = 12.4

if 1 > 2:
    print(ovo)
else:
    print(caju)


if ovo > caju:
    print(ovo)
else: 
    print(caju)


if ovo < caju:
    print(ovo)
else:
    print(caju)

if ovo + caju > 15:
    print(100)
else:
    print(200)

if ovo == 3:
    print(100)
else: 
    print(0)
