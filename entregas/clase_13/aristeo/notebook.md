# Notebook Aristeo
##  Motivación
### ¿por qué un BST básico no garantiza por sí solo búsquedas rápidas?
Porque si no está balanceado ya no jala igual, se nos degenera y se convierte casi que en una lista.
## Degeneración
### ¿qué operación se vuelve costosa cuando el árbol se degenera?
La busqueda, porque entonces ya no elimina la mitad de los casos en cada paso y en el peor de los casos va a tener complejidad O(n)
## Altura y balance
### si un nodo tiene factor de balance `2`, ¿hacia qué lado está cargado?
Hacia la izquierda pq es Izquierda - Derecha, entoces al ser 2 un numero positivo tiene que tener mayor valor el lado izquierdo.
## Ingeniería inversa del algoritmo

### ¿Qué problema intenta resolver AVL?
El deblanceo de un árbol.
### ¿Qué información extra debe recordar cada nodo?
La altura para poder balancearse.
### ¿Qué operación se repite después de insertar?
Calcular la altura.
### ¿Qué propiedad debe conservarse aunque rotemos?
EL orden que nos dicta el BST.
### ¿Cómo detectarías con papel y lápiz que hace falta una rotación?
Restando Altura izquierda con la Altura derecha y ver cuanto distan.
### Escribe pseudocódigo breve de inserción AVL.
fun insertarAVL(nodo, clave):
/1. Inserción normal de un BST
    si nodo es nulo: 
        retornar NuevoNodo(clave)
    si clave < nodo.clave:
        nodo.izquierdo = insertarAVL(nodo.izquierdo, clave)
    sino:
nodo.derecho = insertarAVL(nodo.derecho, clave)
/2. Actualizar la altura de este nodo ancestro
    nodo.altura = 1 + max(altura(nodo.izquierdo), altura(nodo.derecho))
/ 3. Calcular el factor de balance
    balance = altura(nodo.izquierdo) - altura(nodo.derecho)

/ 4. Si está desbalanceado, aplicar rotaciones
/ Caso LL (Izquierda-Izquierda)
    si balance > 1 y clave < nodo.izquierdo.clave:
        retornar rotarDerecha(nodo)

/ Caso RR (Derecha-Derecha)
    si balance < -1 y clave > nodo.derecho.clave:
        retornar rotarIzquierda(nodo)

/ Caso LR (Izquierda-Derecha)
    si balance > 1 y clave > nodo.izquierdo.clave:
        nodo.izquierdo = rotarIzquierda(nodo.izquierdo)
        retornar rotarDerecha(nodo)

/ Caso RL (Derecha-Izquierda)
    si balance < -1 y clave < nodo.derecho.clave:
        nodo.derecho = rotarDerecha(nodo.derecho)
        retornar rotarIzquierda(nodo)
    retornar nodo
...
## Descubrimiento de las rotaciones
### ¿por qué el caso LL se corrige con rotación derecha?
Porque al estar cargado hacia la derecha se tiene que hacer una rotacion a la izquiera, tomando el valor de enmedio como raiz y el de "arriba" como hijo de esa nueva raiz, pero del lado derecho.
### ¿por qué el caso RR es simétrico al caso LL?
Porque de igual forma está degenerado, pero esta vez hacia la derecha, entonces se rota a la izquierda y el caso es análogo al LL, pero cambia de rotación, es basicamente el reflejo del caso LL.
### ¿qué pasaría si intentaras corregir LR con una sola rotación derecha?
No se haría el balance necesario para un BST.
### ¿cómo se refleja RL respecto a LR?
Mismos pasos pero direcciones opuestas
## Complejidad
### ¿qué costo adicional pagamos al insertar para conservar baja la altura?
Pagamos costo adicional en tiempo al ajustar el arbol mediante rotaciones para mantener la altura.
## Pruebas
### Mis pruebas
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
## Revisión técnica
### ¿qué evidencia debe incluir una buena revisión técnica?
Una reflexión o critica constructiva sobre lo revisado, supongo.
## Cierre
### explica en una frase la idea central de AVL como decisión de diseño.
Ir acomodando para que tenga balance y jale el BST.