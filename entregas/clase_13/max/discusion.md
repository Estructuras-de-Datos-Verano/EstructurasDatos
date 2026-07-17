# Discusión_cale_13_Max

## 1. Problema que resuelve AVL

El arbol binario comun se vuelve lento y se estira como una lista si metes los datos en orden. El AVL soluciona esto obligando al arbol a mantenerse chato y repartido para que buscar cualquier dato sea siempre rapidisimo.

## 2. Factor de balance

Cada nodo mide la diferencia de altura entre su lado izquierdo y su lado derecho para ver que tan inclinado esta. La regla es estricta: si esa resta da mas de uno o menos de uno, el nodo se declara en desequilibrio.

## 3. Rotaciones e invariante BST

Para enderezarse sin desordenar los datos, el arbol mueve los punteros de los nodos como si fuera un rompecabezas. Esto hace que el hijo pesado suba a ser el nuevo padre y el padre baje, manteniendo intacto el orden logico.

## 4. Casos LL RR LR RL

Segun donde caiga el peso extra, hay cuatro jugadas: si esta todo inclinado hacia un lado se arregla con un solo giro basico. Si el peso hace un zig-zag, se necesitan dos giros combinados para poder nivelar la estructura.

## 5. Complejidad

Al mantenerse siempre bajito y parejo, el AVL asegura que buscar, meter o sacar datos tome poquisimo tiempo de forma logaritmica. Ademas, hacer los giros de balanceo es instantaneo porque solo implica mover un par de flechas de memoria.

## 6. Pruebas propias

Estan adjuntas en el documento test_estudiante, y sirven para verificar la implementación de las diferentes variables.

## 7. Revisión técnica recibida


## 8. Revisión técnica realizada


## 9. Pregunta abierta

¿Además de con árboles, se puede crear algo parecido para pila?
