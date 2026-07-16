# Notebook clase 19 - Leonardo Daniel Arenas Serafín

## Pregunta inicial

#### **¿Cómo encontramos un orden válido para ejecutar tareas cuando unas dependen de otras?**
Considero que se podría utilizar un árbol en donde se puede notar el orden de dependencia de arriba hacia abajo, donde si la raíz no está disponible, no se puede acceder al subárbol

## 1. Presentación de la clase

#### En el problema de cursos, ¿qué operación necesitamos repetir para construir un plan válido?
Debemos revisar que los requisitos previos para poder continuar con el plan.

## 2. El nuevo problema: dependencias

#### ¿Qué debe ocurrir antes de Proyecto Final y por qué puede haber más de una respuesta correcta?
Se debe de tomar Algoritmos u Optimización como requisito para poder proceder con Proyecto FInal. Puede haber más de una respuesta correcta ya que surge a partir de dos requisitos distintos.

## 3. Interpretación de aristas dirigidas

#### ¿Por qué A → B y B → A representan restricciones diferentes?
Porque a pesar que las une una arista, ésta tiene sentido.

## 4. Qué es un DAG

#### **Actividad.** Clasifica `X → Y`, dos nodos aislados, una autoarista `Z → Z` y `P → Q → R → P`. 
`X → Y` y `Z → Z` son topológicos pues no tienen ciclos, a diferencia de `P → Q → R → P` que sí tiene ciclos, por lo que no es topológico
#### ¿Por qué el ciclo A → B → C → A impide cualquier orden topológico?
Porque un orden topológico no tiene ciclos y este si.

## 5. Ejemplos con y sin ciclos

#### En el grafo mixto, ¿por qué procesar D y E no permite devolver un orden parcial como solución?
Porque simplemente es una parte del grafo completo, el cual sigue bloqueado

## 6. Grado de entrada

| Nodo | Aristas entrantes | Grado |
| --- | --- | ---: |
| Programación | ninguna | 0 |
| Discretas | ninguna | 0 |
| Estructuras | Programación→Estructuras, Discretas→Estructuras | 2 |
| Álgebra | ninguna | 0 |
| Algoritmos | Estructuras→Algoritmos| 1 |
| Optimización | Álgebra→Optimización| 1 |
| Proyecto Final | Algoritmos→Proyecto Final, Optimización→Proyecto Final | 2 |

#### ¿Qué grados de entrada tienen Algoritmos, Optimización y Proyecto Final en el problema conductor?
1, 1 y 2 respectivamente

## 7. Nodos disponibles

#### ¿En qué momento exacto debe encolarse Estructuras de Datos?
Después de que Programación y Discretas fueron procesadas 

## 8. Descubrimiento de Kahn

#### ¿Qué representa disminuir en uno el grado de entrada de un vecino?
Representa que uno de sus requisitos fue procesado.

## 9. Ejecución manual

| Paso | Cola antes | Actual | Vecino | Grado anterior | Grado nuevo | Acción | Orden |
| ---: | --- | --- | --- | ---: | ---: | --- | --- |
| 1 | A, B | A | C | 2 | 1 | sigue bloqueado | A |
| 2 | B | B | C | 1 | 0 | encolar C | A, B |
| 3 | C | C | D | 1 | 0 | encolar D | A, B, C |
| 4 | D | D | — | — | — | terminar | A, B, C, D |

#### Completa los pasos 3 y 4: ¿qué valores y orden final deben aparecer?
A, B, C, D en ese orden.

## 10. Uso de la cola

#### ¿Por qué la solución evaluada usa deque aunque ColaLigada pueda implementar la misma política?
Para no depender de que ya hayamos termiando la clase 17 o no

## 11. Invariantes

#### Actividad de diagnóstico: (a) B está en cola con grado 2; (b) C aparece dos veces en el orden; (c) una dependencia duplicada provoca grado −1; (d) un aislado está en la cola inicial. Los tres primeros violan invariantes; el cuarto es correcto.

(a) Todos los nodos en la cola deben de ser grado 0. (b) Solo se procesa una única vez cada nodo. (c) No pueden haber grados negativos. (d) Ok

#### ¿Qué invariante se viola si un nodo entra a la cola cuando su grado todavía es 1?
Que los nodos en la cola deben tener grado 0

## 12. Implementación paso a paso

#### ¿Qué cuatro estructuras locales necesita mantener orden_topologico y para qué sirve cada una?
grados, una lista con los grados. disponibles, la cola donde va el orden de procesamiento. orde, lista con el orden de procesamiento. noramlizado, función que devuelve un grafo normalizado para que funcione correctamente el algoritmo.

## 13. Detección de ciclos

#### ¿Por qué len(orden) != len(normalizado) es evidencia de un ciclo?
Porque se ha visto que se han procesado más nodos de los que hay, por lo que alguno debió repetirse en algún ciclo.

## 14. BFS frente a Kahn

#### ¿Cuál es la diferencia decisiva entre la regla para encolar en BFS y en Kahn?
Que en BFS se puede encolar un nodo en el cual se llegue por una sola arista, mientras que en Kahn solo se puede encolar si todas sus aristas conectadas han sido procesadas.

## 15. Órdenes no únicos

#### **Actividad.** Enumera todos los órdenes válidos de `A→D`, `B→D`, `C→D`. Resultado: cualquier permutación de A, B y C seguida de D; son seis.
"A,B,C,D", "A,C,B,D", "B,A,C,D" "B,C,A,D", "C,A,B,D", "C,B,A,D"
#### ¿Por qué un test que exige exactamente [A, B, C] es incorrecto para A→C y B→C?
Porque no hay solamente una solución correcta.

## 16. Validación de un orden

#### **Actividad 4 — validar secuencias.** Para `A→C`, `B→C`, clasifica:

| Secuencia | ¿Válida? | Primera razón |
| --- | --- | --- |
| A,B,C | sí | respeta ambas aristas |
| B,A,C | sí | respeta ambas aristas |
| C,A,B | no | tiene grado 2 |
| A,C | no | tiene grado 1 |
| A,A,C | no | no se puede procesar un nodo dos veces |

#### Clasifica las cuatro secuencias incompletas de la tabla y explica la primera regla que falla.
Falla que para que un nodo pueda procesarse debe estar en la cola y eso lo obliga a tener grado 0, mientras aquí tiene grado 2

## 17. Normalización y dependencias duplicadas

#### **Actividad.** Predice claves y listas para `{"A": ("C","C"), "B": []}`. Resultado según primera aparición: A, C, B; C aparece una vez en la adyacencia.
{"A": ("C"), "B": [], "C": []}
#### ¿Por qué una dependencia duplicada no debe aumentar dos veces el grado de entrada?
Porque la normalización solamente permite que haya una dependencia por nodo.

## 18. Casos límite

#### ¿Cómo deben aparecer los nodos aislados en un orden topológico y por qué?
Deben aparecen en cualquier orden, ya que tienen grado 0 y pueden procesarse en el orden que sea.

## 19. Problema de cursos

#### **Actividad.** Añade `(3,0)` y localiza el ciclo. Después prueba una dependencia duplicada y explica por qué el resultado lógico no cambia.
El ciclo está en que se va al curso de índice 0, que es en donde incia, lo cual es un ciclo. en una dependencia duplicada el resultado lógico no cambia ya que la normalización solamente permite que haya una dependencia por nodo.
#### ¿Qué significa exactamente el par (2, 5) en ordenar_cursos?
El primer elemento significa el grado del nodo y el segundo significa el nodo que se libera en índice.

## 20. CSES Course Schedule

#### ¿Qué conversiones de índices necesita la adaptación de CSES y qué debe imprimirse si hay ciclo?
Que n CSES se trabaja con índices del 1 al n y en nuestra implementación del 0 al n-1, por lo que hay que restarle uno al empezar a trabajar con ellos y sumarle uno al finalizar. Se debe de imprimir IMPOSSIBLE si hay ciclo.

## 21. LeetCode Course Schedule

#### **Actividad.** Convierte `[[1,0],[2,0],[3,1],[3,2]]` a nuestra convención y dibuja el DAG. Hay más de un orden válido porque 1 y 2 pueden intercambiarse.
[[0, 1],[0, 2],[1, 3],[2, 3]].      
        1 -> 3
        2 -> 3
#### ¿Cómo se relacionan ordenar_cursos, puede_completar_cursos y las preguntas de LeetCode 207/210?
El orden de la secuencia se invierte y si hay ciclo en vez de None se devuelve []

## 22. Complejidad

#### ¿Por qué el bucle anidado sobre nodos y vecinos no implica O(VE)?
Porque siempre son consecutivas las fases, por lo que nunca se multiplicará sin importar los valores.

## 23. Pruebas

#### ¿Cómo debe probarse un resultado cuando el grafo admite varios órdenes topológicos?
Puede ser exauhsivamente si es que es una prueba que use un grafo pequeño o is es grande, metiendo lo que se puede repetir en un conjunto.

## 24. Extensión con heap

#### ¿Qué cambio de contrato justifica sustituir la cola por un heap?
Significa siempre priorizar el mínimo, lo que significa que el primer elemento debe ser éste. 

## 25. Cierre integrador

#### **Síntesis personal.** Explica el problema, la operación, la estructura, el invariante, la complejidad y un caso donde no aplica. Después compara con el algoritmo anterior que más se le parece.
El problema es poder conocer el orden en el que podemos procesar nodos cuando cada nodo puede tener dependencia de otros. La operación es procesar nodos que tengan grado 0 e ir encolando los que se vuelvan grado 0. la estructura que se usa es una cola para ir procesando los nuevos nodos sin dependencia. La invariante es que la cola siempre mantenga nodos de grado 0. Su complejidad es consecutiva, por lo que es O(V + E). No aplica en casos donde haya ciclos como en A->B->A.
#### Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos adecuada?
Debemos siempre identificar cuál es el orden de prioridad que se da para el procesamiento de elementos.