import os
os.system('cls')

valor_compra = float(input('Digite o valor total da compra:  '))
parcela = int(
    input('Em quantas vezes você deseja parcelar? [2, 4, 6 ou 8]:  '))

match(parcela):
    case 2: valor_compra * 1.03
    case 4: valor_compra * 1.07
    case 6: valor_compra * 1.09
    case 8: valor_compra * 1.12
    case _: valor_compra = 0
if valor_compra <= 0:
    print('Valor de parcelar inválido!')
else:
    print(f'O valor de cada parcelas é: R${valor_compra/parcela:.2f}')
