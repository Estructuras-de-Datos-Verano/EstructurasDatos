Santiago Saldívar

EL AVL nos ayuda a resolver problemas de balance. Si tenemos un árbol desbalanceado, podemos rotar respecto ciertos nodos, cabiando la raíz. Esto no altera las relaciones entre los nodos, pero ayuda al balance. 
El Factor de balance es la diferencia de altura entre los hijos nodos. Mientras más chico sea, mayor balance. 
Las rotaciones mantienen el invariante porque no alteran las relaciones entre los nodos. 
Los casos LL RR LR RL son todos casos en que están desbalanceados los árboles. En cada uno, las letras indican en qué dirección está desbalanceado. Para corregir, hay que rotar al lado contrario.
La complejidad no aumenta mucho, de hecho es una forma de reducirla para casos de árboles desbalanceados.
Mir pruebas verifican el comportamiento según se van agregando nodos.
**Revisión técnica. Gus, esta es la parte que modificas tú.**
Pregunta abierta:
¿Qué significa AVL? 