# Crea clase Persona
class Persona:
    def __init__(self,nombre,edad,dni) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @edad.setter
    def edad(self,edad):
        if edad < 0:
            print (f'La edad debe ser mayor a 0')
        else:
            self.__edad = edad

    def valido_dni(self,dni):
        try:
            documento = int(dni)
        except ValueError:
            print (f'No es un DNI válido, deben ser números')
        if len(str(documento)) < 7 or len(str(documento)) > 8:
            print(f'No es un número válido para un DNI')

    @dni.setter
    def dni(self,dni):
        self.valido_dni(dni)
        self.__dni = dni

    def mostrar(self):
        return f'Nombre: {self.nombre}, DNI: {self.dni} y tiene {self.edad} años.'
    
    def es_mayor_de_edad (self):
        return self.edad >= 18
    

    