def obtener_programa_usuarios(num_usuarios):
    """
    Solicita el programa académico de cada usuario y devuelve una lista con los programas ingresados.
    """
    programas = []
    for i in range(1, num_usuarios + 1):
        programa = input(f"Ingrese el programa del usuario {i}: ")
        programas.append(programa)
    return programas

def programa_mas_frecuente(programas):
    """
    Determina el programa académico más frecuente en la lista de programas.
    """
    conteo_programas = {}
    for programa in programas:
        conteo_programas[programa] = conteo_programas.get(programa, 0) + 1

    programa_maximo = max(conteo_programas, key=conteo_programas.get)
    return programa_maximo

def main():
    try:
        num_usuarios = int(input("Ingrese el número de usuarios: "))
        programas_usuarios = obtener_programa_usuarios(num_usuarios)
        programa_resultante = programa_mas_frecuente(programas_usuarios)
        print(f"El programa más utilizado en el ascensor es: {programa_resultante}")
    except ValueError:
        print("Por favor, ingrese un número válido de usuarios.")

if __name__ == "__main__":
    main()
