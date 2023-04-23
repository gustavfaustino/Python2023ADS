# 4- Escreva um algoritmo que leia um grupo de valores reais e determine quantos
# valores são positivos e quantos são negativos. Determine, também, qual é o menor
# desses valores. Utilize o comando de repetição que desejar.

qtd_positivos = 0
qtd_negativos = 0
menor_valor = 0

for valor in range(-6, 9):
    if menor_valor is 0 or valor < menor_valor:
        menor_valor = valor

    if valor > 0:
        qtd_positivos += 1
    elif valor < 0:
        qtd_negativos += 1

print(f"Quantidade de valores positivos: {qtd_positivos}")
print(f"Quantidade de valores negativos: {qtd_negativos}")
print(f"Menor valor: {menor_valor}")
