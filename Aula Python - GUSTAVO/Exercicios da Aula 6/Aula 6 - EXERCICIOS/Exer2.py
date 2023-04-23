import os
os.system('cls')

print('Seja bem-vindo, aqui calcularemos a hora, minutos e segundos formatados, a partir de uma quantia de segundos')
seg = int(input('Digite aqui a quantidade de segundos: '))

horas = seg // 3600
min = (seg % 3600) // 60
seg = (seg % 60)

print(f'O seu horário é: {horas} hora(s), {min} minuto(s) e {seg} segundo(s).')

print('---'*12)
resposta = input("Deseja encerrar o programa? (S/N): ")

if resposta in 'Ss':
    print("Finalizando o programa...")
    exit()

print("Continuando a execução do programa...")
