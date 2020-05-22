import os
import sys 
import unittest
from src.Viajes import Viajes
from src.Flights import Flights
from unittest import mock
from src.Bank import Bank
from src.PaymentData import PaymentData
sys.path.append(os.path.realpath('../../src'))
class test_1:
    #def test_error_pagament:
        #'''
        #Dado un viaje con múltiples destinos y más 
        #de un viajero, cuando se produce un error al 
        #realizar el pago, se reporta que la acción 
        #no se ha podido realizar
        #''' 
        #error = PaymentData('VISA','',87296785,352,582)
        #resultado_esperado = Error_pago('VISA','',87296785,352,582)
        #assert resultado_esperado == True
        #print('La acción no se ha realizado correctamente. Pago incorrecto')
    def test_facturacion_correcta:
        '''Dado un viaje con múltiples destinos y más de un viajero, cuando los datos de
        facturación introducidos por el usuario son correctos, se reporta que los datos
        son correctos'''

        
