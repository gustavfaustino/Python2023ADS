
unidade = input('Digite a unidade de medida:')

base = float(input(f'Qual valor da base do retângulo em {unidade}?: '))
altura = float(input(f'Qual valor da altura do retângulo em {unidade}?: '))

area = base * altura
perimetro = 2 * ( base + altura )

print(f"A área do retângulo é {area:.2f} {unidade}² e o perímetro é {perimetro:.2f} {unidade}")