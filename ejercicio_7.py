class Cuenta():

    def __init__(self,titular,cantidad=0) -> None:
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @titular.setter
    def titular(self,titular):
        self.titular=titular

    def mostrar(self):
        print(f'Titular: {self.titular}, Cantidad: {str(self.cantidad)}')

    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad=self.__cantidad + cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad
        