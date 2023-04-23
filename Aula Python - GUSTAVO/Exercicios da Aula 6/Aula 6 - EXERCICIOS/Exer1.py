import os
os.system('cls')

print('Olá, aqui você calculará o valor de seu salário mais a comissão de suas vendas!')
print('---'*27)
sala = float(input("Digite o valor de seu salário:R$ "))
vend = float(input('Digite o valor de suas vendas:R$ '))

comi = vend * 0.04
sal_fin = comi + sala

print(f'Sua comissão é de: R${comi:.2f}')
print(f'O valor final de seu salário, mais comissão, é de: R${sal_fin:.2f}')
 
print('---'*12)
resposta = input("Deseja encerrar o programa? (S/N): ")

if resposta in 'Ss':
    print("Finalizando o programa...")
    exit()

print("Continuando a execução do programa...")