import os
os.system('cls')

mb = float(input('Digite o tamanho do arquivo: '))
mbps = float(input('Digite a velocidade do link de internet (Mbps): '))

tempo_download= mb / (mbps / 8)

horas = int(tempo_download // 3600)
minutos = int((tempo_download % 3600) // 60)
segundos = int((tempo_download % 3600) % 60)

print( f'O tempo aproximado de download é de {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s).')
