def controlar_ingresos(cupo_maximo):
    personas_admitidas = 0

    while personas_admitidas < cupo_maximo:
        boleto = input("Ingrese el número de boleto o 'salir' para terminar: ")

        if boleto.lower() == 'salir':
            break

        if boleto == 'valido':
            personas_admitidas += 10
            print("Acceso permitido.")
        else:
            print("Acceso denegado.")

    if personas_admitidas == cupo_maximo:
        print("El cupo se ha llenado. No se permiten más ingresos.")


cupo_maximo = 100
controlar_ingresos(cupo_maximo)


