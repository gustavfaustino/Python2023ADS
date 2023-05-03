import os
os.system('cls')

num = input('Digite um numero em binario: '.upper())
base = int(input('Digite base: [2] [8] [16]'))
n = len(num)-1


dig = '0123456789ABCDEF'
decimal = 0

for b in num:
    decimal += dig.find(b)*base**n
    n -= 1

print(decimal)