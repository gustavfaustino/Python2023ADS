import os
os.system('cls')

# Faça um programa que solicite o nome da pessoa e que horas são (apenas
# horas). Posteriormente mostre na tela uma mensagem de “Bom dia”, “Boa tarde” ou
# “Boa noite” ao usuário. Para tanto, considere que:
# • Bom dia: entre 5 e 12 h.
# • Boa tarde: entre 13 e 18 horas.
# • Boa noite: entre 19 e 4 horas.

user= input('Primeiramente, qual seu nome?: ')
hr = int(input('Que horas são? (0-23): '))

if hr >= 5 and hr <= 12:
    print(f'Bom dia, {user}!! Que seu dia seja fantástico!')
elif hr >= 13 and hr <= 18:
    print(f"Boa tarde, {user}!! Espero que esteja tendo um dia bom!")
else:
    print(f'Boa noite, {user}. Espero que tenha um bom descanso!')
    
print('---'*12)
resposta = input("Deseja encerrar o programa? (S/N): ")

if resposta in 'Ss':
    print("Finalizando o programa...")
    exit()
print("Continuando a execução do programa...")