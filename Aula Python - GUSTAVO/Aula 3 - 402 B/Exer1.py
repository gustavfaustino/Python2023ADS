
print('Aqui calcularemos o valor do tronco de uma pirâmide em métros.')
h= float(input('Digite o valor da altura: '))
Bmaior= float(input('Digite o valor da base MAIOR: '))
Bmenor= float(input('Digite o valor da base MENOR: '))

Form_Sanches= h/3 * (Bmaior**2 + Bmenor**2+(Bmaior**2 + Bmenor**2)**0.5)

print(f'O valor do tronco da pirâmide é {Form_Sanches:.2f} m³')
    
    











