def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multi(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Impossível dividir por 0"
    return a / b

# Testes com pytest
def test_soma_positivos():
    """Testa soma com números positivos"""
    assert soma(2, 3) == 5

def test_subtracao_negativos():
    """Testa subtração com números negativos"""
    assert subtracao(5, 8) == -3

def test_multiplicacao_por_zero():
    """Testa multiplicação por zero"""
    assert multi(7, 0) == 0

def test_divisao_normal():
    """Testa divisão normal"""
    assert divisao(10, 2) == 5

def test_divisao_por_zero():
    """Testa divisão por zero"""
    assert divisao(5, 0) == "Erro! Impossível dividir por 0"

def test_soma_decimais():
    """Testa soma com números decimais"""
    assert soma(1.5, 2.5) == 4.0

def test_subtracao_resultado_zero():
    """Testa subtração com resultado zero"""
    assert subtracao(5, 5) == 0