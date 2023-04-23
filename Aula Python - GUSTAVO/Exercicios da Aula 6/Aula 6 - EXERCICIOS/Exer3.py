import os
os.system('cls')

num= int(input('Digite o valor de um numero inteiro: '))

if num <0:
    print('Este é um número negativo!')
elif num ==0:
    print('Zero é um número nulo!')
else:
    print('Este número é positivo')
    
print('---'*12)
resposta = input("Deseja encerrar o programa? (S/N): ")

if resposta in 'Ss':
    print("Finalizando o programa...")
    exit()

print("Continuando a execução do programa...")

