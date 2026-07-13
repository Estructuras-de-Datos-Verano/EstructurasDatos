# Clase 14: Discusión
#### Nombre: Patricio Navarro

## 1. Operación dominante.
- Al insertar es el sift-up.
- Al extraer es el sift-down.
## 2. FIFO vs prioridad.
- FIFO sirve para atender filas de gente o tareas conforme llegan, pero por prioridad tú les das un peso distinto y en base a eso atiendes.
## 3. BST/AVL vs heap.
- BST/AVL: Buenas para buscar y hacer recorridos ordenados
- Heap: Bueno para atender de acuerdo a prioridad, buscar mínimos o máximos.
## 4. Propiedad min-heap.
- El padre es menor o igual a sus hijos. Por lo tanto, la raíz es el mínimo global.
## 5. Representación por arreglo.
- Con indexión basada en 0:
    - padre(i) = (i - 1) // 2
    - izquierdo(i) = 2 * i + 1
    - derecho(i) = 2 * (i + 1)
## 6. Sift-up.
1. Insertas un valor al final.
2. Lo comparas con su padre.
3. Si es menor los intercambias.
## 7. Sift-down.
1. Agarras el padre.
2. Lo comparas con sus hijos.
3. Lo intercambias con el más pequeño.
## 8. Complejidad.
- Consultar mínimo (minimo()): $O(1)$ — Solo se lee el índice 0.
- Insertar (insertar()): $O(\log n)$ en el peor caso; $O(1)$ en promedio (la mayoría de las inserciones ocurren en las hojas y no suben muchos niveles).
- Extraer mínimo (extraer_min()): $O(\log n)$ — Requiere que la nueva raíz baje potencialmente hasta el fondo del árbol.
- Construcción del Heap (Heapify): $O(n)$ utilizando el algoritmo de Floyd de abajo hacia arriba.
## 9. Last Stone Weight.
- Este problema de colisión de piedras requiere extraer siempre las dos piedras más grandes. Para resolverlo usando un HeapMin (que extrae los mínimos), se aplica el truco de multiplicar todos los valores de las piedras por $-1$ al insertarlos. De esta forma, el número más grande se convierte en el más negativo (el mínimo matemático) y saldrá primero. Al extraerlos, se vuelven a multiplicar por $-1$ para recuperar su valor real, se calcula la diferencia y el residuo se reinserta nuevamente negado.
## 10. Pruebas propias.
```python
def test_insercion_multiples_cambios():
    """Prueba que un valor pequeño suba múltiples niveles (sift-up) hasta la raíz."""
    
    heap = HeapMin([10, 20, 30, 40, 50, 60, 70])
 
    heap.insertar(5)
    
    assert heap.minimo() == 5
    
    assert heap.valores == [5, 10, 30, 20, 50, 60, 70, 40]
    assert heap.cumple_propiedad_heap() is True

def test_extraccion_multiples_descensos():
    """Prueba que al extraer, la nueva raíz baje más de un nivel (sift-down)."""

    heap = HeapMin([5, 10, 15, 20, 25, 30, 35])

    minimo_extraido = heap.extraer_min()

    assert minimo_extraido == 5

    assert heap.minimo() == 10

    assert heap.valores == [10, 20, 15, 35, 25, 30]
    assert heap.cumple_propiedad_heap() is True

def test_ultima_piedra_casos_extremos():
    """Verifica el comportamiento de ultima_piedra ante entradas inusuales."""

    assert ultima_piedra([]) == 0

    assert ultima_piedra([42]) == 42

    assert ultima_piedra([100, 2, 1, 1]) == 96

    assert ultima_piedra([10, 10, 10, 10, 5]) == 5
```
## 11. Revisión técnica.
## 12. Relación con Dijkstra.
- El algoritmo de Dijkstra calcula el camino más corto en un grafo. En cada paso, requiere seleccionar el vértice no visitado con la menor distancia tentativa.
## 13. Pregunta abierta: ¿qué operación haría preferible otra estructura?
- Buscar un elemento cualquiera o recorrer los datos ordenados.