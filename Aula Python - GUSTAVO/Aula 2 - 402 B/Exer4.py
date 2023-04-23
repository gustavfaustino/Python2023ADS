import math

a= float(input('Digite o valor do coeficiente a: '))
b= float(input('Digite o valor do coeficiente b: '))
c= float(input('Digite o valor do coeficiente c: '))

delta= b**2 -4*a*c

if delta <0:
    print('Não há raizes reais')
elif delta ==0:
    raiz= (-b +math.sqrt(delta)) /(2*a)
    print('O valor da raiz é {:.2f}'.format(raiz))
else:
    raiz1= (-b +math.sqrt(delta)) / (2*a)
    raiz2= (-b -math.sqrt(delta)) / (2*a)
    print('Os valores das raízes 1 e 2, respectivamente, são: {:.2f} e {:.2f}'.format(raiz1, raiz2))




