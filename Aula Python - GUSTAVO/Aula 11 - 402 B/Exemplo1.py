notas = [6, 7, 6.5, 4.8, 8]
soma = 0
cont = 0

for nota in notas:
    soma += nota

# ou
# for i in range(len(notas))
# soma += notas[1]

media = soma / len(notas)

print(notas)
print(f'A média é: {media:.2f}')

for nota in notas:
    if nota > media:
        cont += 1

print(f'As notas acima da média são: {cont}')
