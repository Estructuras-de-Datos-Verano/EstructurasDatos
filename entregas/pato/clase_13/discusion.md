# Clase 13: Discusión
#### Nombre: Patricio Navarro

## 1. Problema que resuelve AVL
- Árboles degenerados.
## 2. Factor de balance
- Herramienta para decidir hacia donde se necesitan las rotaciones y si el arbol esta balanceado.
## 3. Rotaciones e invariante BST
- Hay rotaciones a la izquierda y a la derecha, las rotaciones dobles creo que pueden ser alg contraintuitivas pero muy útiles, ayudan a que el árbol siempre se mantenga balanceado y en su estructura definida.
## 4. Casos LL RR LR RL
- LL: rotación derecha
- RR: rotación izquierda
- LR: rotación izquierda y luego derecha
- RL: rotación derecha y luego izquierda
## 5. Complejidad
- O(log(n)), porque asegura que el peor caso siempre sea un BST.
## 6. Pruebas propias
```python
def test_insercion_descendente():
    """Insertar una secuencia descendente no debe degenerar el AVL."""
    
    arbol = construir([50, 40, 30, 20, 10])
    assert arbol.inorden() == [10, 20, 30, 40, 50]
    assert arbol.altura() == 3
    assert arbol.esta_balanceado()

def test_insercion_valores_negativos():
    """El AVL debe manejar correctamente números negativos y el cero."""
    
    arbol = construir([0, -10, 5, -20])
    assert arbol.contiene(-10)
    assert arbol.contiene(0)
    assert not arbol.contiene(-5)
    assert arbol.inorden() == [-20, -10, 0, 5]
    assert arbol.esta_balanceado()

def test_alturas_internas_nodos():
    
    arbol = construir([20, 10, 30, 40])
    
    assert arbol.raiz is not None
    assert arbol.raiz.valor == 20
    assert arbol.raiz.altura == 3
    assert arbol.raiz.izquierdo is not None
    assert arbol.raiz.izquierdo.valor == 10
    assert arbol.raiz.izquierdo.altura == 1
    assert arbol.raiz.derecho is not None
    assert arbol.raiz.derecho.valor == 30
    assert arbol.raiz.derecho.altura == 2
    assert arbol.raiz.derecho.derecho is not None
    assert arbol.raiz.derecho.derecho.valor == 40
    assert arbol.raiz.derecho.derecho.altura == 1
    assert arbol.esta_balanceado()
```
## 7. Revisión técnica recibida
## 8. Revisión técnica realizada
## 9. Pregunta abierta
¿Qué sistemas se apoyan de árboles AVL para resolverlos? ¿Hay alguna estructura que sea mejor en general que esta?