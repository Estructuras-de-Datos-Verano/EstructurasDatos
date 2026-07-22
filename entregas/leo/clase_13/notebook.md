# Notebook - Clase 13 - Leonardo Daniel Arenas Serafín

## 1. Motivación

#### ¿por qué un BST básico no garantiza por sí solo búsquedas rápidas?
Porque puede convertirse en un árbol degenerado que se comporta igual que una lista.

## 2. Degeneración

#### ¿qué operación se vuelve costosa cuando el árbol se degenera?
La operación de búsqueda, pues el número de comparaciones crece muchísimo.

## 3. Altura y balance

#### si un nodo tiene factor de balance `2`, ¿hacia qué lado está cargado?
Hacia la izquierda, porque un árbol no puede tener altura negativa, y el cálculo de balance es una resta de enteros no negativos, por lo que si el número es positivo, significa que el lado izquierdo es el cargado.

## 4. Factor de balance

#### ¿Qué problema intenta resolver AVL?
Que si solo existe un nodo en todo el árbol con dos hijos, no pase desapercibido como no degenerado, intenta medir más a fondo el balance

#### ¿Qué información extra debe recordar cada nodo?
Cuál es su subárbol asociado

#### ¿Qué operación se repite después de insertar?
Medir la altura

#### ¿Qué propiedad debe conservarse aunque rotemos?
La altura

#### ¿Cómo detectarías con papel y lápiz que hace falta una rotación?
Si vemos que el árbol está muy alto.

#### Escribe pseudocódigo breve de inserción AVL.

    Si nodo es nulo:
        regresar nuevo nodo

    Si valor < nodo.valor:
        insertar en el hijo izquierdo
    Si valor > nodo.valor:
        insertar en el hijo derecho
    Si valor == nodo.valor:
        regresar nodo

    actualizar altura del nodo
    calcular factor de balance

    Si está desbalanceado:
        aplicar la rotación

    regresar nodo

## 5. Rotaciones

### - Caso LL
#### ¿Qué observas que cambia en la forma del subárbol?
Que los subárboles asociados a cada nodo se comportan como un árbol completo al cual se le aplican los métodos de árbol
#### ¿Cómo se obtiene el factor `+2` del nodo 30?
Se resta la altura del lado derecho con el izquierdo, y como 2>1, se reacomodan los árboles
#### ¿Por qué la corrección es una rotación derecha?
Porque como el lado izquierdo es más alto, así se balancea para equilibrarlo con el derecho
#### ¿Por qué el inorden debe ser `10, 20, 30` antes y después?
Porque no se modifica el orden, pues este es inherente a la estructura de árbol

### - Caso RR
#### ¿Qué parte del árbol permanece estable en el nivel 2?
Los valores de dicho nivel se quedan estables pues ya están ordenados, popr lo que no hay que realizar cambios
#### ¿Por qué el factor de balance es negativo?
Se resta la altura del lado derecho con el izquierdo, y como el izquierdo es mayor, se vuelve negativo
#### ¿Por qué la corrección es una rotación izquierda?
Porque como el lado derecho es más alto, así se balancea para equilibrarlo con el izquierdo
#### Comprueba el inorden antes y después de rotar.
Antes de la rotación no hay orden en los datos, pero al rotar todo se acomoda para evitar caer en una degeneración y el inorden y en general todo funciona correctamente

### - Caso LR
#### ¿Qué nodo ocupa la posición interior que obliga a usar dos pasos?
El que está en medio de los 3 nodos, se obliga a hacer 2 pasosa pues primero hay que hacer una rotación izquierda y luego una derehca
#### ¿Cuál es el factor del nodo 30 cuando se detecta LR?
Es la raíz del subárbol sobre el cuál se aplicarán las rotaciones
#### ¿Qué corrige la primera rotación y qué corrige la segunda?
la primera corrige la posición interior y la segunda lo pone en orden de la nueva raíz
#### Verifica el inorden en los tres estados de la tabla.
No cambia nada

### - Caso RL
#### ¿En qué sentido RL es el espejo de LR?
En el sentido de que hace exactamente lo mismo pero en orden invertido
#### ¿Por qué el factor del nodo 10 es `-2`?
POrque el árbol tiene una inclinación haca la derecha, y al restar queda negativo
#### ¿En qué orden se aplican las dos rotaciones?
Primero derecha y luego izquierda
####  Explica por qué el inorden no cambia.
Porque la raíz sigue siendo la misma, y el cambio deja el orden de aparición igual, solo cambia la estructura

## 6. Comparación entre BST y AVL

#### ¿en qué momento se separan claramente las alturas y qué trabajo adicional realiza AVL?
Cuando a la cuarta iteración se da una diferencia de alturas, lo cual permite aplicar los métodos de AVL

## 7. Complejidad

#### ¿qué costo adicional pagamos al insertar para conservar baja la altura?
EL costo de hacer una comparación adicional a la hora de insertar para verificar la estrcutura y el acomodo

## 8. Revisión técnica

#### ¿qué evidencia debe incluir una buena revisión técnica?
La salida de pytest -v de los tests públicos y los propios con buen feedback e interpretación. Conclusión

## 9. Discusión

#### explica en una frase la idea central de AVL como decisión de diseño.
AVL permite tener un orden mucho más profundo que facilite realizar un análisis binario.