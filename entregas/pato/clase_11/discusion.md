# Clase 11: Discusión
#### Nombre: Patricio Navarro

## 1. Lista vs árbol
- Un árbol es mucho más eficiente para buscar datos, porque puedes disponer de algunos e ir acotando tu área de búsqueda, mientras que en una lista tienes que recorrer a todos.
## 2. Motivación del BST
- Encontrar una forma de deshacernos de la información que no nos sirve para optimizar búsquedas.
## 3. Invariante
- El nodo supremo es la raíz, los hijos a la izquierda de cada nodo son menores y los hijos a la derecha de cada nodo son mayores.
## 4. Inserción
- Tienes que comparar donde ya hay dos hijos, y donde no, si el dato es mayor o menor para acomodarlo comohijo izquierdo o derecho.
## 5. Recorridos
- Tres formas:
    - Inorden: izquierda -> raíz -> derecha. Regresa una lista con los datos ordenados de menor a mayor.
    - Preorden: raíz -> izquierda -> derecha. Regresa la lista en el órden en que se creó el árbol.
    - Postorden: izquierda -> derecha -> raíz. Regresa la lista con el árbol de abajo a arriba.
## 6. Altura y eficiencia
- La altura va por niveles, como una torre o un edificio. 
- En tanto a la eficiencia requiere más operaciones porque sí hay que revisar y ordenar la información pero acomoda más bonito la información para buscar datos.
## 7. Pruebas
- 
```python
def construir_arbol_base() -> ArbolBinarioBusqueda:
    """Construye un BST con varios niveles."""

    arbol = ArbolBinarioBusqueda()
    for valor in [8, 4, 10, 2, 6, 9, 12]:
        arbol.insertar(valor)
    return arbol

def test_inorden():
    arbol = construir_arbol_base()
    assert arbol.inorden() == [2, 4, 6, 8, 9, 10, 12]

def test_altura_entradas_nones():
    arbol = ArbolBinarioBusqueda()
    for valor in [4, 5, 7, 2, 3, 6, 9]:
        arbol.insertar(valor)
    assert arbol.altura() == 4

def test_postorden_inorden_con_dos_arboles():
    arbol1 = ArbolBinarioBusqueda()
    for valor in [8, 4, 10, 2, 6]:
        arbol1.insertar(valor)

    arbol2 = ArbolBinarioBusqueda()
    for valor in [4, 2, 8, 6, 10]:
        arbol2.insertar(valor)

    assert arbol1.postorden() != arbol2.postorden()
    assert arbol1.inorden() == arbol2.inorden()
```
## 8. Cambio técnico: evaluar.py
- Fue más práctico para crear el reporte del pytest porque ya no era necesario mover el archivo de implementación de un lado a otro.
## 9. Problemas relacionados
- Subordinates, búsqueda en diccionarios, para filtrar información demográfica por edad me imagino que también funciona.
## 10. Pregunta abierta
- ¿Hay estructuras que se basen o que tal cual usen los BST como cimientos, por así decirlo, para después optimizar las demás operaciones como la inserción?