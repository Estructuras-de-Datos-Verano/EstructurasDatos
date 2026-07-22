# Notebook - Clase 14 - José Iván Reyna Blanco

## Pregunta inicial

**Pregunta:** Si casi nunca necesito buscar cualquier elemento y siempre quiero consultar el menor o el mayor, ¿qué estructura debería usar? Un heap porque permite generar un arreglo de punteros (como una lista) que atiende a los elementos por órdenes de prioridad, de forma tal que se puede acceder a elementos al inicio o final del heap con el mismo costo.

### 1. Motivación

**Pregunta adicional:** Si llegan muchas tareas mientras también atendemos tareas urgentes, ¿qué desventaja tendría mantener toda la lista siempre ordenada? El costo de hacer inserciones y reordenar la lista.

**Pregunta:** ¿Qué operación domina en dos de estos escenarios? Acceder al inicio de la estructura o al final, así como insertar nuevas 'tareas'.

## 2. Operación dominante

**Pregunta:** ¿Qué costo se repite si extraemos mínimos desde una lista sin ordenar? Encontrar/extraer mínimos.

## 3. Cola FIFO vs cola de prioridad

**Pregunta:** ¿Cuándo sería incorrecto usar una cola FIFO? Cuándo quérramos resolver problemas que no tienen un órden fijo. En una cola FIFO se asume que las prioridades van de forma creciente entre los elementos.

## 4. Descubrimiento manual

Antes de formalizar el heap, diseñemos la agenda que necesitamos. Buscamos cuatro propiedades: que el mínimo esté visible, que insertar no obligue a recorrer todo, que extraer no reordene toda la colección y que la representación sea compacta.

Trabajaremos con prioridades `7, 3, 9, 1, 6, 5`. En lugar de ordenarlas por completo, colocaremos cada valor en la siguiente posición disponible y permitiremos intercambios únicamente hacia arriba cuando una prioridad nueva sea menor que su responsable inmediato.

| Valor que llega | Arreglo provisional | Comparación necesaria | Arreglo después de reparar | Intercambios |
| ---: | --- | --- | --- | ---: |
| 7 | `[7]` | no tiene padre | `[7]` | 0 |
| 3 | `[7, 3]` | `3 < 7` | `[3, 7]` | 1 |
| 9 | `[3, 7, 9]` | `9 > 3` | `[3, 7, 9]` | 0 |
| 1 | `[3, 7, 9, 1]` | `1 < 7`, luego `1 < 3` | `[1, 3, 9, 7]` | 2 |
| 6 | `[1, 3, 9, 7, 6]` | `6 > 3` | `[1, 3, 9, 7, 6]` | 0 |
| 5 | `[1, 3, 9, 7, 6, 5]` | `5 < 9` | `[1, 3, 5, 7, 6, 9]` | 1 |

**Pregunta:** ¿Qué permanece estable después de insertar un valor? El órden creciente respecto al mínimo.

## 5. Qué es un heap

**Pregunta:** ¿Por qué un heap no es un BST? Porque aquí el 'nodo' siempre es el primer elemento. El nodo es siempre menor a sus hijos. En un BST hay un órden izquierdo y derecho. 

## 6. Propiedad de min-heap

**Pregunta:** ¿Los hermanos deben estar ordenados entre sí? No, solo han de cumplir ser mayores a su padre.

## 7. BST completo

**Pregunta:** ¿Qué ventaja da esta forma para almacenar el árbol? Tener niveles que pemritan identificar el órden sin almeacenar información adicional de padre-hijos.

## 8. Representación por arreglo

**Pregunta:** Para `[2, 5, 4, 9]`, ¿qué valor está en el índice 2?
Es el 4. En un arreglo ordenado por niveles de izquierda a derecha, la raíz 2 ocupa el índice 0, su hijo izquierdo 5 el índice 1, y su hijo derecho 4 el índice 2.

## 9. Fórmulas de índices

**Pregunta:** ¿Cuáles son los hijos del índice 2?
De acuerdo a los valores dados, sus hijos correspondientes hacia la izquierda y derecha serían el 5 y el 4.

## 10. Inserción

**Pregunta:** Si insertas `1` en `[2, 5, 4, 9, 8, 7]`, ¿con qué valores esperas que se compare antes de llegar a su posición final?
Primero se comparará con el 4 (su nodo padre directo) y luego con el 2 (la raíz), hasta establecerse finalmente en la parte superior.

**Pregunta:** ¿Por qué no insertamos directamente en la raíz?
Porque el objetivo es mantener la propiedad de prioridad del heap, insertando al final y comparando hacia arriba solo con los padres para no desordenar el resto.

## 11. Sift-up

**Pregunta:** ¿Cuándo se detiene sift-up?
Se detiene en el momento en que se alcanza la raíz del árbol o cuando el valor actual es mayor o igual que su padre.

## 12. Extracción del mínimo

**Pregunta:** ¿Por qué se mueve el último elemento?
Al extraer la raíz, el último elemento toma su lugar para mantener la forma del árbol. Luego se ajusta hacia abajo para restaurar el orden correcto de prioridad entre los nodos restantes.

## 13. Sift-down

**Pregunta:** ¿Por qué debemos elegir el hijo menor?
Para no romper la regla del min-heap, que exige dar prioridad a los mínimos. Si subiéramos un hijo mayor, el padre dejaría de ser el menor de todos sus descendientes.

## 14. Visualizaciones ipywidgets

**Pregunta:** ¿Qué relación observas entre la celda del arreglo y el nodo resaltado?
Representan exactamente lo mismo; el arreglo lineal es simplemente la forma en que se almacena en memoria la estructura jerárquica del árbol.

## 15. Comparación BST, AVL y heap

**Pregunta:** ¿Qué estructura elegirías para cada escenario y qué operación justifica tu decisión?
Escenario A: Un AVL, porque mantiene un orden total y permite recorridos ordenados. 
Escenario B: Un heap, ya que optimiza el acceso inmediato al elemento de mayor prioridad o mínimo.

**Pregunta:** ¿Qué elegirías para búsquedas arbitrarias y qué para extraer mínimos?
Elegiría el heap, ya que permite acceder y extraer los mínimos de forma rápida e inmediata, y no depende de un orden estricto total para funcionar.

## 16. Complejidad

**Pregunta:** ¿Por qué sift-up y sift-down son logarítmicos?
Porque cada operación avanza por los niveles del árbol. Al ser un árbol binario con $n$ elementos, su altura máxima es $\log_2(n)$, limitando el número de comparaciones a esa cantidad de niveles.

## 17. Last Stone Weight

**Pregunta:** ¿Cuál es la operación dominante y el resultado del ejemplo?
La operación dominante es la comparación, indispensable para buscar y enfrentar a los dos elementos más grandes. El resultado final del ejemplo es `[1]`.