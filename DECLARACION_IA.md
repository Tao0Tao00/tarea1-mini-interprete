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

> Cuenta también el autocompletado del editor (Copilot y similares). Si sólo
> fue eso, basta con decirlo en un renglón y seguir al punto 4.

---

## 2. Objetivo del uso

| Para qué la usamos | En qué parte del entregable |
|---|---|
| Interpretar instrucciones iniciales | Ninguna parte |
| Ayuda general con git e identificar commits rojos y verdes | Tabla 4.3 |
| Correciones de redacción | ANALISIS.md |


> Sean específicos. *"Para la tarea"* no dice nada.
> *"Para generar las pruebas de `minimo_de_llaves`"* sí.

---

## 3. Prompts principales

Textuales, tal como los escribieron. No los limpien ni los reescriban.
```
huh? avr, paso a paso, ya hice clone, que sigue unu
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

---

## 4. Cómo se incorporó o se descartó lo obtenido

**Éste es el punto que más pesa.**

| Qué produjo la herramienta | ¿Aceptado, modificado o descartado? | Por qué | Dónde quedó (archivo / commit) |
|---|---|---|---|
| Análisis de las instrucciones iniciales | Aceptado | No se implementó en ninguna parte del código, solo era para entender la tarea | Ningún lado |
| Revisión de redacción en las preguntas 4.1 y 4.2| Modificado | Solo explicaba en que fallaba la redacción, nunca escribió por su cuenta las respuestas, había que implementar sus observaciones a la respuesta final | ANALISIS.md, commits: e2cbc4c e17d159|
| Revisión de identificacón de comportamientos no probados (2.2) | Modificado | Aunque interpreté mal lo que significaba que un comportamiento no estuviera probado, tuve que adaptar la respuesta de la ia | ANALISIS.m pregunta 2.2, commit: 0a179f1 | 
| Comandos de git sobre ramas, e historial de commits para identificar commits rojos y verdes | Aceptado | Son comandos de terminal | ANALISIS.md pregunta 4.3, commit: e0ad237 |  

> **"Lo descartamos" es una respuesta excelente**, si dicen por qué.
> Una declaración donde todo se aceptó sin cambios es una declaración que
> no muestra criterio.

### 4.1 Si la usaron para el análisis: el contraste

Se les pidió intentarlo primero por su cuenta. Si lo hicieron así:

| | |
|---|---|
| ¿Qué encontró la herramienta que ustedes **no** habían notado? | Distinguir cuando un comportamiento no estaba probado |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? |  |

> La segunda es la que más nos interesa. Una herramienta suele no señalar la
> duplicación de código, porque el programa funciona igual. Ustedes ya saben
> por qué eso sí importa.
>
> Si no usaron IA para el análisis, escriban *"no aplica"*.

### 4.2 ¿Cómo verificaron que lo que incorporaron era correcto?

Los comandos hacían lo que necesitaba, las verificaciones de redacción tenían sentido y mostraban en que partes me equivoqué o pude haberlo hecho mejor

> Una prueba que escribieron, una ejecución, un contraste contra las notas de
> clase o contra el enunciado. *"Lo revisamos"* no es una verificación.

---

## 5. Reflexión

### 5.1 ¿Qué limitación concreta observaron **en esta actividad**?

Claude no tenía todo el contexto de la actividad, solo pensaba con el material que yo le daba. Entonces pudo cometer errores por falta de contexto, aunque en mi caso concreto no fue asi

> Concreta. No *"a veces se equivoca"*, sino *"propuso pruebas sólo para
> m = 4 y nunca para órdenes impares, porque no conocía la definición del
> laboratorio"*.

### 5.2 ¿Qué harían distinto la próxima vez?

Tratar de leer con calma las instrucciones de la actividad y antes de hacer nada, ver como funcionaba el problema original.

---

## Firma

> Declaramos que entendemos y podemos explicar todo lo que entregamos,
> independientemente de las herramientas que hayamos utilizado.

| Nombre | Número de cuenta |
|---|---|
| Gustavo Botello Salcido | 323177308 |
