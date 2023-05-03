import os
os.system('cls')

valor = float(input('Qual o valor do prodtuo'))

valor += (valor * 0.05)

# trocaria o ponto pela virgula, ou qualquer coisa desejada

print(f'O valor acrescido é de: R$ {valor:.2f}'.replace('.',','))