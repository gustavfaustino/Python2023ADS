#Escreva um algoritmo que solicite um número ao usuário. Caso seja digitado um
#valor entre 0 e 9, mostre: “valor correto”, caso contrário mostre: “valor incorreto”.
import os
os.system('cls')

num= int(input('Digite um número inteiro de 0-9:  '))

if num >=0 and num <=9:
    print(f'Valor corrento, {num}')
else:
    print(f'Valor incorreto, {num}')
