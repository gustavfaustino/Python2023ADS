#Escreva um programa em Python que solicite ao usuário os valores de três contas
#de consumo (p.ex. água, luz e telefone) e o valor de seu salário. Verifique se o salário
#é suficiente para pagar as três contas, caso não seja apresente a mensagem “Salário
#insuficiente!”. Caso seja, apresente o valor que restou do salário após pagar as contas

import os
os.system('cls')

agua= float(input('Por favor, digite o valor, em média, do gasto em água: '))
luz= float(input('Digite o valor, em média, do gasto em luz: '))
internet= float(input('Digite o valor do gasto em internet: '))
salario= float(input('Qual valor de seu ganho liquido?: R$'))

gastos= (agua+luz+internet)

if gastos< salario:
    restante= salario-gastos
    print(f'O valor restante de seu salario menos esses gastos de consumo, é de: R$ {restante:.2f}')
    # Dificil um pobre viver bem pagando o minimo que qualquer um merece.
else:
    print('Salário insuficiente!!')
    
        
