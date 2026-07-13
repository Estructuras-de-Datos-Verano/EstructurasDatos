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
## 6. Casos LL RR LR RL
## 7. Implementación
## 8. Complejidad
## 9. Pruebas
## 10. Revisión técnica
## 11. Discusión