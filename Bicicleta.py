from Vehiculo import Vehiculo


#Si pones que el tipo es mayor que 3, es de tipo deportivo porque es de gama muy alta.
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__( color, ruedas)
        if tipo > 3:
            self.tipo = 'deportivo'
        else:
            self.tipo = 'urbano'
    def __str__(self):
        return Vehiculo.__str__(self) + ", es de tipo {}".format(self.tipo)

    def get_ruedas (self):
        return int(self.ruedas)
