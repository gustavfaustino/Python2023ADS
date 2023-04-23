import os
os.system('cls')

# Faça um programa em Python que receba a idade de cada um dos 10 alunos de
# uma escola, matriculados no Ensino Médio. O programa deverá verificar, calcular e
# imprimir:
# a) a quantidade de alunos que podem votar, ou seja, têm idade mínima de 16 anos.
# b) a média da idade dos alunos

votantes = 0
contador = 0
soma= 0

while contador <10:
    idade = int(input('Digite aqui a idade do aluno: '))
    contador += 1
    soma += idade
    if idade >=16:
        votantes += 1
    
media = soma / 10

print(f'Quantidade de alunos que podem votar: {votantes}')
print(f'Média de idade dos alunos: {media:.2f}')




