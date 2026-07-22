# Clase 15: Notebook
#### Nombre: Patricio Navarro

## Pregunta inicial
¿Cómo encontramos el camino de menor costo cuando las aristas no cuestan lo mismo?
- Partiendo de un punto y eligiendo las aristas que cuesten menos a partir de dicho punto.

## Por qué BFS ya no basta
**Pregunta adicional:** ¿Qué camino elegiría una estrategia que solo compara niveles y cuál debería elegir si optimizamos costo total?
- BFS elegiría el camino directo de `A -> D`, pero si optimizaramos costo total debería de elegir `A → B → D`

¿Por qué contar aristas ya no es suficiente en un grafo ponderado?
- Porque aunque puedas encontrar el camino más corto entre dos nodos, no quiere decir que sea el más óptimo.

## Recordatorio de BFS
¿En qué condición BFS sí garantiza caminos de costo mínimo?
- Cuando todos los caminos valen lo mismo o no están ponderados.

## Red de ciudades conductora
**Actividad manual:** enumera al menos dos caminos de A a E y suma sus pesos. No decidas todavía cuál usará el algoritmo.
1. A -> C -> B -> D -> E = 1 + 2 + 1 + 3 = 7
2. A -> B -> D -> E = 4 + 1 + 3 = 8

¿Qué representan nodos, aristas y pesos en esta red?
- Nodo = Ciudad
- Aristas = Caminos dirigidos entre ellas
- Pesos = Tiempos de viaje

## Distancias tentativas
¿Qué significa infinito en la tabla de distancias?
- Que aún no conocemos un camino.

## Relajación 
¿Qué tres valores comparamos al relajar una arista?
- La distancia del punto actual a un punto `v`.
- La candidata.
- El peso.

## Mejoras sucesivas
¿Por qué actualizar una distancia no obliga a borrar inmediatamente su entrada anterior del heap?
- Porque podrían ser iguales o la anterior podría ser mejor.

## Descubrimiento de la cola de prioridad
¿Qué componente del par funciona como prioridad y cuál como elemento?
- Distancia = prioridad
- Nodo = elemento

## Algoritmo de Dijkstra
¿Qué problema resuelve Dijkstra y qué restricción tienen los pesos?
- Problema: Encontrar caminos mínimos desde un origen con pesos no negativos.
- Los pesos no pueden ser negativos.

## Pseudocódigo y entradas obsoletas
**Actividad:** subraya en el pseudocódigo las tres operaciones que dependen directamente de la Clase 14.
para cada nodo:
    distancia[nodo] = infinito
    predecesor[nodo] = ninguno

distancia[origen] = 0
`insertar (0, origen) en la cola de prioridad`

mientras la cola no esté vacía:
    `extraer (distancia_extraida, actual)`

    si distancia_extraida no coincide con distancia[actual]:
        ignorar esta entrada y continuar

    para cada (vecino, peso) de actual:
        candidata = distancia[actual] + peso
        si candidata < distancia[vecino]:
            distancia[vecino] = candidata
            predecesor[vecino] = actual
            `insertar (candidata, vecino)`

¿En qué momento se ignora una entrada obsoleta?
- Cuando la distancia que sigue es mayor que la que tiene en ese momento.

## Recorrido manual mínimo
¿Cuál es el orden de extracción vigente en el ejemplo mínimo?
- (0, A), (1, B) y (3, C)

## Recorrido manual intermedio
Completa la tabla antes de usar el visualizador:

| Extracción vigente | Mejoras producidas | Distancias después | Predecesores que cambian |
| --- | --- | --- | --- |
| `(0,A)` | B=4, C=1 | A0 B4 C1 D∞ E∞ | B←A, C←A |
| `(1,C)` | B=3, D=6 | A0 B3 C1 D6 E∞ | B←C, D←C |
| `(3,B)` | D=4 | A0 B3 C1 D4 E∞ | D←B |
| `(4,D)` | E=7 | A0 B3 C1 D4 E7 | E←D |
| `(7,E)` | Ninguna | A0 B3 C1 D4 E7 | Ninguno |

- (4, B): ¿4 > 3? Sí -> se ignora
- (6, D): ¿6 > 4? Sí -> se ignora
- (10, E): ¿10 > 7? Sí -> se ignora

¿Cuáles son las distancias finales desde A en la red conductora?
- A0 B3 C1 D4 E7

## Reconstrucción del camino
¿Por qué recorremos predecesores desde el destino y después invertimos?
- Porque cada nodo apunta a su predecesor, entonces para que no regrese `None`, empezamos por nuestro punto de llegada y recorremos la ruta al revés hasta el origen. Así, al invertir la ruta tenemos nuestra ruta ideal de origen a destino.

## Visualización interactiva
**Actividad:** en “Entradas obsoletas”, pausa antes de extraer `(10,B)` y predice la decisión.
- Si pasas por Centonces la distancia a B es 3 en vez de 10, entonces relajas ese camino.

¿Qué tres representaciones deben permanecer sincronizadas en cada paso?
- El heap, el predecsor y las distancias.

## Implementación
¿Qué responsabilidad tiene cada una de las tres funciones de la entrega?
- `dijkstra`: validar pesos, calcular distancias y registrar predecesores.
- `reconstruir_camino`: sigue el mapa.
- `camino_minimo`: coordina ambas y devuelve costo/camino para un destino.

## Complejidad
¿De dónde proviene el factor logarítmico de Dijkstra con heap?
- De la altura del árbol de la cola de prioridad. 

## Problema guiado: Entrega urgente
1. Modelado
```python
{
    "A": [("B", 4), ("C", 1)],
    "B": [("D", 1), ("E", 7)],
    "C": [("B", 2), ("D", 5)],
    "D": [("E", 3)],
    "E": [],
}
```

2. Iniciaización
    - Distancias iniciales: A = 0, B = ∞, C = ∞, D = ∞, E = ∞
    - Predecesores iniciales: A = None, B = None, C = None, D = None, E = None
    - Cola de prioridad inicial: [(0, 'A')]

3. (4 y 5 también)
    - Paso 1: Extraer (0, A) (Vigente)
        - Vecino B: Candidata = $0 + 4 = 4$. 
        Comparación: $4 < \infty$ (Sí). Decisión: B = 4, B ← A. Añadir (4, B)
        - Vecino C: Candidata = $0 + 1 = 1$. 
        Comparación: $1 < \infty$ (Sí). Decisión: C = 1, C ← A. Añadir (1, C).
    - Paso 2: Extraer (1, C) (Vigente)
        - Vecino B: Candidata = $1 + 2 = 3$. Comparación: $3 < 4$ (Sí). Decisión: B = 3, B ← C. Añadir (3, B). (La entrada (4, B) en el heap ahora es obsoleta).
        - Vecino D: Candidata = $1 + 5 = 6$. Comparación: $6 < \infty$ (Sí). Decisión: D = 6, D ← C. Añadir (6, D).
    - Paso 3: Extraer (3, B) (Vigente)
        - Vecino D: Candidata = $3 + 1 = 4$. Comparación: $4 < 6$ (Sí). Decisión: D = 4, D ← B. Añadir (4, D). (La entrada (6, D) en el heap ahora es obsoleta).
        - Vecino E: Candidata = $3 + 7 = 10$. Comparación: $10 < \infty$ (Sí). Decisión: E = 10, E ← B. Añadir (10, E).
    - Paso 4: Extraer (4, B) ENTRADA OBSOLETA 
    Comparación: ¿Distancia extraída ($4$) > Distancia real ($3$)? Sí. Decisión: Ignorar.
    - Paso 5: Extraer (4, D) (Vigente)
        - Vecino E: Candidata = $4 + 3 = 7$. Comparación: $7 < 10$ (Sí). Decisión: ¡Atajo encontrado! Actualizar E = 7, E ← D. Añadir (7, E). (La entrada (10, E) en el heap ahora es obsoleta).
    - Paso 6: Extraer (6, D) ENTRADA OBSOLETA
    Comparación: ¿Distancia extraída ($6$) > Distancia real ($4$)? Sí. Decisión: Ignorar.
    - Paso 7: Extraer (7, E) (Vigente) Nodo destino alcanzado con costo mínimo. No tiene salidas.
    - Paso 8: Extraer (10, E) ENTRADA OBSOLETA
    Comparación: ¿Distancia extraída ($10$) > Distancia real ($7$)? Sí. Decisión: Ignorar.

6. Destino: E
- Predecesor de E: D
- Predecesor de D: B
- Predecesor de B: C
- Predecesor de C: A (Fin)
- Ruta óptima invertida: A → C → B → D → E

Tabla de evidencia:

| Concepto | Resultado que debes completar |
| --- | --- |
| Orden de extracciones vigentes | A, C, B, D, E |
| Mejoras de B | Bajó de 4 (vía A) a 3 (vía C) |
| Mejoras de D | Bajó de 6 (vía C) a 4 (vía B) |
| Mejoras de E | Bajó de ∞ a 10 (vía B), y luego bajó a 7 (vía D) |
| Predecesores finales | B←C, C←A, D←B, E←D |
| Camino A→E | A → C → B → D → E |
| Costo total | 7 minutos |

Comparación:
1. Ruta Directa A → B → E:
    - Siguiendo el camino físico: $4 \text{ (A→B)} + 7 \text{ (B→E)} = 11 \text{ minutos}$.
2. Ruta Alternativa A → C → D → E:
    - Siguiendo el camino físico: $1 \text{ (A→C)} + 5 \text{ (C→D)} + 3 \text{ (D→E)} = 9 \text{ minutos}$.
3. Ruta Óptima de Dijkstra A → C → B → D → E:
    - Costo acumulado real: $1 + 2 + 1 + 3 = 7 \text{ minutos}$.

¿Cuál es el costo y camino mínimo de A a E en la red conductora?
- La ruta óptima `A → C → B → D → E`.

## Limitaciones y pesos negativos
¿Por qué una arista negativa rompe la decisión codiciosa de Dijkstra?
- Porque a la hora de hacer la suma de las distancias habría errores, pues las distancias negativas se restarían en vez de sumarse y el viaje podría ser más largo de lo que marca el algoritmo.

## Pruebas y revisión técnica
¿Qué caso de prueba demuestra que manejamos entradas obsoletas correctamente?
- `test_red_ciudades_calcula_distancias_minimas()`

## Práctica adicional
¿Qué operación dominante indica que un problema puede resolverse con Dijkstra?
- Caminos mínimos con aristas ponderadas.

## Cierre
¿Qué cadena de decisiones transforma el problema ponderado en Dijkstra?
- Cambiar de saltos a costo, eso nos lleva a saltar de FIFO a prioridad, necesitamos entonces comparar distancias y guardarlas en un heap.