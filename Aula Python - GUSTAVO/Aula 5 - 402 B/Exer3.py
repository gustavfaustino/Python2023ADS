import os
os.system('cls')

nome = input('Digite o nome do produto aqui: ')
valor_compra= float(input('Digite o valor de compra aqui:  '))

if valor_compra <10:
    venda = valor_compra * 0.70
    print(f'O produto {nome} sairá com lucro de 70% com o valor de R${venda:.2f}')
elif valor_compra <30:
    venda = valor_compra * 0.50
    print(f'O produto {nome} sairá com lucro de 50% com o valor de R${venda:.2f}')
elif valor_compra <50:
    venda = valor_compra * 0.40
    print(f'O produto {nome} sairá com lucro de 40% com o valor de R${venda:.2f}')
elif valor_compra >=50:
    venda = valor_compra * 0.30
    print(f'O produto {nome} sairá com lucro de 30% com o valor de R${venda:.2f}')
