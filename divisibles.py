n = []
div = []
divisor = int(input("Digite el divisor: "))
c = int(input("Digite la cantidad de numeros: "))
for i in range(c):
  numero = int(input("Digite numero: "))
  n.append(numero)
  if numero % divisor == 0:
    div.append(numero)
print("Numeros digitados: ", n)
print("Divisibles por ", divisor,":",div)