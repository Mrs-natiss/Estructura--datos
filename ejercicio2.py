#Solicitar si el numero es par o impar
numero=int(input("Ingrese un numero: "))
if numero%2==0:
    print("El numero es par")
else:
    print("El numero es impar")

#Mostrar el resultado 
print("El numero es par" if numero%2==0 else "El numero es impar")

