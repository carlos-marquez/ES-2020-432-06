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

    def test2(self):
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        y = PaymentData('MASTERCARD', 'Pepito', '4546')
        x = Viajes(user = User, lista_pasajeros = ['p1', 'p2', 'p3'], vuelos = aux_vuelo)
        aux = User('Pol', '12345678J', '08390', '123456789', 'user@uab.cat')

        fallo = x.payment_V2(y, 1)
        Bank.do_payment = MagicMock(return_value = False)
        i = Bank()

        assert i.do_payment(aux, y) == fallo
        

    def test3(self):
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        x = Viajes(user = User, lista_pasajeros = ['p1', 'p2', 'p3'], vuelos = aux_vuelo)


Test_v2.test1(1)
Test_v2.test2(1)
Test_v2.test3(1)