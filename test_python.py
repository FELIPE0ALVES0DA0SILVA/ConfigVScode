import pytest

def calcular(x, y):
    """
    Essa calculadora, calcula alguma coisa.
    
    """
    x = x * 3
    y = x ** 2 + y
    return y

class Test_testando:

    def  test_calcular(self):
        assert calcular(3, 2) == 83
    def test_calculo(self):
        assert calcular(3, 2) == 83
