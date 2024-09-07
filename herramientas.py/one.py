import random
import string

def generar_contrasena(nombre, fecha_nac, gusto, complejidad):
    fecha_nac = fecha_nac.replace("-", "")

    base_contrasena = nombre + fecha_nac + gusto

    if complejidad == 1:
        caracteres = string.ascii_lowercase
    elif complejidad == 2:
        caracteres = string.ascii_letters
    else:
        caracteres = string.ascii_letters + string.digits + string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(10))
    contrasena = base_contrasena[:3] + contrasena + base_contrasena[-3:]

    return contrasena

nombre = input("Ingrese su nombre: ")
fecha_nac = input("Ingrese su fecha de nacimiento (AAAA-MM-DD): ")
gusto = input("Ingrese algo que le guste: ")
complejidad = int(input("Seleccione la complejidad de la contraseña (1-fácil, 2-media, 3-difícil): "))

contrasena = generar_contrasena(nombre, fecha_nac, gusto, complejidad)
print("Su contraseña sugerida es:", contrasena)

while True:
    validacion = input("¿Le gusta esta contraseña? (sí/no): ").strip().lower()
    if validacion == "sí" or validacion == "si":
        print("¡Un gusto ayudarte!")
        print("¡Excelente! Utilice esta contraseña de forma segura.")
        break
    elif validacion == "no":
        print("Generemos otra contraseña.")
        contrasena = generar_contrasena(nombre, fecha_nac, gusto, complejidad)
        print("Su nueva contraseña sugerida es:", contrasena)
    else:
        print("Por favor, responda 'sí' o 'no'.")
