## 1. Motivación

Una lista guarda datos en secuencia. Un árbol organiza datos de forma jerárquica.

Motivación central: tengo muchos datos y necesito buscar muchas veces.

Ejemplos:

- IDs de alumnos;
- matrículas;
- usuarios;
- palabras;
- registros;
- calificaciones;
- claves de acceso;
- números ordenables.

En una lista, buscar puede requerir revisar muchos elementos. En un árbol binario de búsqueda, si la estructura está bien organizada, podemos descartar una parte del espacio en cada paso.

¿Qué problema aparece cuando buscamos muchas veces en una lista?
  - en escencia que perdemos generalidad



## 2. Problemas relacionados

Estos problemas sirven como mapa de práctica y motivación. No los resolveremos todos hoy.

LeetCode:

- 94 Binary Tree Inorder Traversal.
- 144 Binary Tree Preorder Traversal.
- 145 Binary Tree Postorder Traversal.
- 700 Search in a Binary Search Tree.
- 701 Insert into a Binary Search Tree.

CSES:

- [Subordinates](https://cses.fi/problemset/task/1674/): árboles y jerarquías.

**Pregunta.** Elige uno de estos problemas y explica qué concepto de la clase parece practicar.
  - parece usar una estructura de colas por que vemos que el empleado número 1 es el jefe y entre mas va avanzando el número va disminuyendo la cantidad de empleados


## 3. Conceptos básicos

Vocabulario mínimo:

- nodo;
- raíz;
- hijo izquierdo;
- hijo derecho;
- hoja;
- altura;
- subárbol;
- árbol binario.

Un árbol binario es un árbol donde cada nodo tiene como máximo dos hijos.

Dibuja o describe un árbol con raíz, dos hijos y al menos una hoja.
  - imaginemosnos una hoja en blanco con un nodo en la parte superior y dos aristas que salen de el hacia abajo 

Responde esta pregunta en `notebook.md`.

## 4. Árbol binario de búsqueda

Un árbol binario de búsqueda, BST, mantiene este invariante:

Para cada nodo:

- todos los valores del subárbol izquierdo son menores que el valor del nodo;
- todos los valores del subárbol derecho son mayores que el valor del nodo.

En esta clase no permitimos valores repetidos.

**Pregunta.** ¿Por qué el invariante permite descartar una parte del árbol durante la búsqueda?

  - por qwue depende de que etemos trabajando si es con numeros crecientes o decrecientes  

## 5. Búsqueda

Buscar en una lista puede requerir revisar muchos elementos.

Buscar en un BST:

1. comparar con el nodo actual;
2. si el valor es igual, terminar;
3. si el valor es menor, ir al hijo izquierdo;
4. si el valor es mayor, ir al hijo derecho.

**Ejemplo manual.** En el árbol formado por `8, 4, 10, 2, 6, 9, 12`, busca `9`.

**Pregunta.** ¿Qué nodos comparas y qué parte descartas en cada paso?

  - 


## 6. Inserción

Para insertar en un BST seguimos el mismo tipo de decisiones que en búsqueda.

Valores de ejemplo:

```text
8, 4, 10, 2, 6, 9, 12
```

Regla:

- menor: avanzar a la izquierda;
- mayor: avanzar a la derecha;
- repetido: no insertar en esta práctica.

**Pregunta.** Inserta manualmente los valores del ejemplo y describe dónde queda cada uno.

Responde esta pregunta en `notebook.md`.


## 7. Altura

Convención de esta clase:

- árbol vacío: altura 0;
- árbol con solo raíz: altura 1.

La altura importa porque una búsqueda sigue un camino desde la raíz hasta algún nodo o hasta `None`.

**Pregunta.** ¿Qué relación hay entre altura y costo de búsqueda?

Responde esta pregunta en `notebook.md`.


## 8. Recorridos

Tres recorridos clásicos:

- preorden: raíz, izquierda, derecha;
- inorden: izquierda, raíz, derecha;
- postorden: izquierda, derecha, raíz.

En un BST, inorden produce los valores ordenados.

**Pregunta.** ¿Por qué inorden produce valores ordenados en un BST?

Responde esta pregunta en `notebook.md`.

## 9. Animaciones

Los alumnos no programan animaciones en esta clase.

Observa los GIFs:

![Inserción BST](gifs/insercion_bst.gif)

![Búsqueda BST](gifs/busqueda_bst.gif)

![Inorden](gifs/recorrido_inorden.gif)

![Preorden](gifs/recorrido_preorden.gif)

![Postorden](gifs/recorrido_postorden.gif)

**Pregunta.** ¿Qué te ayuda a ver una animación que no se ve tan claro en una lista de valores?

Responde esta pregunta en `notebook.md`.


## 10. Implementación

Implementa en `implementacion.py`:

```python
class Nodo:
    ...

class ArbolBinarioBusqueda:
    def esta_vacio(self) -> bool: ...
    def insertar(self, valor: int) -> None: ...
    def contiene(self, valor: int) -> bool: ...
    def altura(self) -> int: ...
    def inorden(self) -> list[int]: ...
    def preorden(self) -> list[int]: ...
    def postorden(self) -> list[int]: ...
```

No implementes eliminación de nodos en esta clase.

**Pregunta.** ¿Qué métodos parecen depender naturalmente de recursión?

Responde esta pregunta en `notebook.md`.


## 11. Pruebas

Nuevo flujo técnico: los tests públicos importan directamente desde `implementacion.py`.

```python
from implementacion import ArbolBinarioBusqueda, Nodo
```

Para evaluar una entrega usa:

```bash
python3 evaluar.py entregas/clase_11/nombre clase_11/tests
```

El script `evaluar.py` verifica que exista `implementacion.py`, agrega la carpeta de entrega al `PYTHONPATH` y ejecuta internamente `pytest -v`.

Observación. Si necesitas ejecutar pytest directamente porque tu entorno no encuentra el comando, usa:

```bash
python3 -m pytest -v
```

Este comando usa explícitamente el intérprete de Python y suele resolver problemas con múltiples instalaciones o con el `PATH`.

También debes escribir al menos 3 pruebas propias en `test_estudiante.py`.

`notebook.md` contiene respuestas guiadas del notebook. `discusion.md` es un documento técnico y no debe repetir literalmente esas respuestas.

**Pregunta.** ¿Qué problema resuelve `evaluar.py`?

Responde esta pregunta en `notebook.md`.

## 12. Patrón descubierto

Patrón: organización jerárquica para búsqueda.

Preguntas que lo activan:

- ¿Necesito consultar muchas veces si un dato existe?
- ¿Puedo descartar una parte del espacio en cada paso?
- ¿Mis datos tienen una relación de orden?

**Pregunta.** Explica con tus palabras el patrón descubierto.

Responde esta pregunta en `notebook.md`.

## 13. Cierre

Responde en `notebook.md`:

1. ¿Qué ganamos frente a una lista?
2. ¿Qué propiedad mantiene el BST?
3. ¿Qué pasa si insertamos datos ordenados?
4. ¿Cuándo podría degradarse un BST?
5. ¿Qué problema relacionado puedo practicar?

No respondas aquí. Responde en `notebook.md`.