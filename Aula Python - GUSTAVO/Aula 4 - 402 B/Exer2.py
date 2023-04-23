import os
os.system('cls')

print('Qual seu turno de trabalho?')
turno= input('N - Noturno ou D - diurno?: ')
hora= float(input('Qual sua carga horária?: '))

if turno == 'N': 
    hora_value= 45
else:
    hora_value= 37.50
    
salario_diario= hora_value * hora  

print(f'Seu ganho por dia no trabalho é de R${salario_diario:.2f}')
