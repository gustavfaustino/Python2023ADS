import os
os.system('cls')

print('Bem-vindo a Pousada BelaFlor')
print(30*'-')
print('Por favor, digite qual tipo de sua diária?')
diaria = input('[S] Simples\n[D] Duplo\n[T] Triplo :  ')
# o comando \n cria 'listas'
if diaria in 'SsDdTt':
    qnt= int(input('Digite a quantidade de diárias:  '))

if diaria in 'sS':
    print(f'O valor total a pagar é: R$ { qnt*255.50:.2f}')
elif diaria in 'dD':
    print(f'O valor total a pagar é: R$ { qnt*305.50:.2f}')
elif diaria in 'tT':
    print(f'O valor total a pagar é: R$ { qnt*360.5:.2f}')

else:
    print('Tipo de diária inválido 🤨')
    
print('Obrigado e volte sempre!!')