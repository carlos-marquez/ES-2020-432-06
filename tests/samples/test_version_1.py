import os
import sys 
import unittest
#import src.Viajes
#import src.Flights
from src.Viajes import Viajes
from src.Flights import Flights
from unittest import mock
#import src.Bank
from src.Bank import Bank
sys.path.append(os.path.realpath('../../src'))


class Test_v1:
    def test_1(self):
        '''
        Dado un viaje con más de un viajero,
        el número de viajeros es el esperado
        '''
        
        x = Viajes(4, ['P1', 'P2', 'P3', 'P4'], [])
        num_esperado = x.funcion1(4, ['P1', 'P2', 'P3', 'P4'])
        assert num_esperado == True

    def test_2(self):
        '''
        Dado un viaje sin destinos, 
        la lista de destinos está vacía
        '''

        lista_destinos = []
        x = Viajes(4, ['P1', 'P2', 'P3', 'P4'], [])
        assert lista_destinos == x.num_destinos

    def test_3(self):
        '''
        Dado un viaje sin destinos,
        la lista de vuelos está vacía
        '''

        lista_vuelos = []
        x = Viajes(4, ['P1', 'P2', 'P3', 'P4'], [])
        assert lista_vuelos == x.num_destinos     

    def test_4(self):
        '''
        Dado un viaje sin destinos,
        el precio del viaje es cero
        '''
        precio_viaje = 0

        x = Viajes(4, ['P1', 'P2', 'P3', 'P4'], [])
        assert precio_viaje == len(x.num_destinos)
    
    def test_5(self):
        '''
        Dado un viaje, cuando se añaden destinos,
        la lista de destinos es la esperada
        '''
        llista_destinacions = ['A', 'BCN']
        
        vol_1 = Flights()
        vol_2 = Flights(destino = 'BCN')
        vols = [vol_1, vol_2]

        v = Viajes(llista_vols = vols)

        print('test 5 = ', llista_destinacions == v.llista_destinacions)
        assert llista_destinacions == v.llista_destinacions

    def test_6(self):
        '''
        Dado un viaje, cuando se añaden destinos, 
        la lista de vuelos es la esperada
        '''
        vol_1 = Flight()
        vol_2 = Flight(destinacio = 'BCN')
        vols = [vol_1, vol_2]

        v = Viatge(llista_vols = vols)

        print('test 6 = ', vols == v.llista_vols)
        assert vols == v.llista_vols


    def test_7(self):
        '''
        Dado un viaje, cuando se añaden destinos, 
        el precio del viaje es el esperado
        '''
        vol_1 = Flight()
        vol_2 = Flight(destinacio = 'BCN')
        vols = [vol_1, vol_2]

        v = Viatge(llista_vols = vols)
        preu_vol = v.preu_vol
        preu_total = len(vols) * preu_vol
        
        print('test 7 = ', preu_total == v.calculate_price())
        assert preu_total == v.calculate_price()

    def test_8(self):
        '''
        Dado un viaje con más de un viajero, 
        cuando se añaden destinos, el precio del viaje es el esperado
        '''
        vol_1 = Flight()
        vol_2 = Flight(destinacio = 'BCN')
        vols = [vol_1, vol_2]
        n_viatgers = 3

        v = Viatge(llista_viatgers = ['a', 'b','c'], llista_vols = vols)
        preu_vol = v.preu_vol
        preu_total = len(vols) * preu_vol * n_viatgers 
        
        print('test 8 = ', preu_total == v.calculate_price())
        assert preu_total == v.calculate_price()


    def test_9(self):
        '''
        Dado  un  viaje  con múltiples destinos  y 
        más  de  un  viajero,cuando  se  quitan destinos,
        la lista de destinos es la esperada
        '''
        vol_1 = Flight()
        vol_2 = Flights(destinacio = 'BCN')
        vols = [vol_1, vol_2]

        v = Viajes(llista_viatgers = ['a', 'b','c'], llista_vols = vols)
        v.delete_dest('A')

        print('test 9 = ', ['BCN'] == v.llista_destinacions)
        assert ['BCN'] == v.llista_destinacions
    
    def test_10(self):
        '''
        Dado  un  viaje  con múltiples destinos  y
        más  de  un  viajero,cuando  se  quitan destinos, 
        la lista de vuelos es la esperada
        '''
        vol_1 = Flight(destinacio = 'PR')
        vol_2 = Flight(destinacio = 'BCN')
        vols = [vol_1, vol_2]

        v = Viajes(llista_viatgers = ['a', 'b','c'], llista_vols = vols)
        v.delete_dest('PR')
        vols.remove(vol_1)

        print('test 10 = ', vols == v.llista_vols)
        assert vols == v.llista_vols
    
    def test_11(self):
        '''
        Dado  un  viaje  con múltiples destinos  y
        más  de  un  viajero,cuando  se  quitan destinos,
        el precio del viaje es el esperado
        '''
        vol_1 = Flight(destinacio = 'PR')
        vol_2 = Flight(destinacio = 'BCN')
        vols = [vol_1, vol_2]

        v = Viatge(llista_viatgers = ['a', 'b','c'], llista_vols = vols)
        v.delete_dest('PR')
        
        #1 Viajes* 100€ per Viajes* n_passatgers
        preu_total = 100 * 3

        print('test 11 = ', preu_total == v.calculate_price())
        assert preu_total == v.calculate_price()

#    def test_12(self):
#        '''
#        Dado  un  viaje  con múltiples destinos y
#        más  de  un  viajero,  cuando  el  pago
#        se realiza correctamente, se reporta que
#        la acción se ha realizado correctamente
#        '''
#        vol_1 = Flight(destinacio = 'PR')
#        vol_2 = Flight(destinacio = 'BCN')
#        vols = [vol_1, vol_2]
#
#        v = Viatge(llista_viatgers = ['a', 'b','c'], llista_vols = vols)    
#        @mock.patch('Bank')
#        mock = Mock()
#        mock.do_payment = Bank.do_payment
#        print('test 12 = ', preu_total == v.calculate_price())
#        assert preu_total == v.calculate_price()
#



 
 
 
Test_v1.test_1(1)
Test_v1.test_2(1)
Test_v1.test_3(1)
Test_v1.test_4(1)
Test_v1.test_5(1)
Test_v1.test_6(1)
Test_v1.test_7(1)
Test_v1.test_8(1)
Test_v1.test_9(1)
Test_v1.test_10(1)
Test_v1.test_11(1)
#Test_v1.test_12(1)
#Test_v1.test_13(1)



