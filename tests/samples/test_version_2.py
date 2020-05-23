import os
import sys 
import unittest
<<<<<<< HEAD
#import src.Viajes
=======
#import src.Viajes 
>>>>>>> 22c15ac44668516671e5b566da9509be93e5008e
#import src.Flights
from src.Viajes import Viajes
from src.Flights import Flights, Vuelos
from src.PaymentData import PaymentData
from src.Skyscanner import Skyscanner
<<<<<<< HEAD
from unittest.mock import MagicMock
=======
from unittest.mock import MagicMock 
>>>>>>> 22c15ac44668516671e5b566da9509be93e5008e
#from unittest import mock
#import src.Bank
from src.Bank import Bank
from src.User import User
sys.path.append(os.path.realpath('../../src'))

<<<<<<< HEAD
class Test_v2:
=======
class Test_v2:  
>>>>>>> 22c15ac44668516671e5b566da9509be93e5008e
    def test1(self):
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        x = Viajes(lista_pasajeros = ['p1', 'p2', 'p3'], vuelos = aux_vuelo)
        y = PaymentData('MASTERCARD', 'Pepito', '4546', '50')

        x.payment_V2(y)

        assert(x.payment_data.tipo_tarjeta == 'MASTERCARD')

    def test2(self):
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        y = PaymentData('MASTERCARD', 'Pepito', '4546', '50')
        x = Viajes(user = User, lista_pasajeros = ['p1', 'p2', 'p3'], vuelos = aux_vuelo)
        aux = User('Pol', '12345678J', '08390', '123456789', 'user@uab.cat')

        fallo = x.payment_V2(y, 1)
        Bank.do_payment = MagicMock(return_value = False)
        i = Bank()

<<<<<<< HEAD
        assert i.do_payment(aux, y) == fallo
=======
        assert i.do_payment(aux, y) == fallo 
>>>>>>> 22c15ac44668516671e5b566da9509be93e5008e
        

    def test3(self):
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        x = Viajes(user = User, lista_pasajeros = ['p1', 'p2', 'p3'], vuelos = aux_vuelo)
        aux = User('Pol', '12345678J', '08390', '123456789', 'user@uab.cat')

        fallo = x.anadir_reserva(1)
        sky = Skyscanner()
        sky.confirm_reserve = MagicMock(return_value = False)

        assert sky.confirm_reserve(aux, aux_vuelo) == fallo


<<<<<<< HEAD
Test_v2.test1(1)
Test_v2.test2(1)
=======
Test_v2.test1(1)  
Test_v2.test2(1) 
>>>>>>> 22c15ac44668516671e5b566da9509be93e5008e
Test_v2.test3(1)