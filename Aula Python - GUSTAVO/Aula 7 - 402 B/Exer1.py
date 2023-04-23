#1- Faça um programa em Python que imprima os números pares entre 0 e 100.
pares = 0
for pares in range(101):
    if pares %2!=0:
        continue
    print(pares)