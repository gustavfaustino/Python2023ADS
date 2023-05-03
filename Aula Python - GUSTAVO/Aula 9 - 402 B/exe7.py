texto = input('Digite um texto:')
pontuação = [',', ',' 'etc']

#  remove sinais de pontuaçao
for p in pontuação:
    texto = texto.replace(p,' ')

# split devolve a lista com aplavras como itens
caracteres = len(texto.split())
print('Numero de caracteres:', caracteres)