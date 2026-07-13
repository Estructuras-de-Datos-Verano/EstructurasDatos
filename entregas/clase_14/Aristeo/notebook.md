# Notebook
## 1. Motivación
### Si llegan muchas tareas mientras también atendemos tareas urgentes, ¿qué desventaja tendría mantener toda la lista siempre ordenada?

### ¿Qué operación domina en dos de estos escenarios?

## 2. Operación dominante
### ¿Qué costo se repite si extraemos mínimos desde una lista sin ordenar?

## 3. Cola FIFO vs cola de prioridad
### ¿Cuándo sería incorrecto usar una cola FIFO?

## 4. Descubrimiento manual
### Completa la fila correspondiente a insertar `9` y explica por qué se detiene la reparación.
| Valor que llega | Arreglo provisional | Comparación necesaria | Arreglo después de reparar | Intercambios |
| ---: | --- | --- | --- | ---: |
| 7 | `[7]` | no tiene padre | `[7]` | 0 |
| 3 | `[7, 3]` | `3 < 7` | `[3, 7]` | 1 |
| 9 | | | | |
| 1 | | | | |
| 6 | | | | |
| 5 | | | | |
### ¿Qué permanece estable después de insertar un valor?
## 5. Qué es un heap
### ¿Por qué un heap no es un BST?
## 6. Propiedad de min-heap
### ¿Los hermanos deben estar ordenados entre sí?
## 7. Árbol binario completo
### ¿Qué ventaja da esta forma para almacenar el árbol?
## 8. Representación por arreglo
### Para `[2, 5, 4, 9]`, ¿qué valor está en el índice 2?
## 9. Fórmulas de índices
### ¿Cuáles son los hijos del índice 2?
## 10. Inserción
### Si insertas `1` en `[2, 5, 4, 9, 8, 7]`, ¿con qué valores esperas que se compare antes de llegar a su posición final?
...
### ¿Por qué no insertamos directamente en la raíz?
## 11. Sift-up
### ¿Cuándo se detiene sift-up?
## 12. Extracción del mínimo
### ¿Por qué se mueve el último elemento?
## 13. Sift-down
### ¿Por qué debemos elegir el hijo menor?
## 14. Visualizaciones ipywidgets
### ¿Qué relación observas entre la celda del arreglo y el nodo resaltado?
## 15. Comparación BST, AVL y heap
### ¿Qué estructura elegirías para cada escenario y qué operación justifica tu decisión?
...
### ¿Qué elegirías para búsquedas arbitrarias y qué para extraer mínimos?
...
## 16. Complejidad
### ¿Por qué sift-up y sift-down son logarítmicos?


