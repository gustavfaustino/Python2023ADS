import math
import os
os.system('cls')

# INICIO
print('Olá e seja bem-vindo ao BasicCalc. Por favor, selecione a operação: ')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

# OPÇÕES
OP = int(input('Digite aqui sua escolha [1, 2, 3 ou 4]: '))

# VALORES
n1 = float(input('Digite o primeiro número:  '))
n2 = float(input('Digite o segundo número:  '))

# RESULTADOS
match(OP):
    case 1:
        soma = n1+n2
        print(f'Resultado: {n1} + {n2} = {soma:.2f}')
    case 2:
        sub = n1-n2
        print(f'Resultado: {n1} - {n2} = {sub:.2f}')
    case 3:
        mult = n1*n2
        print(f'Resultado: {n1} x {n2} = {mult:.2f}')
    case 4:
        div = n1/n2
        print(f'Resultado: {n1} / {n2} = {div:.2f}')

print('Obrigado por usar minha calculadora 🤗')
print('Aperte qualquer tecla para continuar...')
