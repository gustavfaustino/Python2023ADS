nomes = []

for i in range(5):
    nome = input('Digite um nome:')
    nomes.append(nome)
    # ^^ = em nomes, adicione o que for digitado em "nome"
    
n = int(input('Quem você quer exibir [0-4]? '))
print(nomes[n])