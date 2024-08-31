import random

def generar_contrasena(longitud):
  """Genera una contraseña aleatoria de una longitud dada.

  Args:
    longitud: La longitud de la contraseña.

  Returns:
    Una cadena con la contraseña aleatoria.
  """

  caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@$#"
  contrasena = ""
  for _ in range(longitud):
    contrasena += random.choice(caracteres)
  return contrasena
nueva_contrasena = generar_contrasena(10)
print(nueva_contrasena)