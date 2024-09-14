num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, x, /): ")
if operacion == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operacion == "x":
    resultado = num1 * num2
    print(f"{num1} x {num2} = {resultado}")
elif operacion == "/":
    if num2 == 0:
        print("No se puede dividir entre cero.")
    else:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
else:
    print("Operación inválida.")
