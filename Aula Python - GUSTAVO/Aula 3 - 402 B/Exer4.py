import os
os.system('cls')

print('Bem-vindo ao BancoPYT.')
valorPrestacao= float(input('Por favor, digite o valor de sua prestação: '))
qtdeDias= float(input('Digite a quantidade de dias de atraso: '))

if qtdeDias <= 10:
    multa = 2
elif qtdeDias <= 18:
    multa = 5
else:
    multa = 10

prestação = valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

print(f'O valor da sua prestação ficará: R${prestação:.2f}')