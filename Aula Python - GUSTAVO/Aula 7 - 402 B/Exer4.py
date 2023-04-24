# 4- Escreva um algoritmo que leia um grupo de valores reais e determine quantos
# valores são positivos e quantos são negativos. Determine, também, qual é o menor
# desses valores. Utilize o comando de repetição que desejar.

qtd_positivos = 0
qtd_negativos = 0
menor_valor = 0

while True:
    num = float(input('Digite um número ou 0 para terminar'))
    if num == 0:
        break
    if num >0:
        qntd_positivos +=1
    else:
        qntd_negativos +=1
        if num < menor_valor:
            menor_valor = num

print(f"Quantidade de valores positivos: {qtd_positivos}")
print(f"Quantidade de valores negativos: {qtd_negativos}")
print(f"Menor valor: {menor_valor}")
