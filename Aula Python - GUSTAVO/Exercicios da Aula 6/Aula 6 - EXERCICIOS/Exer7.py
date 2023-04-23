import os, math
os.system('cls')

# Faça um programa que solicite as coordenadas de um ponto P, verifique e
# apresente na tela a qual quadrante pertence o ponto, desconsiderando a hipótese
# desse ponto estar sobre um dos eixos. Para tanto, lembre-se que:
# • 1º quadrante: x>0 e y>0
# • 2º quadrante: x<0 e y>0
# • 3º quadrante: x<0 e y<0
# • 4º quadrante: x>0 e y<0

print('Cordenadas do ponto P')
x= int(input('Digite aqui o valor de x:  '))
y= int(input('Digite aqui o valor de y:  '))

if x>0 and y>0:
    print(f'O ponto P{x,y} se encontra no 1º quadrante')
elif x<0 and y>0:
    print(f'O ponto P{x,y} se encontra no 2º quadrante')
elif x<0 and y<0:
    print(f'O ponto P{x,y} se encontra no 3º quadrante')
else:
    print(f'O ponto P{x,y} se encontra no 4º quadrante')
    
print('---'*12)
resposta = input("Deseja encerrar o programa? (S/N): ")

if resposta in 'Ss':
    print("Finalizando o programa...")
    exit()
print("Continuando a execução do programa...")
