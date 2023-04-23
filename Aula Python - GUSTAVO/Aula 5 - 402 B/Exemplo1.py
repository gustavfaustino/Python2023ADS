import os
os.system('cls')

media= float(input('Qual a média do aluno?:  '))
freq= float(input('Qual a frequência do aluno?  '))

if freq < 75:
    print('Reprovado por falta')
elif media < 6: 
    print('Reprovado por nota')
else:
    print('Aprovado')
