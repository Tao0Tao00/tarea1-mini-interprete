"""Pruebas del evaluador: del AST a un numero."""
import pytest
from mini_interprete.cli import interpretar
from mini_interprete.errores import ErrorDeEvaluacion 


def test_suma():
    assert interpretar("3 + 4") == 7


def test_resta():
    assert interpretar("10 - 3") == 7


def test_multiplicacion():
    assert interpretar("6 * 7") == 42


def test_division():
    assert interpretar("10 / 2") == 5
#Caso normal

def test_diferentes_niveles1():
    assert interpretar ("8 - 6 / 2") == 5.0

def test_diferentes_niveles2():
    assert interpretar ("8 + 6 * 2") == 20.0

def test_multiplicacion_antes_que_suma():
    assert interpretar ("3 * 3 + 2") == 11.0

def test_division_antes_que_resta():
    assert interpretar ("8 / 2 - 3") == 1.0

#Caso frontera
def test_division_entre_cero():
    with pytest.raises(ErrorDeEvaluacion):
        interpretar("10 / 0")

def test_precedencia_sin_parentesis():
    assert interpretar("3 + 4 * 2") == 11


def test_precedencia_con_parentesis():
    assert interpretar("(3 + 4) * 2") == 14
