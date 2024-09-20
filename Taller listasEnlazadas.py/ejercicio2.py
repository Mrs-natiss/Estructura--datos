class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.siguiente = None
class ListaDeTareas:
    def __init__(self):
        self.cabeza = None  

    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento):
        nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
        nueva_tarea.siguiente = self.cabeza  
        self.cabeza = nueva_tarea  

    def eliminar_tarea(self, descripcion):
        actual = self.cabeza
        anterior = None

        while actual and actual.descripcion != descripcion:
            anterior = actual
            actual = actual.siguiente

        if not actual:
            print("Tarea no encontrada.")
            return

        if anterior:
            anterior.siguiente = actual.siguiente
        else:
            self.cabeza = actual.siguiente

        print(f"Tarea '{descripcion}' eliminada.")

    def mostrar_tareas(self):
        actual = self.cabeza
        if not actual:
            print("No hay tareas.")
            return

        print("Lista de tareas:")
        while actual:
            print(f"Descripción: {actual.descripcion}, Prioridad: {actual.prioridad}, Vence: {actual.fecha_vencimiento}")
            actual = actual.siguiente

    def buscar_tarea(self, descripcion):
        actual = self.cabeza
        while actual:
            if actual.descripcion == descripcion:
                print(f"Tarea encontrada: {actual.descripcion}, Prioridad: {actual.prioridad}, Vence: {actual.fecha_vencimiento}")
                return
            actual = actual.siguiente
        print("Tarea no encontrada.")

    def marcar_completada(self, descripcion):
        self.eliminar_tarea(descripcion)
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Buscar tarea")
    print("5. Marcar como completada")
    print("6. Salir")

lista_tareas = ListaDeTareas()

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        desc = input("Descripción: ")
        pri = input("Prioridad (1=Alta, 3=Baja): ")
        fecha = input("Fecha de vencimiento: ")
        lista_tareas.agregar_tarea(desc, pri, fecha)

    elif opcion == "2":
        desc = input("Descripción de la tarea a eliminar: ")
        lista_tareas.eliminar_tarea(desc)

    elif opcion == "3":
        lista_tareas.mostrar_tareas()

    elif opcion == "4":
        desc = input("Descripción de la tarea a buscar: ")
        lista_tareas.buscar_tarea(desc)

    elif opcion == "5":
        desc = input("Descripción de la tarea completada: ")
        lista_tareas.marcar_completada(desc)

    elif opcion == "6":
        break

    else:
        print("Opción inválida.")
