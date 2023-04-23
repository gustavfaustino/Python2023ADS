numero = int(input('Digite um número inteiro: '))

for i in range(11):
    # range( inicio, parada, incremento)
    tab = numero * i
    print(f'|{numero}*{i} = {tab}|')
