def es_palindromo(cadena):

    cadena = cadena.replace(" ", "").lower()

    return cadena == cadena[::-1]

if __name__ == "__main__":
    cadena = input("Ingresa una cadena: ")

    if es_palindromo(cadena):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")
     