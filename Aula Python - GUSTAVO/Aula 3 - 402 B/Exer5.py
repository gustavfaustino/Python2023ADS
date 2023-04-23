import math, os
os.system('cls')

ang= float(input('Digite o valor de um ângulo em graus: '))

ang_rad = math.radians(ang)

print(f'O valor do ângulo {ang:.2f}° em seno é: {math.sin(ang_rad):.2f}')
print(f'O valor do ângulo {ang:.2f}° em cosseno é: {math.cos(ang_rad):.2f}')
print(f'O valor do ângulo {ang:.2f}° em tangente é: {math.tan(ang_rad):.2f}')

