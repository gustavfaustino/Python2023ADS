import os
os.system('cls')

print('Bem-vindo a MDcalcs!')

print('---'*12)
print('O que deseja fazer?')
print('1 - Média')
print('2 - Diferença')
print('3 - Produto')
print('4 - Divisão')
op= input('[1, 2, 3 ou 4]: ')
if op >'4':
    print('Ops, essa operação não é válida!')
print('---'*12)

print('Agora digite dois números inteiros:')
n1= int(input('Número 1: '))
n2= int(input('Número 2: '))

print('---'*12)

if op in '1':
    print('Você escolheu MÉDIA')
    print(f'A média dos valores são: {((n1+n2)/2):.2f}')
    
elif op in '2':
    print('Você escolheu a DIFERENÇA')
    print(f'A diferença dos valores são: {(n1-n2)}')

elif op in '3':
    print('Você escolheu PRODUTO')
    print(f'O produto dos valores são: {(n1*n2)}')
    
elif op in '4':
    if n2==0:
        print('Não é possível dividir por zero!')
    else:
        print('Você escolheu DIVISÃO')
        print(f'A divisão dos valores são: {(n1/n2):.2f}')
else:
    print('Ops, essa operação não é válida! 😓')

print('---'*12)
resposta = input("Deseja encerrar o programa? (S/N): ")

if resposta in 'Ss':
    print("Finalizando o programa...")
    exit()
print("Continuando a execução do programa...")