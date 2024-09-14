class Vehiculo: 
   def __init__ (self, marca : str, combustible : str):
      self.marca = marca
      self.combustible = combustible 
   def encender (self ):
      pass 
   def arrancar (self ):
      pass
carro = Vehiculo ("toyota","Corriente")
print (carro)
print (type(carro))

class Moto (Vehiculo) :
     def __init__(self, marca:str,combustible:str): 
        super().__init__(marca,combustible)
class Carro (Vehiculo):
   pass
motocicleta = Moto ("Honda","Corriente")
mi_carro = Carro ("Mazda","Extra")
print(motocicleta,mi_carro)

class Vehiculo:
     def __init__ (self, marca:str,combustible:str,tipo:str):
         self.marca = marca
         self.combustible = combustible 
         self.tipo = tipo
     def encender (self): 
         pass
     def arrancar (self):
         pass
class moto (Vehiculo):
     def __init__(self, marca, combustible):
        super().__init__( marca, combustible, tipo= "Moto")

class Carro(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible, tipo= "Carro")
        moto = Moto("honda", "corriente")
carro = Carro("mazda", "extra")
print(moto)
print(carro)

class Vehiculo:
    def __init__(self, marca, combustible, tipo, nivel_combustible):
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo
        self.nivel_combustible = nivel_combustible  # En galones
    
    def encender(self):
        if self.nivel_combustible / 100 < 0.10:
            pass
    def arrancar(self):
        pass         
    def __str__(self):
        pass
class Moto(Vehiculo):
    def __init__(self, marca, combustible, nivel_combustible):
        super().__init__(marca, combustible, tipo="Moto", nivel_combustible=nivel_combustible)

class Carro(Vehiculo):
    def __init__(self, marca, combustible, nivel_combustible):
        super().__init__ (marca, combustible, tipo= "Carro", nivel_combustible=nivel_combustible)
moto = Moto("honda", "combustible", 8)
carro = Carro("mazda", "extra", 50)
print(moto.encender())
print(carro.encender())

class Vehiculo:
    def __init__(self, marca, combustible, tipo, nivel_combustible):
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo
        self.nivel_combustible = nivel_combustible 
    
    def encender(self):
        if self.nivel_combustible / 100 < 0.10:
            return "Advertencia: El nivel de combustible es muy bajo. Necesitas ir a la gasolinera."
        else:
            return "El vehículo está encendido."
    
    def arrancar(self):
        return "El vehículo está en marcha."
    
    def consumir_combustible(self, consumo):
        if self.nivel_combustible > 0:
            self.nivel_combustible -= consumo
            if self.nivel_combustible <= 0:
                self.nivel_combustible = 0
                return "El vehículo se ha detenido. No tienes combustible."
            elif self.nivel_combustible / 100 < 0.10:
                return "Advertencia: El nivel de combustible es muy bajo. Necesitas ir a la gasolinera."
            else:
                return f"Quedan {self.nivel_combustible} galones de combustible."
        else:
            return "No puedes arrancar, no tienes combustible."

    def __str__(self):
        return f"Vehículo tipo: {self.tipo}, marca: {self.marca}, combustible: {self.combustible}"

class Moto(Vehiculo):
    def __init__(self, marca, combustible, nivel_combustible):
        super().__init__(marca, combustible, tipo="Moto", nivel_combustible=nivel_combustible)

class Carro(Vehiculo):
    def __init__(self, marca, combustible, nivel_combustible):
        super().__init__(marca, combustible, tipo="Carro", nivel_combustible=nivel_combustible)

moto = Moto("honda", "combustible", 4)  
carro = Carro("mazda", "extra", 60) 

print(carro.arrancar())
print(carro.consumir_combustible(20))
print(carro.consumir_combustible(40))
print(carro.consumir_combustible(20))
