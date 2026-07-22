## 1. Presentación de la clase

**Pregunta.** ¿Qué diferencia hay entre modelar una secuencia y modelar relaciones?

Modelar una secuencia implica un orden propia de la misma secuencia, donde a cada elemento sigue otro.. Las relaciones no necesariamente llevan un orden, y pueden funcionar en varias direcciones y relacionarse cada elemento con varios otros.

## 2. Problemas motivadores CSES

1. ¿Qué representa un nodo?
Building Roads. Ciudades.
Counting Rooms. Los muros y pisos.
Labyrinth. Los muros, pisos, inicio y final.
Message Route. Computadoras.
2. ¿Qué representa una arista?
Building Roads. Carreteras.
Counting Rooms. Adyacencia.
Labyrinth. Adyacencia.
Message Route. Conexioes.
3. ¿Es dirigido?
Building Roads. No.
Counting Rooms. No.
Labyrinth. No.
Message Route. No.
4. ¿Es ponderado?
Building Roads. No.
Counting Rooms. No.
Labyrinth. No.
Message Route. No.
5. ¿Qué pregunta algorítmica aparece?
Building Roads. Tener carreteras entre cualesquiera dos ciudades.
Counting Rooms. Contar las habitaciones conociendo sólo los muros y pisos.
Labyrinth. Encontrar la ruta para salir conociendo sólo muros y pisos.
Message Route. Encontrar la mejor ruta entre dos computadoras.

## 3. Lectura de modelado

Completa una tabla como esta en `notebook.md`.

| Problema | Nodo | Arista | Dirigido | Ponderado | Pregunta algorítmica |
| --- | --- | --- | --- | --- | --- |
| Building Roads | Ciudad. | Carretera. | No. | No. | Tener carreteras entre cualesquiera dos ciudades. |
| Counting Rooms | Muros y pisos. | Adyacencia. | No. | No. | Contar las habitaciones conociendo sólo los muros y pisos. |
| Labyrinth | Muros y pisos. | Adyacencia. | No. | No. | Encontrar la ruta para salir conociendo sólo muros y pisos. |
| Message Route | Computadoras. | Conexiones. | No. | No. | Encontrar la mejor ruta entre dos computadoras. |

## 4. Conceptos básicos de grafos

**Pregunta.** Da un ejemplo propio de grafo dirigido y otro de grafo no dirigido.

Grafo dirigido: Un juego de teléfono descompuesto. 
Grafo no dirigido: Carreteras entre ciudades.

## 5. Representaciones de grafos

**Pregunta.** ¿Qué operación te parece más importante en un grafo: listar vecinos o preguntar si existe una arista? ¿Por qué?

Depende. Si necesitamos conocer sobre un nodo específico, adyacencia. Si queremos información sobre el grafo en general, la lista de arista.

## 6. Interfaz común

**Pregunta.** ¿Por qué conviene que `GrafoListaAdyacencia` y `GrafoMatrizAdyacencia` tengan la misma interfaz?
Porque pueden ser hijas de GrafoAbstracto, ya que trabajan con la misma información: nodos y aristas.

## 7. Implementación 1: `GrafoListaAdyacencia`

**Pregunta.** ¿Por qué un `set` ayuda a evitar aristas duplicadas?

Porque los conjuntos no consideran repeticiones.

## 8. Implementación 2: `GrafoMatrizAdyacencia`

**Pregunta.** ¿Qué debe pasar con la matriz cuando agregas un vértice nuevo?

Genera nuevas relaciones entre el nuevo y los viejos, agregando nueva fila y columna.

## 9. Comparación

| Aspecto | Lista de adyacencia | Matriz de adyacencia |
| --- | --- | --- |
| Memoria | satisfactorio | satisfactorio |
| Facilidad de implementación | baja | muy baja |
| Consultar vecinos | sencillo si ya se implementó | raro porque trabaja booleanos |
| Consultar si existe arista | sencillo | medio raro |
| Grafos dispersos | sencillo | mucho false |
| Grafos densos | listas muy largas | mucho true |

## 11. Convertir implementación propia a NetworkX

**Pregunta.** ¿Por qué conviene poder convertir una implementación propia a una biblioteca externa?
Porque nos permite usar algo que ya entendemos para explicar una herramienta más general.

## 12. Diseño de pruebas

**Pregunta.** Diseña al menos dos pruebas propias y explica qué comportamiento verifican.

Test de aristas ausentes: revisa que no se creen aristas no deseadas.
Test de vértices vacíos: revisa que pueda trabajar normalmente con ciertos vértices, mientras deja solos a otros.

## 13. Patrón descubierto

**Pregunta.** Explica con tus palabras el patrón de modelado de relaciones.

Es establecer conexiones entre los datos, según criterios convenientes, usando nodos, que representan los datos, y aristas, que representan las conexiones. El modelo busca guardas estas conexiones entre los datos, centrándose en cómo se relacionan o afectan los unos a los otros.

## 14. Cierre

1. ¿Qué ganamos al modelar relaciones como grafo?

Información sobre las relaciones entre los datos que no depeden de factores como la antigüedad.

2. ¿Cuándo usarías lista de adyacencia?

Cuando necesite conocer las relaciones de un elemento específico.

3. ¿Cuándo usarías matriz de adyacencia?

Cuando necesite conocer los datos más en general.

4. ¿Qué puede ocultar una visualización?

Cierta información sobre los datos y sobre por qué se relacionan.

5. ¿Qué algoritmo necesitaremos para recorrer el grafo?

Un for que varía según lo necesario, ya que podemos iterar sobre vértices o sobre aristas.