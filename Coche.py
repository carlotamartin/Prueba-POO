from Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

    def get_ruedas (self):
        return int(self.ruedas)