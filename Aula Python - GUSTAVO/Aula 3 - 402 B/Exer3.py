
import os
os.system('cls')

print('Qual sua data de nascimento?')
anos = int(input('Digite sua idade em anos:'))
meses = int(input('Digite o número de meses desde seu aniversário: '))
dias = int(input('Digite o número do dia de seu nascimento: '))

dias_totais = 365 * anos + 30 * meses + dias

print(f'A quantidade de dias que você está aqui, em média, é: {dias_totais}')

# Esse cálculo não é exato por n fatores, mas por acaso na minha situaçao (18, 04, 13) isso deu certo.
