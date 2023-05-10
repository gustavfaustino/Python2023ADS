import os
os.system('cls')

num = []
maior = 0

while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    num.append(n)
    
média = sum(num)  / len(num) #len ira verificar quantos números foram digitados e sum irá somar todos os números
print(num)
print(f'A média é: {média:.2f}')
for n in num:
    if n > maior:
        maior = n
#irá verificar se o numero digitado é maior que o elemento "maior". Caso seja,
#ele vai armazenar nesse elemento.

print(f'O maior número digitado é: {maior}')