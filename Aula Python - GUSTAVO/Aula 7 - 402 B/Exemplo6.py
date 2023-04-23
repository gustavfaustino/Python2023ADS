import os
os.system('cls')

resp = 's'
contador = 0
soma = 0

while resp in 'sS':
    num = float(input('Digite um número: '))
    soma += num  # o mesmo que soma = soma(0) + num(n)
    contador += 1

    resp = input('Deseja continuar? [S/N]:  ')
    
media = soma / contador
print(f'A média é de {soma:.2f} é: {media:.2f}')
