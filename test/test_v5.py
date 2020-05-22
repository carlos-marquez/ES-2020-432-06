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

class test_v5:

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

    def test_3(self):
        user = User('Lola Mento', '11334445X', '08988', '666333999', 'lola@gmail.com')
        
        datos=user.datos_completos()
        user.datos_completos = MagicMock(return_value=False)

        assert datos == user.datos_completos()

    #def test_4(self): FET!

test_v5.test_1(1)
test_v5.test_2(1)
test_v5.test_3(1)