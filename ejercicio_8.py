from ejercicio_7 import Cuenta
from ejercicio_6 import Persona

class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad=0, bonificacion=0) -> None:
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion (self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        return self.titular.edad < 25 and self.titular.es_mayor_de_edad()
    
    def retirar(self,cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print(f'No puede retirar dinero porque no es un titular válido.')

    def mostrar(self):
        print(f'Cuenta Joven Titular: {self.titular.mostrar()}, Bonificación: {self.bonificacion} %')


    