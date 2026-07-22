# Clase 19: Notebook
#### Nombre: Patricio Navarro

## Pregunta inicial
**¿Cómo encontramos un orden válido para ejecutar tareas cuando unas dependen de otras?**
- Empezando por aquellas que no tienen prerequisitos y de ahi ir moviendonos a las que se van "desbloqueando" hasta terminarlas todas.

## Presentación de la clase
**En el problema de cursos, ¿qué operación necesitamos repetir para construir un plan válido?**
- Tomar primero los cursos que no requieren llevar otros cursos antes y de ahi ir tomando los demás hasta terminar el plan.

## El nuevo problema: dependencias
**Actividad inicial.** Anota qué cursos tomarías primero, cuáles esperan y si crees que existe un solo plan. Resultado comprobable: cualquier propuesta debe colocar cada prerrequisito antes que su curso.
1. Programación y discretas.
2. Estructuras de datos y álgebra.
3. Algoritmos y optimización.
4. Proyecto final.
- Este no es el único plan, me hizo sentido ahorita así porque lo estoy pensando como llevamos las materias nosotros, pero si fuera una por una puedes tomar primero programación y luego discretas o viceversa, o primero álgebra y luego las otras dos y así.

¿Qué debe ocurrir antes de Proyecto Final y por qué puede haber más de una respuesta correcta?
- Debes llevar todas las demás materias. Pero hay más de una respuesta correcta porque hay muchas formas de tomar los primeros tres cursos que no tienen dependencias y de tomar los cursos intermedios hasta llegar a Proyecto Final.

## Interpretación de aristas dirigidas
**Comprobación manual.** Para `A → C` y `B → C`, C debe esperar dos tareas. A y B no están ordenadas entre sí. Dibuja también las flechas inversas y describe cómo cambia la historia.
- `C → A` y `C → B`:
    - Aquí debes tomar C antes de podar tomar A y B, aunque A y B no tiene un orden entre ellas.

¿Por qué A → B y B → A representan restricciones diferentes?
- Porque la relación no es simétrica, no es lo mismo que B depnda de A a que A dependa de B. Si así fuera no habría ningún órden.

## Qué es un DAG
**Actividad.** Clasifica `X → Y`, dos nodos aislados, una autoarista `Z → Z` y `P → Q → R → P`. Resultado esperado: los dos primeros son DAG; los dos últimos contienen ciclo.
- `X → Y`: Y depende de X; es un DAG.
- `X` y `Y`: Ninguno depende del otro, se pueden hacer en cualquier órden; es un DAG.
- `z → Z`: Z depende de Z, entonces para hacer Z necesitas haber hecho Z. No tiene sentido y es un DCG.
- `P → Q → R → P`: Q depende P, R depende Q y P depende de R. No importa donde empieces dependes de otras dos que dependen de ti, es un DCG.

¿Por qué el ciclo A → B → C → A impide cualquier orden topológico?
- No importa donde empieces dependes de otras dos que dependen de ti, por lo tanto terminas atorado en un ciclo sin poder avanzar.

## Ejemplos con y sin ciclos
**Desarrollo manual.** Escribe una secuencia candidata para cada DAG y marca la primera arista que invalida cada propuesta incorrecta. No basta decir “se ve mal”; localiza `u → v` con `v` antes que `u`.
1. Cadena: `A → B, B → C`
    - Secuencia candidata: `A, B, C`.
    - Propuesta incorrecta: `B, A, C`
    - Arista que lo invalida: `A → B`.
2. Fuente: `A → C, B → C`
    - Secuencia candidata: `A, B, C` o `B, A, C`.
    - Propuesta incorrecta: `C, A, B` o `C, B, A` o `B, C, A` o `A, C, B`.
    - Arista que lo invalida: `A → C` o `B → C`.
3. Los casos ciclo y mixto no son DAG.

En el grafo mixto, ¿por qué procesar D y E no permite devolver un orden parcial como solución?
- Porque el contrato del problema exige un orden completo para todo el grafo. Si una parte está trabada en un ciclo, el plan completo falla y la solución no es válida.

## Grado de entrada
| Nodo | Aristas entrantes | Grado |
| --- | --- | ---: |
| Programación | ninguna | 0 |
| Algebra | ninguna | 0 |
| Discretas | ninguna | 0 |
| Estructuras de Datos | Programacion, Discretas | 2 |
| Optimizacion | ALgebra | 1 |
| Algoritmos | Estructuras de datos | 1 |
| Proyecto Final | Optimizacion, Algoritmos | 2 |

**¿Qué grados de entrada tienen Algoritmos, Optimización y Proyecto Final en el problema conductor?**
- Algoritmos tiene 1.
- Optimización tiene 1.
- Proyecto Final tiene 2.

## Nodos disponibles
**¿En qué momento exacto debe encolarse Estructuras de Datos?**
- Al terminar de procesar Programación y Discretas.

## Descubrimiento de Kahn:
**Actividad.** Antes de ejecutar, predice cola inicial, primer nodo y qué grados cambiarán para `A→C`, `B→C`, `C→D`. Resultado verificable: C entra únicamente después de A y B.
1. Cola inicial: `[A, B]`; grado de C: 2
2. Primer nodo: `A`; grado de C: 1
3. Segundo nodo: `B`; grado de C: 0 
4. Cola: `[C]`; grado de D: 1
5. Tercer Nodo: `C`; grado de D: 0
6. Cola: `[D]`; Se procesa `D`.

¿Qué representa disminuir en uno el grado de entrada de un vecino?
- Que faltan menos nodos antes de poder acceder a él.

## Ejecución manual
**Actividad — completar Kahn.** Llena las incógnitas y repite el ejercicio comenzando con B. Debes obtener dos órdenes válidos: `A,B,C,D` y `B,A,C,D`.
1. 
| Paso | Cola antes | Actual | Vecino | Grado anterior | Grado nuevo | Acción | Orden |
| ---: | --- | --- | --- | ---: | ---: | --- | --- |
| 1 | A, B | A | C | 2 | 1 | sigue bloqueado | A |
| 2 | B | B | C | 1 | 0 | encolar C | A, B |
| 3 | C | C | D | 1 | 0 | encolar D | A, B, C |
| 4 | D | D | — | — | — | terminar | A, B, C, D |

2. 
| Paso | Cola antes | Actual | Vecino | Grado anterior | Grado nuevo | Acción | Orden |
| ---: | --- | --- | --- | ---: | ---: | --- | --- |
| 1 | A, B | B | C | 2 | 1 | sigue bloqueado | B |
| 2 | A | A | C | 1 | 0 | encolar C | B, A |
| 3 | C | C | D | 1 | 0 | encolar D | B, A, C |
| 4 | D | D | — | — | — | terminar | B, A, C, D |

Completa los pasos 3 y 4: ¿qué valores y orden final deben aparecer?
- Paso 3: 
    - Cola antes: [C]
    - Actual: C
    - Vecino: D
    - Grado anterior: 1
    - Grado nuevo: 
    - Acción: encolar D
    - Orden: [A, B, C].  
- Paso 4: 
    - Cola antes: [D]
    - Actual: D, Vecino: —
    - Grado anterior: — 
    - Grado nuevo: —
    - Acción: terminar
    - Orden final: [A, B, C, D] (o [B, A, C, D]).  

## Uso de la cola
**¿Por qué la solución evaluada usa deque aunque ColaLigada pueda implementar la misma política?**
- Para asegurar que el ejercicio evalúe únicamente la lógica de dependencias y grados de esta clase.

## Invariantes
**¿Qué invariante se viola si un nodo entra a la cola cuando su grado todavía es 1?**
- Se viola la regla central de que solo pueden estar en la cola los nodos que tengan un grado de entrada actual de cero.

## Implementación paso a paso
**¿Qué cuatro estructuras locales necesita mantener orden_topologico y para qué sirve cada una?**
- `normalizado`: Una copia limpia del grafo para no modificar los datos originales.  
- `grados`: Un diccionario para llevar la cuenta de cuántos requisitos le quedan a cada nodo.  
- `disponibles`: Una cola para guardar temporalmente las tareas listas para realizar.  
- `orden`: Una lista donde vamos anotando la secuencia final del plan.

## Detección de ciclos
**Actividad — detectar ciclos.** Clasifica: cadena; dos fuentes hacia un sumidero; autoarista; componente acíclica junto a un ciclo. Para cada caso anota cola inicial, cantidad procesada y retorno esperado.
- Caso 1: Cadena `(A → B → C)`
    - Cola inicial: [A].  
    - Cantidad procesada: 3.  
    - Retorno esperado: Una lista con el orden topológico único: `[A, B, C]`.  
- Caso 2: Dos fuentes hacia un sumidero `(A → C, B → C)`

    Cola inicial: `[A, B]` o `[B, A]`.  

    Cantidad procesada: 3.  

    Retorno esperado: Una lista con un orden válido puede ser `['A', 'B', 'C']` o `['B', 'A', 'C']`.  

- Caso 3: Autoarista `(A → A)`
    - Cola inicial: `[]`.  
    - Cantidad procesada: 0.  
    - Retorno esperado: `None`.  

- Caso 4: Componente acíclica junto a un ciclo `(D → E y A → B → C → A)`
    - Cola inicial: `[D]`.  
    - Cantidad procesada: 2.  
    - Retorno esperado: `None`.

¿Por qué len(orden) != len(normalizado) es evidencia de un ciclo?
- Porque significa que la cola se quedó vacía antes de procesar todas las tareas. Esto demuestra que los nodos que faltan se están bloqueando mutuamente en un ciclo y ninguno pudo llegar a grado cero.

## BFS frente a Kahn
**¿Cuál es la diferencia decisiva entre la regla para encolar en BFS y en Kahn?**
- En BFS un nodo entra a la cola en cuanto es descubierto por primera vez. 
- En Kahn, el nodo solo puede entrar cuando todos sus requisitos previos ya fueron procesados.

## Ordenes no únicos
**Actividad.** Enumera todos los órdenes válidos de `A→D`, `B→D`, `C→D`. Resultado: cualquier permutación de A, B y C seguida de D; son seis.
1. `[A, B, C, D]`
2. `[A, C, B, D]`
3. `[B, A, C, D]`
4. `[B, C, A, D]`
5. `[C, A, B, D]`
6. `[C, B, A, D]`

¿Por qué un test que exige exactamente [A, B, C] es incorrecto para A→C y B→C?
- Porque ignora el otro posible caso.

## Validación de un orden
**Actividad — validar secuencias.** Para `A→C`, `B→C`, clasifica:

| Secuencia | ¿Válida? | Primera razón |
| --- | --- | --- |
| A,B,C | sí | respeta ambas aristas |
| B,A,C | sí | respeta ambas aristas |
| C,A,B | no | viola `A → C` |
| A,C | no | viola `B → C` |
| A,A,C | no | repite A y viola `B → C` |

Clasifica las cuatro secuencias incompletas de la tabla y explica la primera regla que falla.
- B,A,C: 
    - Válida: Respeta perfectamente que A y B se hagan antes que C.  
- C,A,B: 
    - Inválida: Falla porque coloca a C antes de completar sus requisitos A y B.  
- A,C: 
    - Inválida: Falla por cobertura (falta incluir la tarea B). 
- A,A,C: 
    - Inválida: Falla porque repite el nodo A y omite el nodo B. 

## Normalización y depenedencias duplicadas
**Actividad.** Predice claves y listas para `{"A": ("C","C"), "B": []}`. Resultado según primera aparición: A, C, B; C aparece una vez en la adyacencia.
- Entrada original: `{"A": ("C", "C"), "B": []}`[cite: 5]
- Predicción paso a paso:
    1. Orden de las claves: Se registra primero `A`, luego se descubre `C` y finalmente se registra `B`. 
        - El orden estable de claves será: `A, C, B`.
    2. Listas de adyacencia:
        - Para `A`: Se convierte la tupla en lista y se eliminan los duplicados, conservando solo la primera aparición. Queda `["C"]`.
        - Para `C`: Como es un nodo implícito, se normaliza agregándolo con una lista vacía `[]`.
        - Para `B`: Conserva su lista vacía original `[]`.
- Resultado final:
    ```python
    {
        "A": ["C"],
        "C": [],
        "B": []
    }

¿Por qué una dependencia duplicada no debe aumentar dos veces el grado de entrada?
- Porque si cuenta doble, cuando completes esa tarea previa solo reducirás el grado en uno. El nodo quedará bloqueado para siempre con un requisito fantasma.

## Casos límite
¿Cómo deben aparecer los nodos aislados en un orden topológico y por qué?
- Deben aparecer en la lista final porque son parte del grafo y como no tienen requisitos, su grado inicial es cero entonces están listos desde el primer momento.

## Problema de cursos
**Actividad.** Añade `(3,0)` y localiza el ciclo. Después prueba una dependencia duplicada y explica por qué el resultado lógico no cambia.
1. Añadir la arista `(3, 0)` y localizar el ciclo
    - Grafo actualizado: `(0, 2), (1, 2), (2, 3)` y ahora `(3, 0)`.
    - Ciclo localizado: `0 → 2 → 3 → 0`
    - Análisis: Al introducir la flecha del nodo 3 al nodo 0, se crea un bloqueo circular irresoluble. El nodo 2 espera al 0, el 3 espera al 2, y el 0 ahora espera al 3. Ninguno de estos tres nodos podrá alcanzar un grado de entrada de cero, por lo que la cola quedará vacía prematuramente y no habrá orden topológico posible.
2. Probar una dependencia duplicada
    - Ejemplo: Añadir nuevamente la arista `(0, 2)` al grafo original, quedando `(0, 2), (0, 2), (1, 2), (2, 3)`.
    - Explicación lógica: El resultado lógico de la dependencia no cambia porque repetir la instrucción "debes terminar la tarea 0 antes de empezar la 2" no genera ninguna restricción nueva ni altera la relación de tiempo entre ambos nodos. Sigue siendo el mismo requisito. 
    - Impacto en el algoritmo: Mientras el paso de normalización elimine este duplicado para evitar registrar un grado de entrada "fantasma" que bloquee al nodo 2 para siempre, los órdenes válidos seguirán siendo exactamente los mismos: `0, 1, 2, 3` o `1, 0, 2, 3`.

¿Qué significa exactamente el par (2, 5) en ordenar_cursos?
- Significa que el curso 2 es un prerrequisito obligatorio del curso 5.

## CSES Course Schedule
**¿Qué conversiones de índices necesita la adaptación de CSES y qué debe imprimirse si hay ciclo?**
- Necesita restar 1 a los números al leer la entrada y sumar 1 a los resultados antes de mostrarlos. Si hay un ciclo, debe imprimirse la palabra "IMPOSSIBLE".

## LeetCode Course Schedule
**Actividad.** Convierte `[[1,0],[2,0],[3,1],[3,2]]` a nuestra convención y dibuja el DAG. Hay más de un orden válido porque 1 y 2 pueden intercambiarse.
1. Conversión
    - El par `[1,0]` se convierte en `0 → 1`
    - El par `[2,0]` se convierte en `0 → 2`
    - El par `[3,1]` se convierte en `1 → 3`
    - El par `[3,2]` se convierte en `2 → 3`

2. Representación del DAG
```text
      1
    /   \
  0       3
    \   /
      2
```

¿Cómo se relacionan ordenar_cursos, puede_completar_cursos y las preguntas de LeetCode 207/210?
- LeetCode 207 equivale a usar puede_completar_cursos y LeetCode 210 equivale a ordenar_cursos. La única adaptación necesaria es invertir los pares porque LeetCode los escribe al revés [curso, requisito].

## Complejidad
**¿Por qué el bucle anidado sobre nodos y vecinos no implica O(VE)?**
- Porque el algoritmo no repite búsquedas desde cero. Cada nodo entra a la cola una sola vez y cada arista se revisa exactamente una vez en todo el programa, sumando el trabajo en lugar de multiplicarlo.

## Pruebas
**¿Cómo debe probarse un resultado cuando el grafo admite varios órdenes topológicos?**
- No se debe comparar contra una lista fija. Se debe usar una función que verifique las propiedades del resultado: que no falten nodos, que no haya repetidos y que para cada flecha `u → v`, la tarea `u` aparezca antes que `v`.

## Extensión con heap
**¿Qué cambio de contrato justifica sustituir la cola por un heap?**
- Que el problema cambie sus reglas y exija obligatoriamente el orden "lexicográficamente mínimo".

## Cierre
### Síntesis personal — Orden Topológico 
- El problema: Encontrar una secuencia válida para realizar tareas cuando unas dependen de otras.
- La operación principal: Buscar tareas que no tengan requisitos pendientes, procesarlas y descontar ese requisito de las tareas siguientes.
- La estructura de datos: 
    - Un contador para llevar el registro de cuántos requisitos le faltan a cada tarea.
    - Una cola para formar las tareas que ya están desbloqueadas y listas para hacerse.
- El invariante: Una tarea solo puede entrar a la cola si su contador de requisitos pendientes llegó exactamente a cero.
- La complejidad: `O(V + E)`. Es lineal y eficiente porque revisa cada tarea y cada conexión exactamente una vez.
- Caso donde no aplica: Cuando el grafo tiene ciclos. Si la tarea A exige terminar la B, y la B exige terminar la A, el algoritmo se traba porque ninguna llega a cero.
- Comparación con BFS:
    - Este método se parece mucho a BFS porque ambos avanzan usando una cola para procesar los elementos uno por uno.  La diferencia clave está en la regla para meter elementos a esa cola: 
    - En BFS, un nodo entra a la cola en el momento exacto en que lo ves por primera vez.
    - En Kahn, verlo no es suficiente. Un nodo solo entra a la cola cuando todos sus requisitos anteriores ya fueron completamente procesados.

**Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos adecuada?**
- Operación dominante: Analizando cuál es la acción que más veces se va a repetir en el núcleo del problema. 
- Una vez identificada, elegimos la estructura que resuelva esa acción específica al menor costo de tiempo posible.




