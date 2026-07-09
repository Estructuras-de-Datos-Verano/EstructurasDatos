# Discusión técnica clase 12 - Leonardo Daniel Arenas Serafín

## 1. ¿Un BST siempre es eficiente?
No siempre, cuando tenemos un árbol degenerado tiene la misma eficiencia de una lista

## 2. Lista vs BST
La lista siempre es menos eficiente porque en la lista el único criterio de orden que hay es la secuencia, mientras que en BSt no solo tenemos secuencia sino también se considera el propio valor del elemento. Esto nos proporciona mucha mayor eficiencia al querer buscar elementos en una estructura, excepto en el caso de un árbol degenerado, donde es lo mismo.

## 3. Altura y comparaciones
El límite de comparaciones que se puede hacer en un árbol al buscar un valor es la altura del árbol. Por lo que se podría decir que la complejidad de dicha operación es la altura, la cual siempre será menor que el número de nodos, a diferencia de la lista, la cual su complejidad es su longitud, sin embargo cuando tenemos un árbol degenerado su complejidad es la misma que la de una lista.

## 4. Árbol balanceado vs árbol degenerado
El árbol balanceado es el caso ideal, es el mejor de los casos en los que puedes hacer esta estructura, mientras que el árbol degenerado es el peor de los casos. 

## 5. Orden de inserción
Para evitar crear un árbol degenerado es cierto que el propio valor de los elementos a insertar cambia drásticamente la estructura del árbol, sin embargo no es la única variable que entra en juego. El orden de inserción también juega un papel importante a la hora de estructurar el árbol.

## 6. Complejidad

La complejidad de un árbol tiende a ser O(log n) cuando tiende a ser un árbol balanceado y tiende a ser O(n) cuando tiende a ser un árbol degenerado.

## 7. Experimentos y evidencia
Se realizó el siguiente experimento: 
```python
valores_balanceados = [8, 4, 12, 2, 6, 10, 14]
valores_degenerados = [1, 2, 3, 4, 5, 6, 7]
objetivos = [2, 6, 10, 14]

print('Usa estos datos para comparar altura y comparaciones en tu implementación.')
print('Balanceado:', valores_balanceados)
print('Degenerado:', valores_degenerados)
print('Objetivos sugeridos:', objetivos)

from implementacion import *

arbol_b = ArbolBinarioBusqueda()
arbol_d = ArbolBinarioBusqueda()

for v in [8, 4, 12, 2, 6, 10, 14]:
    arbol_b.insertar(v)
for v in [1, 2, 3, 4, 5, 6, 7]:
    arbol_d.insertar(v)
for v in [2, 6, 10, 14]:
    print("Balanceado: objetivo", v, ":", arbol_b.comparaciones_busqueda(v))
    print("Degenerado: objetivo", v, ":", arbol_d.comparaciones_busqueda(v))
```
        Usa estos datos para comparar altura y comparaciones en tu implementación.
        Balanceado: [8, 4, 12, 2, 6, 10, 14]
        Degenerado: [1, 2, 3, 4, 5, 6, 7]
        Objetivos sugeridos: [2, 6, 10, 14]
        Balanceado: objetivo 2 : 3
        Degenerado: objetivo 2 : 2
        Balanceado: objetivo 6 : 3
        Degenerado: objetivo 6 : 6
        Balanceado: objetivo 10 : 3
        Degenerado: objetivo 10 : 7
        Balanceado: objetivo 14 : 3
        Degenerado: objetivo 14 : 7

Esto deja en evidencia que el número de comparaciones para encontrar un valor en un árbol degenerado vs un árbol balanceado no depende totalmente de su balance, sino que también depende de los propios valores de los árboles.

## 8. Animaciones
Las animaciones fueron muy útiles para visualizar cómo es que un árbol se crea y cómo sus valores y el orden de inserción afectan en la estructura del árbol.

## 9. Pruebas propias

Yo diseñé las siguientes pruebas TODO: test_todo_busqueda_balanceada(), test_todo_busqueda_degenerada(), test_todo_insercion_ordenada_altura_maxima(). Y por mi propia cuenta implementé las siguientes pruebas: test_arbol_balanceado_altura_no_es_num_nodos_LEO(), test_busqueda_en_arbol_vacio_es_0_LEO(), test_arbol_vacio_no_es_degenerado_LEO()

## 10. Revisión técnica del PR

...

## 11. Problemas relacionados

Subordinates: Este problema se trata acerca de que representamos la estructura de una compañía como un árbol, el cúal es la estructura de poder. Este problema busca saber cuál es el número de subordinados de un empleado. Para hacer esto, primero necesitamos aplicar el método de contiene() para primero encontrar al empleado buscado. Posteriormente debemos de tomar al empleado encontrado como la raíz de su subárbol, para después aplicarle el método de cantidad_nodos() para ver cuántos nodos hay en dicho subárbol y así obtener el número de subordinados. 
 Tal vez relacionado con este problema, podría ponerse a prueba el contar_nodos() a partir de un subárbol.

## 12. Pregunta abierta
Hasta ahoa hemos visto solo un tipo de árbol, el BST, pero ¿cuáles otros tipos de árboles existen?