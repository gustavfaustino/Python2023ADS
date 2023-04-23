n=0 
while n <2:
  nome = input('digite nome: ')
  n1= float(input(f'Qual a primeira nota do {nome}: '))
  n2= float(input(f'Qual a segunda nota do {nome}: '))
  media = (n1+n2)/2
  print(f'A média do aluno {nome} é {media:.2f}')
  n = n+1
  #Lembrar de atualizar a Variavel (n) pois se nao sempre se repetirá