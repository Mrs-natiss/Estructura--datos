
numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el segundo número: "))
numero3=int(input("Ingrese el tercer número: "))

if numero1 >= numero2 and numero1 >= numero3:
    numero_mas_grande = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    numero_mas_grande = numero2
else:
    numero_mas_grande = numero3

if numero1 <= numero2 and numero1 <= numero3:
    numero_mas_grande = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    numero_mas_grande = numero2
else:
    numero_mas_grande = numero3

print("El número más grande es:", numero_mas_grande)
print("El número más pequeño es:", numero_mas_grande)



