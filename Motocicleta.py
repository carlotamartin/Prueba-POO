from Bicicleta import Bicicleta


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__( color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Bicicleta.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

    def get_ruedas (self):
        return int(self.ruedas)