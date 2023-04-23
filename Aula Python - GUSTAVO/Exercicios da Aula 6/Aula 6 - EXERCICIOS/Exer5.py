import os
import math
os.system('cls')

m2 = float(input('Digite o valor de metros quadrados(m²) a ser pintado: '))
# 1 lata = 54m² e R$80

latas = m2 / 54
preço = math.ceil(latas) * 80

print(f'Você precisa comprar {math.ceil(latas)} de tinta')
print(f'O valor total a se pagar é: R${preço:.2f}')

print('---'*12)
resposta = input("Deseja encerrar o programa? (S/N): ")

if resposta in 'Ss':
    print("Finalizando o programa...")
    exit()
print("Continuando a execução do programa...")
