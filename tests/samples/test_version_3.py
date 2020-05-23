import os
import sys 
import unittest
#import src.Viajes
#import src.Flights
from src.Viajes import Viajes
from src.Flights import Flights, Vuelos
from src.Cars import Cars, Vehiculo
from src.Hotels import Hotels, Alojamiento
from src.Rentalcars import Rentalcars
from src.Booking import Booking

from unittest.mock import MagicMock
#from unittest import mock
#import src.Bank
from src.Bank import Bank
from src.User import User
sys.path.append(os.path.realpath('../../src'))


class Test_v3:
    def test_1(self):
        aux1 = Vehiculo()
        aux2 = Vehiculo()
        aux_coche = [aux1, aux2]
        n_viajeros = 3

        x = Viajes(lista_pasajeros = ['p1', 'p2','p3'], coches = aux_coche)
        precio = x.precio
        precio_total = len(aux_coche) * precio * n_viajeros 
        
        assert precio_total == x.calcular_precio()
    
    def test_2(self):
        aux1 = Cars(marca = 'BMW')
        aux2 = Cars()
        aux_coches = [aux1, aux2]
        n_viajeros = 3

        x = Viajes(lista_pasajeros = ['p1', 'p2','p3'], coches = aux_coches)       
        x.eliminar_coches('BMW')
        precio = x.precio
        precio_total = len(aux_coches) * precio * n_viajeros 

        assert precio_total == x.calcular_precio()
    
    def test_3(self):
        aux1 = Alojamiento()
        aux2 = Alojamiento()
        aux_alojamiento = [aux1, aux2]
        n_viajeros = 3

        x = Viajes(lista_pasajeros = ['p1', 'p2','p3'], hoteles = aux_alojamiento)
        precio = x.precio
        precio_total = len(aux_alojamiento) * precio * n_viajeros 
        
        assert precio_total == x.calcular_precio()

    def test_4(self):
        aux1 = Hotels(nombre_hotel = 'Vela') 
        aux2 = Hotels()
        aux_alojamiento = [aux1, aux2]
        n_viajeros = 3

        x = Viajes(lista_pasajeros = ['p1', 'p2','p3'], hoteles = aux_alojamiento)       
        x.eliminar_alojamiento('Vela')
        precio = x.precio
        precio_total =   precio * n_viajeros
        precio_total = len(aux_alojamiento) * precio * n_viajeros

        assert precio_total == x.calcular_precio()
    
    def test_5(self):
        
        aux1 = Cars(marca = 'BMW')
        aux2 = Cars()
        aux_coches = [aux1, aux2]

        user = User('Pepito Los Palotes', '12345678P', '08390','678942316', 'pepe@e-champus.uab.cat')

        x = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3'], coches = aux_coches)

        datos = x.anadir_coche()
        x.anadir_coche = MagicMock(return_value=True)

        assert datos == x.anadir_coche()
    
    def test_6(self):
        aux1 = Cars(marca = 'BMW')
        aux2 = Cars()
        aux_coches = [aux1, aux2]

        x = Viajes(user = User, lista_pasajeros = ['p1', 'p2', 'p3'], coches = aux_coches)
        aux = User('Pepito Los Palotes', '12345678P', '08390','678942316', 'pepe@e-champus.uab.cat')

        fallo = x.anadir_coche(1)
        rentalcars = Rentalcars()
        rentalcars.confirm_reserve = MagicMock(return_value = False)

        assert rentalcars.confirm_reserve(aux, aux_coches) == fallo

    def test_7(self):
        
        aux1 = Hotels(nombre_hotel = 'Vela')
        aux2 = Hotels()
        aux_alojamiento = [aux1, aux2]

        user = User('Pepito Los Palotes', '12345678P', '08390','678942316', 'pepe@e-champus.uab.cat')

        x = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3'], hoteles = aux_alojamiento)

        datos = x.anadir_alojamiento() 
        x.anadir_alojamiento = MagicMock(return_value=True)

        assert datos == x.anadir_alojamiento()

    def test_8(self): 
        aux1 = Hotels(nombre_hotel = 'Vela')
        aux2 = Hotels()
        aux_alojamiento = [aux1, aux2]  

        x = Viajes(user = User, lista_pasajeros = ['p1', 'p2', 'p3'], hoteles = aux_alojamiento)
        aux = User('Pepito Los Palotes', '12345678P', '08390','678942316', 'pepe@e-champus.uab.cat')

        fallo = x.anadir_alojamiento(1) 
        book = Booking()
        book.confirm_reserve = MagicMock(return_value = False)

        assert book.confirm_reserve(aux, aux_alojamiento) == fallo
       
        
 
Test_v3.test_1(1)
Test_v3.test_2(1)  
Test_v3.test_3(1)
Test_v3.test_4(1)
Test_v3.test_5(1)
Test_v3.test_6(1)
Test_v3.test_7(1)
Test_v3.test_8(1)

