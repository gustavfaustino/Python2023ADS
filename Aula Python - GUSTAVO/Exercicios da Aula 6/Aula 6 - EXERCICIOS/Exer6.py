import os
os.system('cls')

n1 = float(input('Digite sua primeira nota parcial: '))
n2 = float(input('Digite sua segunda nota parcial: '))

md = (n1+n2) / 2

if md >= 9 and md <= 10:
    print('Você esta no conceito: A')
elif md >= 7.5 and md < 9:
    print('Você esta no conceito: B')
elif md >= 6 and md < 7.5:
    print('Você esta no conceito: C')
elif md >=4 and md <6:
    print('Você esta no conceito: D')
else:
    print('Você esta no conceito: E')
if md < 6:
    print('Você foi REPROVADO!')
elif md >= 6:
    print('Você foi APROVADO!')


print('---'*12)
resposta = input("Deseja encerrar o programa? (S/N): ")

if resposta in 'Ss':
    print("Finalizando o programa...")
    exit()
print("Continuando a execução do programa...")

