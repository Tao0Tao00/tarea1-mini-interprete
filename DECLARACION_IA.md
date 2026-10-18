# Declaración de uso de Inteligencia Artificial

**Actividad:**
Tarea 1

**Integrantes:**
Omar Díaz Aguilar, Lizeth Suemy Esquivel Izquierdo, Gustavo Botello Salcido

**Fecha:** 
16/Oct/2026

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
| Claude ia | Sonet 5.5 |
|DeepSeek | |

> Cuenta también el autocompletado del editor (Copilot y similares). Si sólo
> fue eso, basta con decirlo en un renglón y seguir al punto 4.

---

## 2. Objetivo del uso

| Para qué la usamos | En qué parte del entregable |
|---|---|
| Interpretar instrucciones iniciales | Ninguna parte |
| Ayuda general con git e identificar commits rojos y verdes | Tabla 4.3 |
| Correciones de redacción | ANALISIS.md |
| Para dudas de comprensión existentes de python respecto a algunso metodos y apoyo para identificar como hacer una prueba en python | Unas fueron teoricas, una prueba que despues de comprender solo la modifique otras veces esta en evaluator.py |
|Ayuda para comprension y ver que informacion podia dar |En el 5.3 ver que podia decir sobre la pregunta y comprender lo que decia si daba informacion extra |

> Sean específicos. *"Para la tarea"* no dice nada.
> *"Para generar las pruebas de `minimo_de_llaves`"* sí.

---

## 3. Prompts principales

Textuales, tal como los escribieron. No los limpien ni los reescriban.
```
huh? avr, paso a paso, ya hice clone, que sigue unu
```
```
Que "42" produzca [Token(NUMERO, 42, 0)]
LO que hace esto es pasar tipo si da 41 pasar a 41,0?
```
```
oya oya, avr, hago mis preguntas viendo la tabla de la seccion 7
hay algun numero con 0s a la izquierda? no
hay alguna prueba que divida? si, la 4ta de evaluator, si no existiera la regla 2 se rompería?  creo que no, osea es verde, osea va en 2.2
hay alguna prueba que divida entre 0? no
hay alguna prueba que tenga un numero negativo? no
hay alguna prueba que tenga la prioridad de operaciones? primero parentesis, luego / y *, al final + y -, si, la 5ta y 6ta de evaluator, 2da y 3ra de parser, se rompen si no exisiera la regla 5? 5 de evaluator si y va a 2.2, 6ta de evaluator creo que no, 2da de parser si y va a 2.2, 3ra de parser creo que no
hay alguna prueba con asociatividad? no
hay alguna con espacios? si, la 3ra de lexer, falla si la regla 7 no existe? ....sssssi?, creo que si, o no... no se pdn
y las otras 2 reglas no aplican pq ninguna falla
```
```
como veo el historial de commits jeje xd
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

```
En la pregunta 5.3 que  es lo de factory method y adapter, estaba pensando que realmente no son necesarios o no vi como usarlos, ya que factory method funciona por medio de una super clase y subclases, pensaba que fuera para los operadores pero no lo vi muy practico, y de adapter pues tampoco ya que sigue una regla de comportamientos que tampoco logre ver, no se si este correcto mi pensamiento


Tu razonamiento es correcto, y “ninguno” es una respuesta válida: el README lo dice expresamente, y lo que se evalúa es el criterio, no que metan un patrón.   

Factory Method

Tu idea de usarlo para los operadores es la única aplicación plausible, así que la consideraste bien. Se vería así: una clase por operador (Suma, Resta, ...) y una fábrica que decide cuál crear. Pero el sistema solo crea dos tipos de nodo (Numero y OperacionBinaria), y el parser siempre sabe cuál toca según la gramática. No hay un contexto que cambie qué se crea, que es el problema que resuelve el patrón. Habría más clases y más archivos, y el problema real (el conocimiento de cada operador está repartido en cuatro archivos) seguiría ahí.

Adapter

Sirve para conectar dos interfaces incompatibles, por ejemplo si tuvieran que usar un lexer externo que devuelve tuplas y el parser espera Token. Aquí todos los componentes son del propio proyecto y ya encajan entre sí, así que no hay nada que adaptar. Cuando dices que “sigue una regla de comportamientos”, seguramente te refieres a eso: no encontraste dos interfaces que no se entiendan.

Qué cambiaría la respuesta (esto también es parte de lo que pide la sección 5.3)

    Factory Method convendría si hubiera muchos operadores o familias de nodos y la creación tuviera que centralizarse.
    Adapter convendría si apareciera una pieza externa con otra interfaz.

Para la respuesta, justifiquen “ninguno” con lo anterior: qué problema concreto resolvería cada patrón, por qué aquí no aparece y qué tendría que cambiar para que convinieran.
```
---

## 4. Cómo se incorporó o se descartó lo obtenido

**Éste es el punto que más pesa.**

| Qué produjo la herramienta | ¿Aceptado, modificado o descartado? | Por qué | Dónde quedó (archivo / commit) |
|---|---|---|---|
| Análisis de las instrucciones iniciales | Aceptado | No se implementó en ninguna parte del código, solo era para entender la tarea | Ningún lado |
| Revisión de redacción en las preguntas 4.1 y 4.2| Modificado | Solo explicaba en que fallaba la redacción, nunca escribió por su cuenta las respuestas, había que implementar sus observaciones a la respuesta final | ANALISIS.md, commits: e2cbc4c e17d159|
| Revisión de identificacón de comportamientos no probados (2.2) | Modificado | Aunque interpreté mal lo que significaba que un comportamiento no estuviera probado, tuve que adaptar la respuesta de la ia | ANALISIS.m pregunta 2.2, commit: 0a179f1 | 
| Comandos de git sobre ramas, e historial de commits para identificar commits rojos y verdes | Aceptado | Son comandos de terminal | ANALISIS.md pregunta 4.3, commit: e0ad237 |  
|En las que le pedí un resultado/corrección mando código | Aceptado | Depende de que pedí, si no pedí una respuesta de codigo solo me fijo en las primera respuesta de "Esta mal", hago mis intentos para saber que es lo que esta mal y si pedí codigo pues tomo y leo toda la respuesta para saber que voy a copiar | en test_evaluator.py, los metodos copiados son dos: test_division_entre_cero_reporta_posicion() y test_division_entre_cero()|

> **"Lo descartamos" es una respuesta excelente**, si dicen por qué.
> Una declaración donde todo se aceptó sin cambios es una declaración que
> no muestra criterio.

### 4.1 Si la usaron para el análisis: el contraste

Se les pidió intentarlo primero por su cuenta. Si lo hicieron así:

| | |
|---|---|
| ¿Qué encontró la herramienta que ustedes **no** habían notado? | Distinguir cuando un comportamiento no estaba probado |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? | Nada, al menos no con el contexto que le di |
| ¿Qué encontró la herramienta que ustedes **no** habían notado? | En un test que hice mal me mando la corrección usando funciones que no había identificado, cuando no sabía una implementación de python en vez de buscar por google lo busque por la IA  |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? | |
| ¿Qué encontró la herramienta que ustedes **no** habían notado? | Dar lo de tupla como interfaz si se quiere usar adapter |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? |Nada en especial contando tenia informacion de las clases pero no la respuesta completa a la pregunta|

> La segunda es la que más nos interesa. Una herramienta suele no señalar la
> duplicación de código, porque el programa funciona igual. Ustedes ya saben
> por qué eso sí importa.
>
> Si no usaron IA para el análisis, escriban *"no aplica"*.

### 4.2 ¿Cómo verificaron que lo que incorporaron era correcto?

Los comandos hacían lo que necesitaba, las verificaciones de redacción tenían sentido y mostraban en que partes me equivoqué o pude haberlo hecho mejor.

Pasaron los test que quería que pasaran, como:
test_division_entre_cero() o test_expresion_incompleta_reporta_posicion_final()
la logíca que tambien se implemento fue coherente, ademas que las modificaciones al codigo fueron echas sin IA, solo la prueba 
> Una prueba que escribieron, una ejecución, un contraste contra las notas de
> clase o contra el enunciado. *"Lo revisamos"* no es una verificación.

---

## 5. Reflexión

### 5.1 ¿Qué limitación concreta observaron **en esta actividad**?

Claude no tenía todo el contexto de la actividad, solo pensaba con el material que yo le daba. Entonces pudo cometer errores por falta de contexto, aunque en mi caso concreto no fue asi

> Concreta. No *"a veces se equivoca"*, sino *"propuso pruebas sólo para
> m = 4 y nunca para órdenes impares, porque no conocía la definición del
> laboratorio"*.
Las intrucciones transmitidas a la IA deben de ser muy concretas ya que por ejemplo le pedi apoyo para buscar una solución a la agrupación de signos y al enviarle un ejemplo del metodo que estaba proponiendo uso el comportamiento del metodo y implemento lo que le pedí.
### 5.2 ¿Qué harían distinto la próxima vez?

Tratar de leer con calma las instrucciones de la actividad y antes de hacer nada, ver como funcionaba el problema original.

---

## Firma

> Declaramos que entendemos y podemos explicar todo lo que entregamos,
> independientemente de las herramientas que hayamos utilizado.

| Nombre | Número de cuenta |
|---|---|
| Gustavo Botello Salcido | 323177308 |
| Lizeth Suemy Esquivel Izquierdo |32333374-2 |
| Omar Diaz Aguilar| 322012628|
