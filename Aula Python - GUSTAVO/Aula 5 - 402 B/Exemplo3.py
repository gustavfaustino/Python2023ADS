import os
os.system('cls')

print('Por favor digite três números inteiros distintos:')
d1= int(input('Digite o número 1: '))
d2= int(input('Digite o número 2: '))
d3= int(input('Digite o número 3: '))

if d1>d2 and d1>d3:
    print(f'O {d1} é o maior')
elif d2>d1 and d2>d3:
    print(f'O {d2} é o maior')
elif d3>d1 and d3>d2:
    print(f'O {d3} é o maior')
else:
    print('Por favor digite valores distintos')