"""Del AST a un numero.

Recorre el arbol de abajo hacia arriba: para evaluar una operacion hay que
evaluar primero sus dos lados.
"""
import operator
from .ast import Numero, OperacionBinaria
from .errores import ErrorDeEvaluacion

OPERACIONES = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

def evaluar(nodo):
    """Evalua un nodo del AST y regresa su valor."""
    if isinstance(nodo, Numero):
        return nodo.valor

    if isinstance(nodo, OperacionBinaria):
        izquierda = evaluar(nodo.izquierda)
        derecha = evaluar(nodo.derecha)

        operacion = OPERACIONES.get(nodo.operador)
        if operacion is None:
            raise ErrorDeEvaluacion(f"operador desconocido {nodo.operador!r}", 0)
        if nodo.operador == "/" and derecha == 0:
            raise ErrorDeEvaluacion("division entre cero", 0)
        return operacion(izquierda, derecha)

    raise ErrorDeEvaluacion(f"nodo desconocido: {nodo!r}", 0)
