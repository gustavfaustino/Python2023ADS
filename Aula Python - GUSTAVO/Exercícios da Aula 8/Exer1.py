import os
os.system('cls')

carneiro = 0
mimir = 'n'

while mimir == 'n' or mimir == 'N':
    mimir= input('Já dormiu? [s/n]: ')
    carneiro += 1

carneiro -= 1
print(f'Você contou {carneiro} carneirinhos!\nBom sonhos...')

