# Crea clase Persona
class Persona:
    def __init__(self,nombre,edad,dni) -> None:
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self.nombre
    
    @property
    def edad(self):
        return self.edad
    
    @property
    def dni(self):
        return self.dni
    
    @nombre.setter
    def nombre(self,nombre):
        self.nombre = nombre

    @edad.setter
    def edad(self,edad):
        self.edad = edad

    @dni.setter
    def dni(self,dni):
        self.dni = dni

    