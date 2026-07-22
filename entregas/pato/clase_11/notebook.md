# Clase 11: Notebook
#### Nombre: Patricio Navarro

## Motivación
¿Qué problema aparece cuando buscamos muchas veces en una lista?
- ¿Cómo podemos descartar los elementos que no nos sirven para encontrar más rápido lo que sí queremos sin tener que recorrer todos losd atos por los que ya pasamos?

## Problemas relacionados: 
Elige uno de estos problemas y explica qué concepto de la clase parece practicar.
- Problema elegido: Subordinates: CSES
- Concepto de clase: Representación y recorrido de grafos

## Conceptos básicos
Dibuja o describe un árbol con raíz, dos hijos y al menos una hoja.
```
                                    A
                                   / \
                                  B   C
                                 /
                                D
```

## Árbol binario de búsqueda
¿Por qué el invariante permite descartar una parte del árbol durante la búsqueda?
- Porque sabes en dónde van a estar colocados los que son mayores y los que son menores, entonces puedes nada mas ir buscando como en el ejemplo del diccionario.

## Búsqueda
En el árbol formado por `8, 4, 10, 2, 6, 9, 12`, busca `9`.
1. Empiezas en `8`, como `9` es mayor te vas al hijo derecho.
2. Estás en `10`, como `9` es menor te vas al hijo izquierdo.
3. Llegaste al `9`.
**Pregunta.** ¿Qué nodos comparas y qué parte descartas en cada paso?
Comparo solo el nodo con sus hijos, y si sé que es menor o mayor, lo demás lo descarto.

## Inserción
```
                                     8
                                   /   \
                                  4     10
                                 / \    / \
                                2   6  9   12
```

## Altura
¿Qué relación hay entre altura y costo de búsqueda?
- Son directamente proporcionales.

## Recorridos
¿Por qué inorden produce valores ordenados en un BST?
- Porque va tomando los valores de cada subárbol de menor a mayor. Entonces devuelve una lista ordenada de menor a mayor.

## Animaciones
¿Qué te ayuda a ver una animación que no se ve tan claro en una lista de valores?
- Te ayuda a ver el proceso y como se van haciendo paso a paso las cosas, por lo que es mucho más ilustrativo y claro.

## Implementación
¿Qué métodos parecen depender naturalmente de recursión?
- La altura y los recorridos.

## Pruebas:
¿Qué problema resuelve `evaluar.py`?
- Verifica que sí exista nuestro archivo de implementacion y arregla la necesidad de checar o modificar el pytest.ini. También ya no tenemos que estar moviendo nuestro archivo de implementación de nuestra carpeta de entregas al de clase 11 y de regreso.

## Patrón descubierto
Explica con tus palabras el patrón descubierto.
- Cuando tienes datos que sí están en un cierto órden, por ejemplo un diccionario, puedes organizar la información de manera que abras el diccionario en cualquier parte. Si la palabra que buscas empieza con una letra de órden menor, entonces te regresas, si es mayor, entonces avanzas. y puedes repetir la misma estrategia hasta encontrarla.

## Cierre
1. ¿Qué ganamos frente a una lista?
    - Buscar un dato es mucho más rápido porque no es necesario revisar todo.
2. ¿Qué propiedad mantiene el BST?
    - Cada nodo solo puede tener dos hijos, el hijo izquierdo debe ser menor y el derecho debe ser mayor.
3. ¿Qué pasa si insertamos datos ordenados?
    - El árbol es como una sola rama, ordenada de menor a mayor o de mayor a menor.
4. ¿Cuándo podría degradarse un BST?
    - Cuando sus entradas ya están ordenadas, porque termina siendo una lista enlazada.
5. ¿Qué problema relacionado puedo practicar?
    - El de Subordinates del CSES.
    - También podríamos trabajar con heap queues según yo.

