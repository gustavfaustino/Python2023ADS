import os
os.system('cls')

valor_hora = float(input('Digite o valor da hora da aula: R$'))
carga_hra = float(input('Digite sua carga horária: '))


salario_base = valor_hora * carga_hra * 4.5
adicional = salario_base * 1 / 6
salario_final = salario_base + adicional

print(f'Salário final: R${salario_final:.2f}')

