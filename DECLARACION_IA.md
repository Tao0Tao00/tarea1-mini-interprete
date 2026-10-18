# Declaración de uso de Inteligencia Artificial

**Actividad:**
**Integrantes:**
**Fecha:**

> Esta declaración es obligatoria en toda tarea, práctica y en el proyecto final.
> **No da ni quita puntos**: es un reporte adicional que se revisa aparte y se
> devuelve con comentarios. **No se evalúa cuánta IA usaron**, sino si pueden
> dar cuenta de lo que entregaron.

---

## 0. ¿Se usó IA en esta actividad?

- [ ] **No.** Firmen la última sección y terminen. Con eso queda completa.
- [X] **Sí.** Contesten los cinco puntos.

---

## 1. Herramienta(s) utilizada(s)

| Herramienta | Versión o modelo, si lo saben |
|---|---|
|DeepSeek | |

> Cuenta también el autocompletado del editor (Copilot y similares). Si sólo
> fue eso, basta con decirlo en un renglón y seguir al punto 4.

---

## 2. Objetivo del uso

| Para qué la usamos | En qué parte del entregable |
|---|---|
| Para dudas de comprensión existentes de python respecto a algunso metodos y apoyo para identificar como hacer una prueba en python | Unas fueron teoricas, una prueba que despues de comprender solo la modifique otras veces esta en evaluator.py |

> Sean específicos. *"Para la tarea"* no dice nada.
> *"Para generar las pruebas de `minimo_de_llaves`"* sí.

---

## 3. Prompts principales

Textuales, tal como los escribieron. No los limpien ni los reescriban.

```
Que "42" produzca [Token(NUMERO, 42, 0)]
LO que hace esto es pasar tipo si da 41 pasar a 41,0?
```

```
pero entonces que hace, osea checa que este un numero en la primera posición? y no un operador?

```

```
##def test_division_cero():
   ## assert interpretar("10 / 0") == 0

esto que puse cuenta como un test frontera?
```

```
def test_division_entre_cero():
    with pytest.raises(ErrorDeEvaluacion):
        interpretar("10 / 0")

esto si es un cado frontera?

```

```
$ pytest -v 
====================================================== test session starts ======================================================
platform linux -- Python 3.13.13, pytest-9.1.1, pluggy-1.6.0 -- /home/suemy/Documentos/Modelado/tarea1-mini-interprete/venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/suemy/Documentos/Modelado/tarea1-mini-interprete
collected 14 items                                                                                                              

tests/test_evaluator.py::test_suma PASSED                                                                                 [  7%]
tests/test_evaluator.py::test_resta PASSED                                                                                [ 14%]
tests/test_evaluator.py::test_multiplicacion PASSED                                                                       [ 21%]
tests/test_evaluator.py::test_division PASSED                                                                             [ 28%]
tests/test_evaluator.py::test_division_entre_cero FAILED                                                                  [ 35%]
tests/test_evaluator.py::test_precedencia_sin_parentesis PASSED                                                           [ 42%]
tests/test_evaluator.py::test_precedencia_con_parentesis PASSED                                                           [ 50%]
tests/test_lexer.py::test_tokeniza_un_numero_solo PASSED                                                                  [ 57%]
tests/test_lexer.py::test_tokeniza_una_suma PASSED                                                                        [ 64%]
tests/test_lexer.py::test_los_espacios_no_producen_tokens PASSED                                                          [ 71%]
tests/test_lexer.py::test_tokeniza_parentesis PASSED                                                                      [ 78%]
tests/test_parser.py::test_construye_el_arbol_de_una_suma PASSED                                                          [ 85%]
tests/test_parser.py::test_la_multiplicacion_se_agrupa_antes_que_la_suma PASSED                                           [ 92%]
tests/test_parser.py::test_los_parentesis_cambian_la_agrupacion PASSED                                                    [100%]

=========================================================== FAILURES ============================================================
___________________________________________________ test_division_entre_cero ____________________________________________________

    def test_division_entre_cero():
>       with pytest.raises(ErrorDeEvaluacion):
             ^^^^^^
E       NameError: name 'pytest' is not defined

tests/test_evaluator.py:23: NameError
==================================================== short test summary info ====================================================
FAILED tests/test_evaluator.py::test_division_entre_cero - NameError: name 'pytest' is not defined
================================================= 1 failed, 13 passed in 0.07s ==================================================
(venv) suemy@2806-104e-0025-fcbd-35c1-e7c0-121e-18a7:~/Documentos/Modelado/tarea1-mini-interprete$ pytest  
====================================================== test session starts ======================================================
platform linux -- Python 3.13.13, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/suemy/Documentos/Modelado/tarea1-mini-interprete
collected 14 items                                                                                                              

tests/test_evaluator.py ....F..                                                                                           [ 50%]
tests/test_lexer.py ....                                                                                                  [ 78%]
tests/test_parser.py ...                                                                                                  [100%]

=========================================================== FAILURES ============================================================
___________________________________________________ test_division_entre_cero ____________________________________________________

    def test_division_entre_cero():
>       with pytest.raises(ErrorDeEvaluacion):
             ^^^^^^
E       NameError: name 'pytest' is not defined

tests/test_evaluator.py:23: NameError
==================================================== short test summary info ====================================================
FAILED tests/test_evaluator.py::test_division_entre_cero - NameError: name 'pytest' is not defined
================================================= 1 failed, 13 passed in 0.07s ==================================================
(venv) suemy@2806-104e-0025-fcbd-35c1-e7c0-121e-18a7:~/Documentos/Modelado/tarea1-mini-interprete$ 
esta bien que salga así no?

```
```
El  2.2 ¿Qué comportamientos no estaban probados?, 
respecto a los 13 test pq eso fue la tabla que llen

por ejemplo le puse que en evaluator falta test de división entre cero y tambien note que falta el comportamiento de una operación de -4-4
$ python3 interprete.py   
-4-4
Error: Token inesperado '-' (posicion 0)

entonces ese tambien falta
```

```
def test_la_suma_acaba_sin_cerrar_parentesis():
    assert interpretar("( 3 + 4") == 7

como puedo corregir esa prueba
```

```
#Agregado
def test_simbolos_como_operadores():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("3 4")

como puedo agregar todos los simbolos o varios, que sean posibles que el usuario pueda ingresar entre 3 y 4, por ejemplo 

3#4

y que mande el error sintatico o 3$4
```
```
Como escribo una prueba que exija la posición correcta
mandame esto, te mando errores.py
"""Errores propios del interprete.

Tener errores propios (y no dejar escapar los de Python) es lo que permite
que una prueba diga "esta entrada DEBE ser rechazada" en vez de "esta entrada
truena de alguna manera".
"""


class ErrorDelInterprete(Exception):
    """Error base. Todo lo que el interprete reporta hereda de aqui."""


class ErrorDeSintaxis(ErrorDelInterprete):
    """La entrada no forma una expresion valida."""

    def __init__(self, mensaje: str, posicion: int):
        self.mensaje = mensaje
        self.posicion = posicion
        super().__init__(f"{mensaje} (posicion {posicion})")


class ErrorDeEvaluacion(ErrorDelInterprete):
    """La expresion es valida pero no se puede evaluar."""

```
---

## 4. Cómo se incorporó o se descartó lo obtenido

**Éste es el punto que más pesa.**

| Qué produjo la herramienta | ¿Aceptado, modificado o descartado? | Por qué | Dónde quedó (archivo / commit) |
|---|---|---|---|
|En las que le pedí un resultado/corrección mando código | Aceptado | Depende de que pedí, si no pedí una respuesta de codigo solo me fijo en las primera respuesta de "Esta mal", hago mis intentos para saber que es lo que esta mal y si pedí codigo pues tomo y leo toda la respuesta para saber que voy a copiar | en test_evaluator.py, los metodos copiados son dos: test_division_entre_cero_reporta_posicion() y test_division_entre_cero()|

> **"Lo descartamos" es una respuesta excelente**, si dicen por qué.
> Una declaración donde todo se aceptó sin cambios es una declaración que
> no muestra criterio.

### 4.1 Si la usaron para el análisis: el contraste

Se les pidió intentarlo primero por su cuenta. Si lo hicieron así:

| | |
|---|---|
| ¿Qué encontró la herramienta que ustedes **no** habían notado? | En un test que hice mal me mando la corrección usando funciones que no había identificado, cuando no sabía una implementación de python en vez de buscar por google lo busque por la IA  |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? | |

> La segunda es la que más nos interesa. Una herramienta suele no señalar la
> duplicación de código, porque el programa funciona igual. Ustedes ya saben
> por qué eso sí importa.
>
> Si no usaron IA para el análisis, escriban *"no aplica"*.

### 4.2 ¿Cómo verificaron que lo que incorporaron era correcto?
Pasaron los test que quería que pasaran, como:
test_division_entre_cero() o test_expresion_incompleta_reporta_posicion_final()
la logíca que tambien se implemento fue coherente, ademas que las modificaciones al codigo fueron echas sin IA, solo la prueba 
> Una prueba que escribieron, una ejecución, un contraste contra las notas de
> clase o contra el enunciado. *"Lo revisamos"* no es una verificación.

---

## 5. Reflexión

### 5.1 ¿Qué limitación concreta observaron **en esta actividad**?

> Concreta. No *"a veces se equivoca"*, sino *"propuso pruebas sólo para
> m = 4 y nunca para órdenes impares, porque no conocía la definición del
> laboratorio"*.
Las intrucciones transmitidas a la IA deben de ser muy concretas ya que por ejemplo le pedi apoyo para buscar una solución a la agrupación de signos y al enviarle un ejemplo del metodo que estaba proponiendo uso el comportamiento del metodo y implemento lo que le pedí.
### 5.2 ¿Qué harían distinto la próxima vez?

---

## Firma

> Declaramos que entendemos y podemos explicar todo lo que entregamos,
> independientemente de las herramientas que hayamos utilizado.

| Nombre | Número de cuenta |
|---|---|
| Lizeth Suemy Esquivel Izquierdo |32333374-2 |
