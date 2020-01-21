def calcular(x, y):
    """
    Essa calculadora, calcula alguma coisa.
    
    """
    x = x * 3
    y = x ** 2 + y
    return y
import pytest

class test_testando:
    def  test_calcular():
        assert calcular(3, 2) == 83
    
    def test_calculo():
        assert calcular(3, 2) == 84
