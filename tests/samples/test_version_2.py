import os
import sys 
import unittest
#import src.Viajes
#import src.Flights
from src.Viajes import Viajes
from src.Flights import Flights, Vuelos

from unittest.mock import MagicMock
#from unittest import mock
#import src.Bank
from src.Bank import Bank
from src.User import User
sys.path.append(os.path.realpath('../../src'))

class Test_v2:
    def test1(self):
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        x = Viajes(lista_pasajeros = ['p1', 'p2', 'p3'], vuelos = aux_vuelo)
        x.payment('MASTERCARD', 'Pepito', '4546')

        assert(x.payment_data.tipo_tarjeta == 'MASTERCARD')

    def test2(self):
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        x = Viajes(lista_pasajeros = ['p1', 'p2', 'p3'], vuelos = aux_vuelo)
        


    def test3(self):
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        x = Viajes(lista_pasajeros = ['p1', 'p2', 'p3'], vuelos = aux_vuelo)

Test_v2.test1(1)
Test_v2.test2(1)
Test_v2.test3(1)