peso = float(input("Ingrese el peso de la persona (en kilos): "))
altura = float(input("Ingrese la altura de la persona (en metros): "))
imc = peso / (altura * altura)
print("El IMC de la persona es:", imc)
if imc > 25:
    print("La persona tiene sobrepeso.")
else:
    print("La persona no tiene sobrepeso.")
