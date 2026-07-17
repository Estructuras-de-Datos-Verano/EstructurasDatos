Santiago Saldívar

Notebook

## 1. Motivación

**Pregunta:** ¿Qué operación domina en dos de estos escenarios?
Elegir un elemento con prioridad.

## 2. Operación dominante

**Pregunta:** ¿Qué costo se repite si extraemos mínimos desde una lista sin ordenar?
Reordenar la lista.

## 3. Cola FIFO vs cola de prioridad
**Pregunta:** ¿Cuándo sería incorrecto usar una cola FIFO?
Cuando la prioridad no se defina por antigüedad.

## 4. Descubrimiento manual
**Pregunta:** ¿Qué permanece estable después de insertar un valor?
La prioridad para con el mínimo.

**Tabla**
| Inserción | Arreglo después de sift-up | Intercambios | Mínimo |
| ---: | --- | ---: | ---: |
| 7 | 7 | - | 7 |
| 3 | 3 7 | 3 al inicio | 3 |
| 9 | 3 7 9 | 9 al final | 3 |
| 1 | 1 3 7 9 | 1 al inicio | 1 |
| 6 | 1 3 6 7 9 | 6 entre 3 y 7 | 1 |
| 5 | 1 3 5 6 7 9 | 5 entre 3 y 6 | 1 |

## 5. Qué es un heap
**Pregunta:** ¿Por qué un heap no es un BST?
Porque guarda orden parcial. El BTS, no.

## 6. Propiedad de min-heap
**Pregunta:** ¿Los hermanos deben estar ordenados entre sí?
No.

## 7. Árbol binario completo
**Pregunta:** ¿Qué ventaja da esta forma para almacenar el árbol?
Que guarda orden parcial.

## 8. Representación por arreglo
**Pregunta:** Para `[2, 5, 4, 9]`, ¿qué valor está en el índice 2?
4

## 9. Fórmulas de índices
**Pregunta:** ¿Cuáles son los hijos del índice 2?
6, 7

## 10. Inserción
**Pregunta:** ¿Por qué no insertamos directamente en la raíz?
Para conservar la forma completa.

## 11. Sift-up
**Pregunta:** ¿Cuándo se detiene sift-up?
Cuando el valor actual es mayor que el padre.

## 12. Extracción del mínimo
**Pregunta:** ¿Por qué se mueve el último elemento?
Por el shift-up.

## 13. Sift-down
**Pregunta:** ¿Por qué debemos elegir el hijo menor?
Porque va de menor a mayor.

## 14. Visualizaciones ipywidgets
**Pregunta:** ¿Qué relación observas entre la celda del arreglo y el nodo resaltado?
Que el nodo ocupa una celda del arreglo.

## 15. Comparación BST, AVL y heap
¿Qué elegirías para búsquedas arbitrarias y qué para extraer mínimos?
AVL, heap, respectivamente.

## 16. Complejidad
**Pregunta:** ¿Por qué sift-up y sift-down son logarítmicos?
Porque recorren la altura completa del árbol.

## 17. Last Stone Weight
**Pregunta:** ¿Cuál es la operación dominante y el resultado del ejemplo?
Buscar máximos.
[2,4,1,1,1]

## 18. Pruebas
**Pregunta:** ¿Qué error específico detecta una extracción con varios descensos?
***

## 19. Revisión técnica
**Pregunta:** ¿Qué debe incluir `revision_Santiago_Saldivar.md`?
Reportes útiles sobre el código y sugerencias constructivas.

## 20. Preparación para Dijkstra
**Pregunta:** ¿Qué guardaría la prioridad en Dijkstra?
La menor distancia.

## 21. Cierre
**Pregunta:** ¿Qué criterio usarás para elegir una estructura en un problema nuevo?
Conocer qué nos está pidiendo el problema.