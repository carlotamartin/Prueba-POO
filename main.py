from Camioneta import Camioneta
from Motocicleta import Motocicleta
from Coche import Coche
from Bicicleta import Bicicleta
from Vehiculo import Vehiculo

#Creamos el método catalogar
def catalogar(lista):
    for i in lista:
        print (str(type(i).__name__ )+ ' = '+ str(i) )


#Creamos el segundo método de catalogar
def catalogar_2 (lista, ruedas):
    j = 0
    for i in lista:
        if i.get_ruedas() == int(ruedas):
            j +=1
            print (str(type(i).__name__ )+ ' = '+ str(i) )
    print('Se han encontrado {} vehículos con {} ruedas'.format(j, ruedas))


def main():
    #Creamos los distintos vehículos
    c = Coche("azul", 4, 150, 1200)
    f = Coche ('rojo', 5, 300, 1400)
    j= Bicicleta('azul', 2, 2)
    h = Motocicleta('azul', 4, 5, 100, 200)
    a = Camioneta('azul', 6, 100, 100, 3000)

    #Creamos la lista de vehículos
    lista = [c, f, j, h, a]

    catalogar(lista)

    print ('\n')
    print('PARTE DOS')

    print ('\n')

    catalogar_2 (lista, 4)


if __name__ == '__main__':
    main()







