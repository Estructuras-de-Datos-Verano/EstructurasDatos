# Notebook Aristeo
## MotivaciónPregunta 
### ¿Qué operación domina en dos de estos escenarios?
Se prioriza la selección o el retiro constante del componente con el valor más extremo (sea el tope mínimo o máximo).
## 2. Operación dominante
### ¿Qué costo se repite si extraemos mínimos desde una lista sin ordenar?
El proceso exige una inspección lineal exhaustiva cada vez, lo que repite un gasto de tiempo de O(n) por retiro.
## 3. Cola FIFO vs cola de prioridad
### ¿Cuándo sería incorrecto usar una cola FIFO?
Falla cuando el orden de salida no debe depender de quién llegó primero, sino del nivel de urgencia o relevancia del elemento.
## 4. Descubrimiento manual

| Inserción | Arreglo después de sift-up | Intercambios | Mínimo |
| ---: | --- | ---: | ---: |
| 7 | [7] | 0 | 7 |
| 3 | [3, 7] | 1 | 3 |
| 9 | [3, 7, 9] | 0 | 3 |
| 1 | [1, 3, 9, 7] | 2 | 1 |
| 6 | [1, 3, 9, 7, 6] | 0 | 1 |
| 5 | [1, 3, 5, 7, 6, 9] | 1 | 1 |

### ¿Qué permanece estable después de insertar un valor?
La mayoría de las conexiones no cambian, la reorganización solo afecta de manera lineal a la ruta que va desde el nuevo nodo hasta la raíz.
## 5. Qué es un heap
### ¿Por qué un heap no es un BST?
A diferencia del BST, el heap maneja una organización jerárquica parcial (los padres son menores que sus hijos) y no sirve para búsquedas aleatorias veloces.
## 6. Propiedad de min-heap
### ¿Los hermanos deben estar ordenados entre sí?
No hay una regla horizontal; la restricción es puramente vertical y condiciona solo la relación directa entre padre e hijo.
## 7. Árbol binario completo
### ¿Qué ventaja da esta forma para almacenar el árbol?
Permite un almacenamiento compacto en memoria secuencial, eliminando espacios vacíos y facilitando el cálculo de posiciones mediante aritmética básica.
## 8. Representación por arreglo
### Para [2, 5, 4, 9], ¿qué valor está en el índice 2?
Bajo un conteo que inicia en cero, la posición dos corresponde estrictamente al número 4.
## 9. Fórmulas de índices
### ¿Cuáles son los hijos del índice 2?
Al aplicar las reglas de derivación para la posición dos:
- Hijo izquierdo: índice 5 (2 × 2 + 1)
- Hijo derecho: índice 6 (2 × 2 + 2)
## 10. Inserción
### ¿Por qué no insertamos directamente en la raíz?
Hacerlo rompería la simetría del árbol y obligaría a mover todos los datos. Colocarlo al final protege la estructura y reduce el ajuste a una sola ruta.
## 11. Sift-up
### ¿Cuándo se detiene sift-up?
El ascenso concluye cuando el nodo llega a la raíz o encuentra un elemento superior que ya es menor o igual a él.
## 12. Extracción del mínimo
### ¿Por qué se mueve el último elemento?
Se traslada a la cima para conservar intacta la silueta del árbol; de este modo, solo se desajusta el orden numérico, el cual se corrige bajando.
## 13. Sift-down
### ¿Por qué debemos elegir el hijo menor?
Garantiza que el elemento reubicado como nuevo padre respete la jerarquía, quedando por debajo de los dos nodos inferiores.
## 14. Visualizaciones ipywidgets
### ¿Qué relación observas entre la celda del arreglo y el nodo resaltado?
Tienen un vínculo idéntico de uno a uno; la lista y el gráfico del árbol representan exactamente los mismos datos bajo dos formatos visuales.
## 15. Comparación BST, AVL y heap
### ¿Qué elegirías para búsquedas arbitrarias y qué para extraer mínimos?
Para localizar cualquier dato conviene un BST o AVL, mientras que para consultar y remover mínimos de forma inmediata es preferible un min-heap.
## 16. Complejidad
### ¿Por qué sift-up y sift-down son logarítmicos?
Dado que la altura de este árbol está limitada a O(log n), las rutinas de ajuste operan únicamente sobre los nodos de esa línea vertical
## 17. Last Stone Weight
### ¿Cuál es la operación dominante y el resultado del ejemplo?
La acción principal consiste en retirar el valor más alto del conjunto; el desenlace final del ejercicio planteado equivale a 1.
## 18. Pruebas
### ¿Qué error específico detecta una extracción con varios descensos?
Evidencia fallas en el método de bajada, como omitir la comparación entre los dos hijos o frenar el descenso antes de estabilizar todo el árbol.
## 19. Revisión técnica
### ¿Qué debe incluir revision_nombre_revisor.md?
Debe registrar la ejecución de los casos de prueba, el diagnóstico de fallos, el reconocimiento del código bien estructurado y sugerencias de mejora.
## 20. Preparación para Dijkstra
### ¿Qué guardaría la prioridad en Dijkstra?
Almacena temporalmente los costos acumulados o trayectorias estimadas más bajas hacia los nodos que faltan por inspeccionar.
## 21. Cierre
### ¿Qué criterio usarás para elegir una estructura en un problema nuevo?
La regla de oro es auditar las necesidades del algoritmo para descubrir el proceso repetitivo clave y emparejarlo con la estructura que lo resuelva más rápido