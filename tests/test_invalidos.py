'Pruebas de entradas inválidas'
import pytest
from mini_interprete.cli import interpretar
from mini_interprete.errores import ErrorDeSintaxis


def test_entrada_vacia():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("")

def test_con_letras():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("2 + Laboon")

def test_sin_operador():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("2 9")

def test_dos_operadores_seguidos():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("2 +* 9")

def test_parentesis_extra():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("9)")

def test_sin_segundo_termino():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("9 +")

def test_negativo():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("-9")

def test_parentesis_sin_cerrar():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("(2 + 9")

def test_simbolo_desconocido():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("2 + 9 &")