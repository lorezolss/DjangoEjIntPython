# Calcula MCD entre dos números
def calcular_mcd(num1,num2):
   c = 0 
   if num1 == num2:
      print (f'Ambos números son iguales')
      return num1
   else:
      a = max(num1,num2)
      b = min(num1,num2)
      while a % b != 0:
        c = a % b
        a = b
        b = c
   return b

# Programa principal
n1 = int(input("Ingrese un número:"))
n2 = int(input("Ingrese otro número:"))
mcd = calcular_mcd(n1,n2)
print(f"El MCD entre {n1} y {n2} es {mcd}")

      