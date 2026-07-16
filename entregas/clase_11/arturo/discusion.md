## 1. Lista vs árbol
    Una lista es una forma de almacenar datos linealmente, mientras que el arbol es especializapo en poder ver los datos en un diagrama, para bsuqueda el arbol es muy bueno psiempre y cuando no siga un orden lineal como el de una lista, pues para cada paso se pueden desechar muchos datos en la busqueda
## 2. Motivación del BST
    la necesidad de una forma de deschar mucha infromacion con pocos casos
    
## 3. Invariante
    El invariante de esta estrcutura es que 

    - todos los valores del subárbol izquierdo son menores que el valor del nodo;
    - todos los valores del subárbol derecho son mayores que el valor del nodo.

    Por lo que el arbol debe de seguir un orden para cada subarbol posible
## 4. Inserción
    PAra insertar un dato en el arbol, primero debe de ser del tipo de dato que queremos, ademas no debe estar repetido y por ultimo, se debe buscar su lugar en todos los subarboles
## 5. Recorridos
    Para reccorer un arbol, necesitas seguir uno de tres ordenes vistos:

    - preorden: raíz, izquierda, derecha;
    - inorden: izquierda, raíz, derecha;
    - postorden: izquierda, derecha, raíz.

    Cada orden nos sirve de algo, por ejemplo el inorden nos arroja una lista creciente
## 6. Altura y eficiencia
    La altura es el numero de "niveles" que tiene el arbol, por ejemplo, si hay una raiz y un hijo, la altura del nodo hijo es 2.
    Nos sirve para considerar si una busqueda es eficiente o no, pues a mayor algura una busqueda se vuelve mas costosa por el numero de datos 
## 7. Pruebas
    La pruebas consideran que el codigo debe tener una buena implementacion, que debe de estar blindado contra usuarios que metan datos erroneos y que no se rompan con ejemplos esperados
## 8. Cambio técnico: evaluar.py
    Se supone que este comando nos ayudaria a que no tengamos que complicarnos de mas con el pytest y lo hace pero a mi me surguieron varios problemas con las carpetas por lo que al final tuve que evaluar mis pruebas en el archivo de test_publucos
## 9. Problemas relacionados
    Contador de hojas / Nivel de profundidad: ¿Cómo calcular cuántas hojas tiene tu árbol? Esto te ayudará a practicar recorridos pero añadiendo un "contador" que se pasa entre llamadas recursivas.
## 10. Pregunta abierta
    ¿por qué un BST puede llegar a tener la misma complejidad de búsqueda que una lista simple?