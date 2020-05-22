import os
import sys
import tempfile
import unittest
from src.Viajes import Viajes
from src.Flights import Flights

from unittest.mock import MagicMock
from src.Bank import Bank
from src.User import User

sys.path.append(os.path.realpath('../../src'))

class test_todos:

    '''Dado un viaje con múltiples destinos y más de un viajero, cuando los datos de
    facturación introducidos por el usuario son correctos, se reporta que los datos
    son correctos'''

    def test_1(self):
        user = User('Elena Nito', '11223345X', '08088', '666992332', 'elena@gmail.com')
        
        datos=user.comprueba_datos()
        user.comprueba_datos = MagicMock(return_value=False)

        assert datos == user.comprueba_datos()

    def test_2(self):
        user = User('Elvis Tec', '11122245X', '08688', '666999333', 'elvis@gmail.com')
        
        datos=user.comprueba_datos()
        user.comprueba_datos = MagicMock(return_value=True)

        assert datos == user.comprueba_datos()