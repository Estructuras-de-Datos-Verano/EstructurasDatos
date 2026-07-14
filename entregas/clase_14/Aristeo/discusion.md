# Discusion
## Operación dominante y complejidad
Los heaps optimizan la inserción y el retiro del valor extremo. Mientras que una lista tradicional requiere un costoso recorrido lineal de O(n) para hallar el mínimo, el heap reduce este gasto a O(log n) gracias a la baja altura de su estructura balanceada.
## FIFO vs prioridad
El orden secuencial por llegada (FIFO) es ineficiente en sistemas operativos o urgencias médicas, donde los eventos críticos exigen atención inmediata. Las colas de prioridad resuelven esto organizando los elementos según su nivel real de importancia.
## BST/AVL vs heap
Los árboles BST y AVL mantienen un orden horizontal estricto para agilizar la localización de cualquier nodo aleatorio. En contraste, el heap aplica una regla vertical parcial que se enfoca únicamente en mantener el elemento óptimo en el nodo raíz.
## Propiedad min-heap
La jerarquía es vertical y parcial: cada padre es menor o igual a su descendencia, sin importar cómo se organicen los hermanos entre sí. Debido a que el árbol se completa de forma simétrica, se mapea en una secuencia contigua mediante cálculos fijos, suprimiendo los punteros y acelerando el acceso en caché.
## Representación por arreglo
La simetría de un árbol completo facilita su traducción a una lista secuencial indexada. Las posiciones de los descendientes se calculan directamente mediante las operaciones 2*i + 1 y 2*i + 2, lo que descarta el uso de referencias de memoria y aprovecha mejor la caché física.
## Sift-up
Este ajuste se activa al colocar un nuevo dato al extremo final del arreglo. El elemento asciende de nivel mediante comparaciones sucesivas con su predecesor, deteniéndose al topar con un valor menor o igual, o al alcanzar la posición inicial.
## Sift-down
Para remover el mínimo sin alterar la silueta del árbol, se traslada el último componente a la cima y se le guía hacia abajo. Es indispensable cambiarlo por el menor de sus hijos para evitar corromper la lógica de orden en la rama contigua.
## Complejidad
Construir el heap desde cero toma un tiempo eficiente de complejidad constante. Por otro lado, cada turno del juego realiza operaciones de extracción e inserción que complejidad logaritmica, lo que nos da un tiempo total impecable de complejidad logaritmica en lugar de tardar demasiado.
## Last Stone Weight
Este escenario requiere recuperar de forma constante los dos pesos más altos. La estrategia ideal consiste en emular un Max-Heap utilizando la estructura original de mínimos, invirtiendo el signo numérico de los elementos al ingresarlos y retirarlos.
## Pruebas propias
``` python
def test_insercion_recorre_varios_niveles_hasta_raiz():
    """
    Caso 1: Inserción con varios intercambios (sift-up).
    Se inserta un valor que es menor a todos los existentes, obligándolo
    a subir desde la última hoja hasta la raíz.
    """
    datos_iniciales = [10, 20, 30, 40, 50, 60]
    heap = HeapMin(datos_iniciales)
    heap.insertar(5)
    
    assert heap.minimo() == 5, "El valor 5 debería ser la nueva raíz"
    assert heap.tamano() == 7
    assert heap.cumple_propiedad_heap(), "La propiedad min-heap se rompió tras subir el 5"

def test_extraccion_desciende_multiples_niveles():
    """
    Caso 2: Extracción con varios descensos (sift-down).
    Se extrae el mínimo y el valor que sube a la raíz es muy grande,
    obligándolo a descender hasta el último nivel posible.
    """
    datos = [1, 10, 20, 100, 110, 120, 130]
    heap = HeapMin(datos)
    minimo_extraido = heap.extraer_min()
    
    assert minimo_extraido == 1
    assert heap.minimo() == 10, "El nuevo mínimo tras extraer 1 debe ser 10"
    assert heap.cumple_propiedad_heap(), "La propiedad se rompió tras bajar el 130"

def test_ultima_piedra_caso_complejo():
    """
    Caso 3: Caso extremo de ultima_piedra.
    Se prueba con una secuencia donde las diferencias generan nuevas 
    piedras que deben reordenarse varias veces en el heap.
    """
    piedras = [10, 8, 7, 6, 5]
    resultado = ultima_piedra(piedras)
    
    assert resultado == 2, "La última piedra debería pesar 2 tras todas las colisiones"

def test_heap_con_muchos_duplicados():
    """
    Caso extra: Verifica que el heap maneje correctamente múltiples
    valores idénticos, manteniendo la estabilidad de la estructura.
    """
    datos = [5, 5, 5, 5, 5]
    heap = HeapMin(datos)
    
    heap.insertar(5)
    assert heap.tamano() == 6
    assert heap.extraer_min() == 5
    assert heap.cumple_propiedad_heap()
```
## Revisión técnica

## Relación con Dijkstra
Dijkstra depende de la selección recurrente del nodo con el menor costo acumulado. Al almacenar pares de datos (distancia, vértice), el heap provee lecturas inmediatas O(1) y retiros en O(log n), impidiendo que el rendimiento caiga al procesar redes complejas.
## Pregunta abierta: ¿qué operación haría preferible otra estructura?
Una operación dentro de una estructura tipo cola, es decir, tipo FIFO.