import os
os.system('cls')

nomes = []
notas = []

while True:
    nome = input("Qual nome do aluno? ")
    n1 = float(input(f"Qual a nota 1 do {nome}? "))
    n2 = float(input(f"Qual a nota 2 do {nome}? "))
    media = (n1+n2)/2
    nomes.append(nome)
    notas.append(media)    
    resp= input("Deseja digitar outro aluno?").upper()
    if resp in 'Nn': 
        break
print(10*"---")

n = int(input("Digite o número do aluno: "))
#       metodo grande:
#print(f"Média: {notas[n]}")
#if notas[n] > 6:
#    print(f"Resultado: APROVADO")
#else:
#    print(f"Resultado: REPROVADO")

result = 'Aprovado' if notas[n] > 6 else 'Reprovado'
print(f"O aluno {nomes[n]}, foi {result} com média {notas[n]}")