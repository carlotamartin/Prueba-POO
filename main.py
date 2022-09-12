class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )

    def get_ruedas (self):
        return int(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

    def get_ruedas (self):
        return int(self.ruedas)

#Creamos la clase Camioneta que hereda de coche

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return Coche.__str__(self) + ", {} kg".format(self.carga)

    def get_ruedas (self):
        return int(self.ruedas)

#Creamos la clase Bicicleta que hereda de Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__( color, ruedas)
        if self.ruedas > 8:
            self.tipo = 'deportivo'
        else:
            self.tipo = 'urbano'
    def __str__(self):
        return Vehiculo.__str__(self) + ", es de tipo {}".format(self.tipo)

    def get_ruedas (self):
        return int(self.ruedas)



#Creamos la clase Motocicleta que hereda de Bicicleta
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__( color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Bicicleta.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

    def get_ruedas (self):
        return int(self.ruedas)


c = Coche("azul", 4, 150, 1200)
f = Coche ('rojo', 5, 300, 1400)
j= Bicicleta('azul', 2, 20)
h = Motocicleta('azul', 4, 5, 100, 200)



#Creamos el método catalogar
def catalogar(lista):
    for i in lista:
        print (str(type(i).__name__ )+ ' = '+ str(i) )

lista = [c, f, j, h]

catalogar(lista)
print('PARTE DOS')
def catalogar_2 (lista, ruedas):
    j = 0
    for i in lista:
        if i.get_ruedas() == int(ruedas):
            j +=1
            print (str(type(i).__name__ )+ ' = '+ str(i) )
    print('Se han encontrado {} vehículos con {} ruedas'.format(j, ruedas))

catalogar_2 (lista, 4)

