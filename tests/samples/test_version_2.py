import os
import sys 
import unittest
#import src.Viajes
#import src.Flights
from src.Viajes import Viajes
from src.Flights import Flights, Vuelos
from src.PaymentData import PaymentData
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
        y = PaymentData('MASTERCARD', 'Pepito', '4546')

        x.payment_V2(y)

        assert(x.payment_data.tipo_tarjeta == 'MASTERCARD')

   


Test_v2.test1(1)
Test_v2.test2(1)
Test_v2.test3(1)