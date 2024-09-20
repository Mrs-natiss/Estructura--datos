class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre  
        self.edad = edad     
        self.tipo = tipo      

class Nodo:
    def __init__(self, animal):
        self.animal = animal  
        self.siguiente = None  

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None 

    def agregar_animal(self, animal):
        if self.buscar_animal(animal.nombre):
            print(f"El animal {animal.nombre} ya está en la lista.")
            return

        nuevo_nodo = Nodo(animal)
        if self.cabeza is None:  
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:  
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo 

    def buscar_animal(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.animal.nombre == nombre: 
                return True  
            actual = actual.siguiente
        return False  

    def mostrar_animales_bucle(self):
        actual = self.cabeza
        while actual:
            print(f"Nombre: {actual.animal.nombre}, Edad: {actual.animal.edad}, Tipo: {actual.animal.tipo}")
            actual = actual.siguiente  

    def mostrar_animales_recursivo(self, nodo):
        if nodo is None:  
            return
        print(f"Nombre: {nodo.animal.nombre}, Edad: {nodo.animal.edad}, Tipo: {nodo.animal.tipo}")
        self.mostrar_animales_recursivo(nodo.siguiente)  

    def mostrar_animales(self):
        self.mostrar_animales_recursivo(self.cabeza)  

if __name__ == "__main__":  
    lista_animales = ListaEnlazada()  

    animal1 = Animal("Águila", 5, "Ave")
    animal2 = Animal("Pantera", 3, "Mamífero")
    animal3 = Animal("Vaca", 4, "Mamífero")
    animal4 = Animal("Águila", 2, "Ave")  

    lista_animales.agregar_animal(animal1)
    lista_animales.agregar_animal(animal2)
    lista_animales.agregar_animal(animal3)
    lista_animales.agregar_animal(animal4)  

    print("Animales (bucle):")
    lista_animales.mostrar_animales_bucle()

    print("\nAnimales (recursivo):")
    lista_animales.mostrar_animales()


