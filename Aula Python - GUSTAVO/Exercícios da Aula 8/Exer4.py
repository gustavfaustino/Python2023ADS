import os
os.system('cls')

conta= int(input('Digite os 4 dígitos de sua conta: '))

D1= conta//100//10
D2= conta//100%10
D3= conta%100//10
D4= conta%10
digito = (D1+D2+D3+D4)%10

print(f'Número da conta completo: 00{conta:.0f}-{digito:.0f}')