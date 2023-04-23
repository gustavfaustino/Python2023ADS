import os , random
segundos = int(input('Digite a quantidade de segundos: '))

horas = segundos//3600

minutos = segundos%3600//60

segundos = segundos%60

print(f'{horas}h, {minutos} e min: {segundos}s')