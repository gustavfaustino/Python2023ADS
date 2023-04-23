import os
os.system('cls')

h= float(input('Digite aqui sua altura em M: '))
sx= input('Digite aqui seu sexo biológico [M/F]: ')

if sx in 'Mm':
    idM= (72.7*h) - 58
    print (f'Seu peso ideal é: {idM:.1f}')
elif sx in 'Ff':
    idF = (62.1*h) - 44.7
    print(f'Seu peso ideal é: {idF:.1f}')
else:
    print('Isto não é um sexo válido!!')
             
print('---'*12)
resposta = input("Deseja encerrar o programa? (S/N): ")

if resposta in 'Ss':
    print("Finalizando o programa...")

print("Continuando a execução do programa...")
