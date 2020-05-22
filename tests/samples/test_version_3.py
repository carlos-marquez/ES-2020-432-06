import os
import sys 
import unittest
#import src.Viajes
#import src.Flights
from src.Viajes import Viajes
from src.Flights import Flights, Vuelos
from src.Cars import Cars, Vehiculo
from src.Hotels import Hotels, Alojamiento

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
        aux1 = Vehiculo()
        aux2 = Vehiculo()
        aux_coches = [aux1, aux2]
        n_viajeros = 3

        x = Viajes(lista_pasajeros = ['p1', 'p2','p3'], coches = aux_coches)       
        x.eliminar_coches(aux1)
        precio = x.precio
        precio_total =  precio * n_viajeros 

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
       
        
 
Test_v3.test_1(1)
Test_v3.test_2(1)
Test_v3.test_3(1)
#Test_v3.test_4(1)
#Test_v3.test_5(1)
#Test_v3.test_6(1)
#Test_v3.test_7(1)
#Test_v3.test_8(1)

