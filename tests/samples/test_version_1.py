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


class Test_v1:
    def test_1(self):
       
        aux = ['p1','p2']
        pasajeros = 2        
        x = Viajes(lista_pasajeros = aux)

        assert pasajeros == x.n_pasajeros

    def test_2(self):
        
        aux = []
        x = Viajes(vuelos=aux)
       
        assert x.lista_destinos == x.vuelos

    def test_3(self):
      
        vuelos = []
        x = Viajes(vuelos)

        assert x.calcular_precio() == 0    

    def test_4(self):
       
        vuelos = []
        x = Viajes(vuelos)

        assert 0 == x.calcular_precio()               
    
    def test_5(self):
       
        lista_dest = ['BCN', 'NYC']
        aux1 = Vuelos()
        aux2 = Vuelos(destino = 'NYC')
        aux_vuelos = [aux1, aux2]
        x = Viajes(vuelos = aux_vuelos)

        assert lista_dest == x.lista_destinos

    def test_6(self):

        aux1 = Vuelos()
        aux2 = Vuelos(destino = 'NYC')
        aux_vuelo = [aux1, aux2]

        x = Viajes(vuelos = aux_vuelo)

        assert aux_vuelo == x.vuelos

    
    def test_7(self):
        
        aux1 = Vuelos()
        aux2 = Vuelos(destino = 'NYC')
        aux_vuelo = [aux1, aux2]

        x = Viajes(vuelos = aux_vuelo, lista_pasajeros = ['p1'])
        #precio = x.precio
        precio_total = len(aux_vuelo) * x.precio * len(x.lista_pasajeros)
        
        assert precio_total == x.calcular_precio()
    
    def test_8(self):
        
        aux1 = Vuelos()
        aux2 = Vuelos(destino = 'NYC')
        aux_vuelo = [aux1, aux2]
        n_viajeros = 3

        x = Viajes(lista_pasajeros = ['p1', 'p2','p3'], vuelos = aux_vuelo)
        precio = x.precio
        precio_total = len(aux_vuelo) * precio * n_viajeros 
        
        assert precio_total == x.calcular_precio()


    def test_9(self):
        
        aux1 = Vuelos()
        aux2 = Vuelos(destino = 'NYC')
        aux_vuelo = [aux1, aux2]

        x = Viajes(lista_pasajeros = ['p1', 'p2','p3'], vuelos = aux_vuelo)       
        x.eliminar_destino('BCN') 

        assert ['NYC'] == x.lista_destinos
     
    def test_10(self):
        
        aux1 = Vuelos(destino = 'BCN') 
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        x = Viajes(lista_pasajeros = ['p1', 'p2','p3'], vuelos = aux_vuelo)
        x.eliminar_destino('BCN')
        aux_vuelo.remove(aux1)

        assert aux_vuelo == x.vuelos
    
    def test_11(self):
        
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        x = Viajes(lista_pasajeros = ['p1', 'p2','p3'], vuelos = aux_vuelo)
        x.eliminar_destino('BCN')

        precio_total = 50 * 3

        assert precio_total == x.calcular_precio()

    def test_12(self):
        
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA')
        aux_vuelo = [aux1, aux2]

        payment_data = ['VISA', 'Pepito Los Palotes', '8520'] 
        user = User('Pepito Los Palotes', '12345678P', '08390','678942316', 'pepe@e-champus.uab.cat')

        x = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3'], vuelos = aux_vuelo)

        datos = x.payment_V1(payment_data[0], payment_data[1], payment_data[2])
        x.payment = MagicMock(return_value=True)

        assert datos == x.payment() 

    def test_13(self):  
        
        aux1 = Vuelos(destino = 'BCN')
        aux2 = Vuelos(destino = 'ITA') 
        aux_vuelo = [aux1, aux2]

        user = User('Pepito Los Palotes', '12345678P', '08390','678942316', 'pepe@e-champus.uab.cat')

        x = Viajes(user = user, lista_pasajeros = ['p1', 'p2','p3'], vuelos = aux_vuelo)

        datos = x.anadir_reserva()
        x.anadir_reserva = MagicMock(return_value=True)

        assert datos == x.anadir_reserva()



 
 
 
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
Test_v1.test_12(1)
Test_v1.test_13(1)
