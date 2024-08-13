def programa_mas_utilizado():
    cantidad_programa1 = int(input("Ingrese la cantidad de veces que se utilizó el Programa 1: "))
    cantidad_programa2 = int(input("Ingrese la cantidad de veces que se utilizó el Programa 2: "))
    cantidad_programa3 = int(input("Ingrese la cantidad de veces que se utilizó el Programa 3: "))

    if cantidad_programa1 > cantidad_programa2 and cantidad_programa1 > cantidad_programa3:
        programa_mas_utilizado = 1
    elif cantidad_programa2 > cantidad_programa1 and cantidad_programa2 > cantidad_programa3:
        programa_mas_utilizado = 2
    else:
        programa_mas_utilizado = 3

    print(f"El programa más utilizado por el ascensor es el Programa {programa_mas_utilizado}")

programa_mas_utilizado()
