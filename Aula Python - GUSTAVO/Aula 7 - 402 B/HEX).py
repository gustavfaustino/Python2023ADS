#Faça um programa em Python que solicite um número decimal, faça a conversão e
#exiba o número digitado na base binária. Use a estrutura de repetição enquanto
#(while).

decimal = int(input('Digite um número em base decimal: '))
temp = decimal
bin= ""

while decimal >0:
  r= decimal%2
  bin =  str(r) + bin 
  decimal= decimal//2
  
print(f'{temp}(10) = {bin}(2)')