"""Pruebas del evaluador: del AST a un numero."""
import pytest #agregado
import pytest #agregado
from mini_interprete.errores import ErrorDeSintaxis #agregado
from mini_interprete.cli import interpretar
from mini_interprete.errores import ErrorDeEvaluacion #agregado


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

#Agregado
def test_mismo_nivel_suma():
    assert interpretar ("10 + 4 + 1") == 15.0

def test_mismo_nivel_resta():
    assert interpretar ("10 - 3 - 2") == 5.0

def test_mismo_nivel_division():
    assert interpretar ("8 / 4 / 2") == 1.0

#Agregado
def test_mismo_nivel_multiplicacion():
    assert interpretar ("2 * 4 * 1") == 8.0

def test_mismo_nivel_2():
    assert interpretar("8 / 2 * 2") == 8.0

def test_mismo_nivel_3():
    assert interpretar("10 - 3 + 2") == 9.0

#Agregado
def test_division_entre_cero():
    with pytest.raises(ErrorDeEvaluacion):
        interpretar("10 / 0")

#Agregado
def test_division_entre_cero_reporta_posicion():
    with pytest.raises(ErrorDeEvaluacion) as info:
        interpretar("10 / 0")
    assert "posicion" in str(info.value)

#Agregado
def test_parentesis_sin_cerrar():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("( 3 + 4")

#Agregado
def test_signo_al_principio():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("-3 + 4")

#Agregado
def test_suma_con_decimales():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("3.2 + 4.0")

#Agregado
def test_numeros_con_espacios():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("3 4")

#Agregado
@pytest.mark.parametrize("entrada", ["3#4", "3$4", "3!4", "3&4", "3@4"])
def test_simbolos_invalidos(entrada):
    with pytest.raises(ErrorDeSintaxis):
        interpretar(entrada)

#Agregado
def test_mismo_nivel_resta():
    assert interpretar ("0007-002") == 5.0


def test_precedencia_sin_parentesis():
    assert interpretar("3 + 4 * 2") == 11


def test_precedencia_con_parentesis():
    assert interpretar("(3 + 4) * 2") == 14
