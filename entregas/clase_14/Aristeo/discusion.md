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
## Last Stone Weight
Este escenario requiere recuperar de forma constante los dos pesos más altos. La estrategia ideal consiste en emular un Max-Heap utilizando la estructura original de mínimos, invirtiendo el signo numérico de los elementos al ingresarlos y retirarlos.
## Pruebas propias
Las verificaciones de control evaluaron el flujo de los ciclos en situaciones críticas donde los nodos requerían desplazarse a través de múltiples niveles, garantizando que el algoritmo de corrección no se interrumpa antes de tiempo.
## Revisión técnica

## Relación con Dijkstra
Dijkstra depende de la selección recurrente del nodo con el menor costo acumulado. Al almacenar pares de datos (distancia, vértice), el heap provee lecturas inmediatas O(1) y retiros en O(log n), impidiendo que el rendimiento caiga al procesar redes complejas.
## Pregunta abierta
