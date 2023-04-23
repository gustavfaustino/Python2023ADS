
#bin = 1010
#n=4
#linguagem = digito1 * base ** 3 + d2*base**2 ...

binario = input("Digite o número em binário: ")

n= len(binario)-1
decimal = 0

for d in binario:
  decimal = decimal + int(d)*2**n
  n= n-1
  
print(f'O binário é igual a {decimal}(10)')