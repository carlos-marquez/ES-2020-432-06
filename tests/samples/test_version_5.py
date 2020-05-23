import os
import sys 
import tempfile
import unittest

from src.Viajes import Viajes
from src.Flights import Flights, Vuelos

from unittest.mock import MagicMock

from src.Bank import Bank
from src.User import User
sys.path.append(os.path.realpath('../../src'))

class Test_v5:
    def test_1(self): 
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]
        
        Viajes(lista_pasajeros = ['p1', 'p2','p3'], vuelos = aux_vuelo)
        
        user = User('Elena Nito', '11223345X', '08088', '666992332', 'elena@gmail.com')
        
        datos=user.comprueba_datos('Elena Nito', '11223345X', '08088', '666992332', 'elena@gmail.com')
        datos2=user.datos_completos('Elena Nito', '11223345X', '08088', '666992332', 'elena@gmail.com')

        assert datos == datos2

    def test_2(self):
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]
        
        Viajes(lista_pasajeros = ['p1', 'p2','p3'], vuelos = aux_vuelo)
        user = User('1234', 'Elvis Moro', '08688', '666999333', 'elvis@gmail.com')
        
        datos=user.comprueba_datos('1234', 'Elvis Moro', '08688', '666999333', 'elvis@gmail.com')
        datos2=user.datos_completos('1234', 'Elvis Moro', '08688', '666999333', 'elvis@gmail.com')

        assert datos != datos2

    def test_3(self):
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA') 
        aux_vuelo = [aux1, aux2]
        
        Viajes(lista_pasajeros = ['p1', 'p2','p3'], vuelos = aux_vuelo)
        user = User('Lola Mento', '11334445X', '08988', '666333999', 'lola@gmail.com')
        
        datos=user.comprueba_datos('Lola Mento', '11334445X', '08988', '666333999', 'lola@gmail.com')
        datos2=user.datos_completos('Lola Mento', '11334445X', '08988', '666333999', 'lola@gmail.com')
        
        assert datos == datos2

        if datos == datos2:
            user.factura('Lola Mento', '11334445X', '08988', '666333999', 'lola@gmail.com')


    def test_4(self):
        
        destino1 = Vuelos(destino='BCN')
        destino2 = Vuelos(destino='ITA')

        vuelo_destinaciones = [destino1,destino2] 
        
        n_viajeros = 5
        datos = [n_viajeros,'57382dh2','Citroen','BCN',7]
        user = User('Dolores Fuertes De Barriga','12345678B','08192','679392698','d-fuertes@gmail.com')
       
        coche = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3','p4','p5'], coches = vuelo_destinaciones)

        x = coche.confirmacion_coches(datos[0],datos[1],datos[2],datos[3],datos[4])
        if x == -1: 
            destino1 = Vuelos(destino='BCN')
            destino2 = Vuelos(destino='ITA')

            vuelo_destinaciones = [destino1,destino2]
            n_viajeros = 5
            datos = [n_viajeros,'57382dh2','Citroen','BCN',7]
            user = User('Dolores Fuertes De Barriga','12345678B','08192','679392698','d-fuertes@gmail.com')

            coche = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3','p4','p5'], coches = vuelo_destinaciones)

            x = coche.confirmacion_coches(datos[0],datos[1],datos[2],datos[3],datos[4])
           
        assert x == -1
    
    def test_5(self):
        destino1 = Vuelos(destino='BCN')
        destino2 = Vuelos(destino='ITA')

        vuelo_destinaciones = [destino1,destino2]
        n_viajeros = 5
        datos = [n_viajeros,'57382dh2','Citroen','BCN',7]
        user = User('Dolores Fuertes De Barriga','12345678B','08192','679392698','d-fuertes@gmail.com')

        coche = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3','p4','p5'], coches = vuelo_destinaciones)

        x = coche.confirmacion_coches(datos[0],datos[1],datos[2],datos[3],datos[4])
        if x == -1: 
            destino1 = Vuelos(destino='BCN')
            destino2 = Vuelos(destino='ITA')

            vuelo_destinaciones = [destino1,destino2]
            n_viajeros = 4
            datos = [n_viajeros,'57382dh2','Citroen','BCN',7]
            user = User('Dolores Fuertes De Barriga','12345678B','08192','679392698','d-fuertes@gmail.com')

            coche = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3','p4'], coches = vuelo_destinaciones)

            x = coche.confirmacion_coches(datos[0],datos[1],datos[2],datos[3],datos[4])

        assert x == coche.confirmacion_coches(datos[0],datos[1],datos[2],datos[3],datos[4])
    
    def test_6(self):

        destino1 = Vuelos(destino='BCN')
        destino2 = Vuelos(destino='ITA')

        vuelo_destinaciones = [destino1,destino2]
        n_viajeros = 5
        datos = [n_viajeros,'57382dh2','Citroen','BCN',7]
        user = User('Dolores Fuertes De Barriga','12345678B','08192','679392698','d-fuertes@gmail.com')

        coche = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3','p4','p5'], coches = vuelo_destinaciones)

        x = coche.confirmacion_coches(datos[0],datos[1],datos[2],datos[3],datos[4])
        contador = 1
        while contador < 4 and x == -1: #3 reintentos + 1 intento original. 
            destino1 = Vuelos(destino='BCN')
            destino2 = Vuelos(destino='ITA')

            vuelo_destinaciones = [destino1,destino2]
            n_viajeros = 5
            datos = [n_viajeros,'57382dh2','Citroen','BCN',7]
            user = User('Dolores Fuertes De Barriga','12345678B','08192','679392698','d-fuertes@gmail.com')

            coche = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3','p4','p5'], coches = vuelo_destinaciones)

            x = coche.confirmacion_coches(datos[0],datos[1],datos[2],datos[3],datos[4])
            if x == -1:
                contador = contador + 1
        assert x == -1
    
    def test_7(self):
        destino1 = Vuelos(destino='BCN')
        destino2 = Vuelos(destino='ITA') 

        vuelo_destinaciones = [destino1,destino2]
        n_viajeros = 5
        datos = ['748237','Hotel y',n_viajeros,1,7]
        user = User('Dolores Fuertes De Barriga','12345678B','08192','679392698','d-fuertes@gmail.com')

        hotel = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3','p4','p5'], hoteles = vuelo_destinaciones)

        x = hotel.confirmacion_alojamiento(datos[0],datos[1],datos[2],datos[3],datos[4])
        if x == -1: 
            destino1 = Vuelos(destino='BCN')
            destino2 = Vuelos(destino='ITA')

            vuelo_destinaciones = [destino1,destino2]
            n_viajeros = 5
            datos = ['748237','Hotel y',n_viajeros,1,7]
            user = User('Dolores Fuertes De Barriga','12345678B','08192','679392698','d-fuertes@gmail.com')

            hotel = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3','p4','p5'], hoteles = vuelo_destinaciones)

            x = hotel.confirmacion_alojamiento(datos[0],datos[1],datos[2],datos[3],datos[4])
           
        assert x == -1
    
    def test_8(self):
        destino1 = Vuelos(destino='BCN')
        destino2 = Vuelos(destino='ITA')

        vuelo_destinaciones = [destino1,destino2]
        n_viajeros = 5
        datos = ['748237','Hotel y',n_viajeros,1,7]
        user = User('Dolores Fuertes De Barriga','12345678B','08192','679392698','d-fuertes@gmail.com')

        hotel = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3','p4','p5'], hoteles = vuelo_destinaciones)

        x = hotel.confirmacion_alojamiento(datos[0],datos[1],datos[2],datos[3],datos[4])
        if x == -1: 
            destino1 = Vuelos(destino='BCN')
            destino2 = Vuelos(destino='ITA')

            vuelo_destinaciones = [destino1,destino2]
            n_viajeros = 6
            datos = ['748237','Hotel y',n_viajeros,2,7]
            user = User('Dolores Fuertes De Barriga','12345678B','08192','679392698','d-fuertes@gmail.com')

            hotel = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3','p4','p5'], hoteles = vuelo_destinaciones)

            x = hotel.confirmacion_alojamiento(datos[0],datos[1],datos[2],datos[3],datos[4])
           
        assert x == hotel.confirmacion_alojamiento(datos[0],datos[1],datos[2],datos[3],datos[4])

    def test_9(self):
        destino1 = Vuelos(destino='BCN')
        destino2 = Vuelos(destino='ITA')

        vuelo_destinaciones = [destino1,destino2]
        n_viajeros = 5
        datos = ['748237','Hotel y',n_viajeros,1,7]
        user = User('Dolores Fuertes De Barriga','12345678B','08192','679392698','d-fuertes@gmail.com')

        hotel = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3','p4','p5'], hoteles = vuelo_destinaciones)

        x = hotel.confirmacion_alojamiento(datos[0],datos[1],datos[2],datos[3],datos[4])
        limite = 1
        while x == -1 and limite < 4:
            destino1 = Vuelos(destino='BCN')
            destino2 = Vuelos(destino='ITA')

            vuelo_destinaciones = [destino1,destino2]
            n_viajeros = 5
            datos = ['748237','Hotel y',n_viajeros,1,7]
            user = User('Dolores Fuertes De Barriga','12345678B','08192','679392698','d-fuertes@gmail.com')

            hotel = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3','p4','p5'], hoteles = vuelo_destinaciones)

            x = hotel.confirmacion_alojamiento(datos[0],datos[1],datos[2],datos[3],datos[4])
            if x == -1:
                limite = limite + 1 
           
        assert x == -1

Test_v5.test_1(1)
Test_v5.test_2(1)
Test_v5.test_3(1)  
Test_v5.test_4(1) 
Test_v5.test_5(1)
Test_v5.test_6(1)
Test_v5.test_7(1)
Test_v5.test_8(1)
Test_v5.test_9(1)
   