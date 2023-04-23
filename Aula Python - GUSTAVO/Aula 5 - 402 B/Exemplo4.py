import os
os.system('cls')

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso/(altura)**2

if imc < 20:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está com peso normal')
elif imc < 30:
    print('Você está sobrepeso')
elif imc < 40:
    print('Você está obeso')
else:
    print('você esta com obesidade mórbida')
