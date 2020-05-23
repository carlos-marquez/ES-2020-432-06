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

class Test_v4:
#reintentar pago cuando hay error
    def test_1(self):
        destinos = ['BCN', 'NYC']
        viajeros = 2
        
#reintentar y pago correcto 
    def test_2(self):
        destinos = ['BCN', 'NYC', 'LA']
        viajeros = 2
#numero maximo de reintentos realizar pago, no se puede realizar accion
    def test_3(self):
        destinos = ['BCN', 'NYC', 'LA']
        viajeros = 2 
#error confirmar vuelos, reintenta confirmacion    
    def test_4(self):
        destinos = ['BCN', 'NYC', 'LA']
        viajeros = 2 
#confirmación ed vuelos correcta en un reintento
    def test_5(self):
        destinos = ['BCN', 'NYC', 'LA']
        viajeros = 2
#numero maximo de reintentos confirmar vuelo
    def test_6(self):
        destinos = ['BCN', 'NYC', 'LA']
        viajeros = 2






    




    



