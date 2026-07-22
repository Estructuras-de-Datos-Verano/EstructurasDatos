# Discusión técnica

## 1. Problema que resuelve AVL
El AVL es un arbol que se balancea a sí mismo, el problema que busca resolver es la optimización de la busqueda en BST mediante un balanceo de este mismo pues hacer una busqueda en un arbol degenerado, un arbol no balanceado nos produce una peridida de recursos al aumentar su complejidad, sobrepasando el ideal de O(logn) llegando incluso a O(n).
## 2. Factor de balance
El factor balance se calcula como ***Factor_Balance = Altura_Izquierda - Altura_Derecha***
## 3. Rotaciones e invariante BST
Las rotaciones son operaciones que modifican los enlaces de los nodos para reducir la altura de un subárbol sin alterar la invariante del BST. 
La invariante del BST dicta que para cualquier nodo con valor X todos los elementos en su subárbol izquierdo deben ser estrictamente menores que X, y todos los elementos en su subárbol derecho deben ser estrictamente mayores que X. Las rotaciones preservan esta propiedad de manera exacta.
## 4. Casos LL RR LR RL
* **Caso LL (Izquierda-Izquierda):** Ocurre cuando un nodo tiene FB = 2 y su hijo izquierdo tiene FB mayor o igual a 0. Significa que el exceso de nodos está en el extremo izquierdo. Se corrige con una **Rotación Simple a la Derecha** sobre el nodo desbalanceado.
* **Caso RR (Derecha-Derecha):** Ocurre cuando un nodo tiene FB = -2 y su hijo derecho tiene FB menor o igual 0. El exceso está en el extremo derecho. Se corrige con una **Rotación Simple a la Izquierda** sobre el nodo desbalanceado.
* **Caso LR (Izquierda-Derecha):** Ocurre cuando un nodo tiene FB = 2 y su hijo izquierdo tiene FB = -1. El desbalance forma un "zig-zag". Requiere una **Rotación Doble**: primero una rotación a la izquierda sobre el hijo izquierdo, transformándolo en un caso LL, y luego una rotación a la derecha sobre el nodo padre desbalanceado.
* **Caso RL (Derecha-Izquierda):** Ocurre cuando un nodo tiene FB = -2 y su hijo derecho tiene FB = 1. Presenta un "zag-zig". Requiere una **Rotación Doble**: primero una rotación a la derecha sobre el hijo derecho (pasando a ser un caso RR) y finalmente una rotación a la izquierda sobre el nodo padre.
## 5. Complejidad
La complejidad debería mantenerse cerca de O(logn)
## 6. Pruebas propias
``` python
def test_rotacion_simple_rr():
    """
    Verifica que una inserción secuencial ascendente (10, 20, 30)
    provoque una rotación simple a la izquierda (Caso RR) y la raíz cambie a 20.
    """
    arbol = ArbolAVL()
    arbol.insertar(10)
    arbol.insertar(20)
    arbol.insertar(30)
    
    assert arbol.raiz.valor == 20
    assert arbol.esta_balanceado()
    assert arbol.inorden() == [10, 20, 30]

def test_rotacion_doble_lr():
    """
    Verifica que el caso Izquierda-Derecha (LR) balancee correctamente el árbol
    mediante una rotación doble (izquierda sobre el hijo, derecha sobre la raíz).
    """
    arbol = ArbolAVL()
    arbol.insertar(30)
    arbol.insertar(10)
    arbol.insertar(20)
    
    assert arbol.raiz.valor == 20
    assert arbol.altura() == 2
    assert arbol.inorden() == [10, 20, 30]

def test_propiedad_inorden_y_balance_masivo():
    """
    Inserta múltiples elementos desordenados y valida que el recorrido inorden
    permanezca perfectamente ordenado y la propiedad AVL se mantenga intacta.
    """
    arbol = ArbolAVL()
    valores = [50, 25, 75, 15, 35, 60, 120, 10, 68]
    
    for v in valores:
        arbol.insertar(v)
        
    assert arbol.esta_balanceado()
    assert arbol.inorden() == sorted(valores)
```
estas fueron las preubas que hice, creo que son buenas verificaciones.
## 7. Revisión técnica recibida
...
## 8. Revisión técnica realizada
Todavía no la hago
## 9. Pregunta abierta
¿ Cómo usarías AVL para resolver problemas de la via diaria?