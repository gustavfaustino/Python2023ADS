import os

os.system('cls')

idade = int(input('Por favor, digite a sua idade:  '))

if idade < 16:
    print('Você não pode votar ainda!')
elif idade < 18 or idade > 65:
    print('Você é um eleitor facultativo, sem a obrigaçâo pelo voto')
else:
    print('Você é um eleitor obrigatório!')
