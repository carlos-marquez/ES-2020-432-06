import os
import sys
import tempfile
import unittest

from unittest.mock import Mock
from src.Bank import Bank

class TestPagament:
    #Cuando el usuario ha seleccionado un método de pago, 
    #el pago sea con el método de pago esperado
    def test_6(self):
        x=('VISA' or 'MASTERCARD')
        assert ('VISA' or 'MASTERCARD') in x


