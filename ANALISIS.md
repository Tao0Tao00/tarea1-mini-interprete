# Análisis — Tarea 1

**Integrantes:**
1.
2.
3.

**Fork:**
**Rama:**

> Contesten en este archivo. Respuestas breves y concretas: se califica que
> hayan entendido, no la extensión.

---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?

| Componente | Qué recibe | Qué entrega | De qué es responsable |
|---|---|---|---|
| `lexer` |Texto de la expresion (str) |Una lista de Token(tipo, valor, posicion) |Recorre el texto, saltar espacios, agrupar los digitos en numero y tokenizar los simbolos |
| `parser` |Lista de tokens |AST(nodo raiz) |Aplica la gramatica(expresion, termino, factor) para agrupar la expresion, ademas que lanza un `ErrorDeSintaxis` cuando los tokens no forman una expresion valida |
| `ast` |Operador y nodos hijo o un valor numerico | Nodos `Numero` y `OperacionBinaria` |Define la estructura del arbol AST ya agrupado |
| `evaluator` | El AST completo |Un numero |Recorre el arbol de abajo hacia arriba y evalua los lados con sus respectivos operadores, Da un `ErrorDeEvaluacion` en casos no evaluables |

### 1.2 ¿Qué recorrido sigue una expresión desde que se recibe como texto hasta que produce un resultado?

> Usen `(3 + 4) * 2` como ejemplo y muestren cómo se ve entre etapa y etapa.

| Etapa | Cómo se ve `(3 + 4) * 2` aquí |
|---|---|
| texto | `"(3 + 4) * 2"` |
| tokens |`[Token(PAR_IZQ, '(', 0), Token(NUMERO, 3, 1), Token(MAS, '+', 3), Token(NUMERO, 4, 5), Token(PAR_DER, ')', 6), Token(POR, '*', 8), Token(NUMERO, 2, 10)]` |
| AST |`OperacionBinaria'*', OperacionBinaria('+', Numero(3), Numero(4), Numero(2))` |
| resultado |14 |

> Para el renglón del AST, dibújenlo **primero ustedes** y después comprueben
> con `python3 interprete.py --arbol "(3 + 4) * 2"`. Si su dibujo y el del
> programa no coinciden, uno de los dos está mal, y averiguar cuál es
> justamente el trabajo.

---

## 2. Las pruebas que ya estaban

### 2.1 ¿Qué pruebas venían incluidas?

| Prueba | Componente | Comportamiento que verifica | ¿Cuántos operadores usa? | ¿Normal, frontera o inválida? |
|---|---|---|---|---|
| test_suma()| evaluator | Verifica que 3 + 4 de 7 | 1 |Normal |
| test_resta()| evaluator| Verifica que 10 - 3 de 7 | 1|Normal |
| test_multiplicacion()| evaluator| Verifica que 6 * 7 de 42 | 1|Normal|
| test_division()| evaluator| Verifica que 10 / 2 de 5 | 1| Normal|
| test_precedencia_sin_parentesis()| evaluator| Verifica la jeraquia de operacion de 3 + 4 * 2 que de 11| 2| Normal |
| test_precedencia_con_parentesis()| evaluator|Verifica la jeraquia de operacion de(3 + 4) * 2 por parentesis que de 14 | 2| Normal |
| test_tokeniza_un_numero_solo| lexer| Checa que sea exactamente el numero 42 en la posicion 0 |0 |Normal |
| test_tokeniza_una_suma()| lexer| Checa la posición de cada numero o operador este en el indicado de 3+4 |1| Normal|
| test_los_espacios_no_producen_tokens()| lexer| Checa que los espacios no sean considerados como tokens de 3 + 4 |1|Frontera|
| test_tokeniza_parentesis()| lexer| Pasa a tokens los parentesis |0| Normal|
| test_construye_el_arbol_de_una_suma()| parser| Forma el arbol de operación de la suma de 3+4 |1| Normal|
| test_la_multiplicacion_se_agrupa_antes_que_la_suma()| parser| Indica que la multiplicación en la operación 3 + 4 * 2 se agrupa para operar |2| Normal|
| test_los_parentesis_cambian_la_agrupacion()| parser| (3 + 4) * 2  debe agruparse al reves |2| Normal|

> Llenen la tabla **completa**, con las 13. Es tediosa a propósito: la única
> forma de saber qué no está cubierto es caracterizar sistemáticamente lo que
> sí. Cuando terminen, léanla como columna, no como renglones, y pregúntense
> qué combinación **no aparece nunca**.

### 2.2 ¿Qué comportamientos **no** estaban probados?

> Ésta es la pregunta importante de toda la tarea. Tómense su tiempo.

---

## 3. Las pruebas que agregaron

### 3.1 ¿Cuáles son casos normales, cuáles frontera y cuáles inválidos?

| Prueba (archivo::nombre) | Entrada | Esperado | Categoría | ¿Por qué esa categoría? |
|---|---|---|---|---|
| test_invalidos::test_entrada_vacia | "" | ErrorDeSintaxis | Entrada inválida | Para que sea válida necesita por lo menos un número (o un número entre parentesis) |
| test_invalidos::test_con_letras | 2 + Laboon | ErrorDeSintaxis | Entrada invalida | Sólo se permiten números, paréntesis y símbolos de operadores (+ - * /)|
| test_invalidos::test_sin_operador | 2 9 | ErrorDeSintaxis | Entrada inválida | No pueden estar dos números sin estar unidos por un operador |
| test_invalidos::test_dos_operadores_seguidos | 2 +* 9 | ErrorDeSintaxis | Entrada inválida | Dos operadores no pueden estar directamente juntos |
| test_invalidos::test_parentesis_extra | 9) | ErrorDeSintaxis | Entrada inválida | Se cierra un paréntesis que no se abrió |
| test_invalidos::test_sin_segundo_termino | 9 + | ErrorDeSintaxis | Entrada inválida | Un operador debe de tener 2 números con los que trabajar, si solo hay uno no funciona |
| test_invalidos::test_negativo | -9 | ErrorDeSintaxis | Entrada inválida | Los números deben ser enteros y sin signo |
| test_invalidos::test_parentesis_sin_cerrar | (2 + 9 | ErrorDeSintaxis | Entrada inválida |  Se abre un paréntesis que no se cierra |
|test_invalidos::test_simbolo_desconocido | 2 + 9 & | ErrorDeSintaxis | Entrada inválida | Sólo se permiten números, paréntesis y símbolos de operadores (+ - * /)|

---

## 4. Los defectos

### 4.1 ¿Qué defecto reveló primero una prueba nueva?
La prueba que reveló el defecto es la de entrada vacía (con la entrada ""), ya que lanzaba el error de IndexError en lugar de ErrorDeSintaxis. El defecto se encuentra en parser.py, ahí el método _avanzar ejecutaba elf.tokens[self.pos] sin antes sevisar si ya no quedaban tokens.

### 4.2 ¿Por qué el comportamiento observado era incorrecto?
No respetaba la fila de *Entrada inválida* donde se dice que el programa debe rechazarse usando ErrorDeSintaxis y nunca con un error propio de Python, sin embargo el programa lo rechazaba con IndexError. También se menciona que los mensajes de error deben indicar la posicion dentro del texto, pero el error IndexError no menciona la posición del problema.

> No basta con "daba mal". Digan contra qué lo están comparando: qué regla,
> qué línea de la semántica declarada del README.

### 4.3 ¿Qué cambio realizaron?

| Defecto | Entrada que lo revela | Daba | Debería dar | Commit rojo | Commit verde |
|---|---|---|---|---|---|
| _avanzar ejecutaba elf.tokens[self.pos] sin revisar si ya no quedaban tokens | "" | IndexError | ErrorDeSintaxis | 01ce476 | e143454 |
| parsear no revisaba si sobraban tokens | 2 9 | no lanzaba error | ErrorDeSintaxis | 01ce476 |	68ad726 |
| lexer ignoraba los caracteres desconocidos | 2 + 9 & | no lanzaba error | ErrorDeSintaxis | e4d2016 |	68ad726 | 

### 4.4 ¿Cómo saben que la corrección es general y no sólo hace pasar ese ejemplo?

---

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontraron?

> Al menos dos. Usen el vocabulario de clase: duplicación, rigidez,
> acoplamiento alto, condicionales repetidos, amplificación del cambio.

### 5.2 ¿Qué refactorización realizaron, y por qué conserva el comportamiento?

> "Las pruebas siguen pasando" es parte de la respuesta, pero no toda.
> ¿Por qué el cambio es equivalente?

### 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?

> Justifiquen. **"Ninguno" puede ser la respuesta correcta.** Si dicen que sí,
> digan qué problema concreto resuelve y qué costo tiene. Si dicen que no,
> digan qué tendría que cambiar en el sistema para que empezara a convenir.

### 5.4 ¿Qué parte del sistema sería más difícil de modificar si se agregara un operador nuevo?

> Por ejemplo `%`. ¿Cuántos archivos hay que tocar? ¿Por qué?

---

## Antes de la declaración: inténtenlo primero ustedes

Usar IA o no es decisión de cada quien, y el curso la permite. Pero **les
pedimos, por favor, que primero hagan el análisis por su cuenta.**

No es una prueba de honestidad. Es que el orden cambia lo que aprenden:

1. **Primero ustedes.** Lean el código, corran las pruebas, escriban sus
   respuestas. Aunque queden incompletas, aunque no encuentren todo.

2. **Después, si quieren, la IA** — pero como contraste, no como sustituto.
   Y entonces contesten dos preguntas, en `DECLARACION_IA.md`:

   - **¿Qué encontró que ustedes no habían notado?**
     Eso es aprendizaje, y se declara sin ninguna pena.

   - **¿Qué *no* encontró, que en este curso sí consideramos un problema?**
     Ésta es la interesante. Una herramienta suele decir que el código
     "funciona bien" y no señalar, por ejemplo, la **duplicación** — porque
     duplicar no rompe nada, el programa corre igual. Pero ustedes ya saben
     por qué eso sí es un mal diseño, y saben nombrarlo. La herramienta no
     tomó esa clase.

> Si invierten el orden se pierden justamente lo segundo: **no se puede notar
> lo que a una herramienta le faltó si uno nunca se formó una opinión propia
> antes de preguntarle.** Y que un programa funcione no implica que esté bien
> diseñado — eso lo dijimos en clase mucho antes de esta tarea.

---

## Declaración de uso de Inteligencia Artificial

Va en `DECLARACION_IA.md`, no aquí. Es obligatoria, pero **no da ni quita
puntos**: es un reporte adicional que se revisa aparte y se les devuelve con
comentarios.

**No se evalúa cuánta IA usaron.** Se evalúa si pueden dar cuenta de lo que
entregaron. *"No usamos"* es una declaración válida y completa; *"lo
descartamos porque..."* es de las mejores respuestas posibles.
