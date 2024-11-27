class mascota:
    def __init__(self,nombre,edad,salud,precio):
        self.nombre=nombre
        self.edad= edad
        self.salud= salud
        self.precio=precio

    def actualizar_informacion(self,edad=None,salud=None, precio=None):
        if edad:   #si existe edad, etc. (ya que dice none, entonces vamos a hacer q la edad se actualice)
            self.edad=edad
        if saludd:
            self.salud= salud
        if precio:
            self.precio=precio

    

    def mostrar_informacion(self):
        return f"Mascota: {self.nombre}, Edad: {self.edad}, Salud: {self.salud}, Precio {self.precio}"

class Perro(mascota):
    def __init__(self, nombre, edad, salud, precio,raza, nivel_de_energia):
        super().__init__(nombre, edad, salud, precio)
        self.raza=raza
        self.nivel_de_energia=nivel_de_energia

    def mostrar_caracteristicas(self):
        return f"raza: {self.raza} y nivel de energia: {self.nivel_de_energia}"
    

    #hacemos lo mismo con el gato copiamos y pegamos
class Gato(mascota):
    def __init__(self, nombre, edad, salud, precio,raza,independencia):
        super().__init__(nombre, edad, salud, precio)
        self.raza=raza
        self.independencia=independencia

    def mostrar_caracteristicas(self):
        return f"raza: {self.raza} y nivel de energia: {self.independencia}"