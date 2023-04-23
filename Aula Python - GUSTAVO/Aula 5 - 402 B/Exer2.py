# Faça um programa em Python que leia três valores inteiros (variáveis a, b e c) e
# efetue o cálculo da equação de segundo grau, apresentando: (i) as duas raízes,
# quando for possível efetuar o cálculo (delta positivo ou zero); (ii) a mensagem "Não há
# raízes reais", se não for possível fazer o cálculo (delta negativo); (iii) a mensagem
# "Não é equação do segundo grau", se o valor de a for igual a zero.

import os
import math
os.system('cls')

print('Calcularemos a sua equação do 2° grau')
a = float(input('Por favor, digite o valor de [a]:  '))
b = float(input('Digite o valor de [b]:  '))
c = float(input('Digite o valor de [c]:  '))

# Embora existam outras maneiras, Bhaskara é a mais simples e fácil
delta = b**2-4*a*c

if a == 0:
    # (iii)
    print('Não é equação do segundo grau, pois não há valor de [a]')
else:
    if delta < 0:
        # (ii)
        print('Não há raízes reais, pois Delta é um número negativo')
    else:
        # (i)
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print('As raízes da equção são:')
        print(f'Raíz positiva (X¹): {raiz1:.2f}')
        print(f'Raíz negativa (X²): {raiz2:.2f}')
