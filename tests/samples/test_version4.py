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

class Test_v4:
#reintentar pago cuando hay error
    def test_1(self):
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        y = PaymentData('MASTERCARD', 'Pepito', '4546', '50')
        x = Viajes(user = User, lista_pasajeros = ['p1', 'p2', 'p3'], vuelos = aux_vuelo)
        aux = User('Pol', '12345678J', '08390', '123456789', 'user@uab.cat')

        fallo = x.payment_V3(y, 1,1,0)
        i = Bank()
        i.do_payment = MagicMock(return_value = False)

        acierto_reintento = x.payment_V3(y,0,0,1)
        j = Bank()
        j.do_payment = MagicMock(return_value = True)

        assert i.do_payment(aux, y) == fallo
        assert j.do_payment(aux, y) == acierto_reintento
        
       
        
#reintentar y pago correcto 
    def test_2(self):
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        y = PaymentData('MASTERCARD', 'Pepito', '4546', '50')
        x = Viajes(user = User, lista_pasajeros = ['p1', 'p2', 'p3'], vuelos = aux_vuelo)
        aux = User('Pol', '12345678J', '08390', '123456789', 'user@uab.cat')

        fallo = x.payment_V3(y, 1,1,0)
        i = Bank()
        i.do_payment = MagicMock(return_value = False)

        acierto_reintento = x.payment_V3(y,0,0,1)
        j = Bank()

        #assert i.do_payment(aux, y) == fallo
        assert j.do_payment(aux, y) == acierto_reintento
        
#numero maximo de reintentos realizar pago, no se puede realizar accion
    def test_3(self):
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        y = PaymentData('MASTERCARD', 'Pepito', '4546', '50')
        x = Viajes(user = User, lista_pasajeros = ['p1', 'p2', 'p3'], vuelos = aux_vuelo)
        aux = User('Pol', '12345678J', '08390', '123456789', 'user@uab.cat')

        fallo = x.payment_V3(y, 1,1,0)
        i = Bank()
        i.do_payment = MagicMock(return_value = False)

        error_max = x.payment_V3(y,0,0,3)
        j = Bank()
        j.do_payment = MagicMock(return_value = False)

        assert j.do_payment(aux, y) == error_max