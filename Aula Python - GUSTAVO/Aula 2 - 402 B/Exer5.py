cota= float(input('Digite a cotação atual do dólar:  '))
dolar= float(input('Digite o valor em dólar($) que deseja converter:  '))

valor_real= dolar *cota

print('O valor em reais (R$) é: R$ {:.2f}'.format(valor_real))
