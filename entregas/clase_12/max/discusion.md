# Discusión técnica

## 1. ¿Un BST siempre es eficiente?

Por lo que se menciona en la clase no, cuando un arbol es muy pequeño el código se puede llegar a romper, ademas si es de tipo degenerado es lo mismo que haberlo echo con listas pero a diferencia de las listas tenemos que hacer todos los metodos y clases abstractactas.

## 2. Lista vs BST

La lista no es tan efectiva a comparación del BTS, ya que las listas no tienen esta función de jerarquización de los nodos, luego, esto de no tener jerarquias genera bastantes problemas a la hora de efecienciar el programa, ya que de echo lo hace bastante más lento.

## 3. Altura y comparaciones

Las altura esta relacionada con la comparación, ya que entre mayor sea la altura tendremos un mayor número de comparaciones, y por lo tanto tendremos un algoritmo que resuelve un problema más complejo, por eso es muy importante tenes en cuenta la altura, ademas si tenemos n nodos y la altura es n, esto quiere decir que tenemos una lista. (Para n en los naturales positivos, que sea al menos no a lo más el nulo).

## 4. Árbol balanceado vs árbol degenerado

El arbol balanceado es la estructura con la que ya estamos familiarizados de arbol, la que parece como unas raices que empieza en un nodo principal y van descendiendo en cada rama.

## 5. Orden de inserción

El orden de inserción es bastante importante en los arboles, y más aun en los arboles degenerados, ya que en los normales por la forma en la que definimos la función insertar los iba acomodando poco a pcoco, ahora en los degenerados como se comporta como lista, no es lo mismo decir el arbol 123 que el 321.

## 6. Complejidad

Como ya vimos la complejidad de los arboles balanceados es de O(logn) ya que va creciendo muy gradualmende dependiendo de la altura del arbol, mientras que en los degenerados, como se comporta como una lista la complejidad se mantiene constante.

## 7. Experimentos y evidencia

```python
valores_balanceados = [8, 4, 12, 2, 6, 10, 14]
valores_degenerados = [1, 2, 3, 4, 5, 6, 7]
objetivos = [2, 6, 10, 14]

print('Usa estos datos para comparar altura y comparaciones en tu implementación.')
print('Balanceado:', valores_balanceados)
print('Degenerado:', valores_degenerados)
print('Objetivos sugeridos:', objetivos)

valores_balanceados = [8, 4, 12, 2, 6, 10, 14]
valores_degenerados = [1, 2, 3, 4, 5, 6, 7]
objetivos = [2, 6, 10, 14]

arbol_balanceado = None
for v in valores_balanceados:
    arbol_balanceado = insertar(arbol_balanceado, v)

arbol_degenerado = None
for v in valores_degenerados:
    arbol_degenerado = insertar(arbol_degenerado, v)
```

Los experimentos que realizamos en el notebook nos ayudan para observar claramente que el tipo de arbol que vayamos a generar afecta a la hora de hacer la implementación, con esta información yo consideraria importante generar un arreglo, función o metodo que sea capaz de decirnos que tipo de arbol es, ya que con esta información podemos tomar decisiones

## 8. Animaciones

Las animaciones sirvieron para tener una referencia visual de todo lo que esta pasando de fondo, así que como herrmienta intuitiva se me hace muy buena, ademas de que a la larga uno puede recordar estas animaciones y así cuando resolvamos otro problema tengamos en mente el como es que funcionan las cosas.

## 9. Pruebas propias

```python
#Acá lo que esta haciendo es que esta construyendo un arbol, y en el esta checando que la altura del arbol sea la correcta.
def test_max1():
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(14)
    arbol.insertar(12)
    arbol.insertar(13)
    arbol.insertar(4)
    arbol.insertar(5)
    assert arbol.altura() == 3

#Acá lo que esta haciendo es que esta intentando que en la busqueda del nodo este si contenga el valor que le debe de corresponder.
def test_max2():
    arbol = construir([8, 4, 12, 2, 6, 10, 14])
    assert arbol.comparaciones_busqueda(3) == 12

#Acá e esta revisando que el arbol se este generando de manera correcta
def test_max3():
    arbol = construir([8, 4, 12, 2, 6, 10, 14, 4])
    assert arbol.cantidad_nodos() == 7
    assert arbol.inorden() == [2, 4, 6, 8, 10, 12, 14]

```
Mis pruebas intentan endorcarse principalmente en que la creación de los arboles se haga correctamente.

## 10. Revisión técnica del PR



## 11. Problemas relacionados

Un problema relacionado que se me ocurre con arboles es el de en una base de datos encontrar el ID de algun profesor en el sistema de la UP, por mencionar un ejemplo el nodo principal seria la Up, un subnodo el campus Mixcoac, otro subnodo la carrera de mátematicas aplicadas, otro subnodo el de la clase de calculo y por ultimo la hoja seria el profesor "Alejandro Dario".

## 12. Pregunta abierta

¿Que ventajas tiene el hacer un arbol degenerado a hacer una lista?