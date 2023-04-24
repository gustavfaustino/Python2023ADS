# 3- Faça um programa em Python que leia um valor n, inteiro e positivo, calcule e
# mostre a seguinte soma:
# S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n
import os
os.system('cls')

n = int(input('Digite um número positivo e inteiro aqui:  '))

soma = 0

for c in range(1,n+1):
  soma +=1/c
  
print(f'O resultado da soma é: {soma:.2f}')
