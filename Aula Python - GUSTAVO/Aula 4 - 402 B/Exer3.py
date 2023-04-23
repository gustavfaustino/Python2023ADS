#Faça um programa em Python que obtenha o valor de uma compra, calcular e
#mostrar o valor da compra considerando o desconto, conforme descrito abaixo:
#• para compras acima de R$ 200 a loja dá um desconto de 20%
#• para as abaixo disso não tem desconto, mostre o valor da compra.


import os
os.system('cls')

compra= float(input('Digite o valor da sua compra: R$ '))

if compra >=200:
    desc= 20
else:
    desc=0

compra_real= compra - ( desc *compra /100 )

print(f'O valor total da sua compra, mais descontos, é de: R$ {compra_real:.2f}')

 