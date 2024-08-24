ef control_ingreso (cupo_maximo):
    control=0
while personas_admitidas < cupo_Maximo :  # type: ignore
boleto = input ("Ingrese el numero de boleto a elegir")
if boleto. lower () == 'salir' :
if boleto == 'valido' :
admitidas += 1 # type: ignore
print("acceso permitido.")
else :
print("acceso denegado.")
if personas_admitidas == cupo_maximo: # type: ignore
    print("El cupo se ha llenado. No se permiten más ingresos.")

cupo_maximo = 100
control_ingreso(cupo_maximo)