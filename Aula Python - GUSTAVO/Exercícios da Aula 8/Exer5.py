# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça
# a quantidade de turmas e a quantidade de alunos para cada turma. Obs: considere que a
# média de alunos não pode ser um número fracionário.
import os
os.system('cls')
turma=int(0)
contador = 0
gente=int(0)

turmas = int(input('Qual a quantidade de turmas?: '))
while turma != turmas:
    turma+=1
    alunos= int(input(f'Digite a quantidade de alunos da {turma}° turma: '))
    gente += alunos
    contador += 1

media = gente / turmas

print('As turmas têm em média {:.0f} alunos.'.format(media))
