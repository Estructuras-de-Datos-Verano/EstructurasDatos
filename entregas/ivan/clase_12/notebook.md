# Notebook.md - José Iván Reyna Blanco
## 1. Motivación

**Pregunta.** Escribe un ejemplo donde buscar en una lista sea costoso y explica qué esperas que un BST mejore.
```python
import time
import random
limite = 10000000
lista_grande = [chr(i) for i in range(1114111)] + ["Z"] * (limite - 1114111) # Pone Z's en donde ya no pueden ir caractéres porque ya no existen.
random.shuffle(lista_grande)
def busqueda_costosa(l: list):
    return l.index("Z")
inicio = time.perf_counter()
index = busqueda_costosa(lista_grande)
fin = time.perf_counter()
t = fin - inicio
print(f"Tiempo total: {t:.6f}, índice: {index}")
```
Espero que el BST permita comparar si el valor que busco está a la izquierda o derecha de la raíz y de ahí encontrar la dirección hacia dónde se debe buscar según dónde se esté parado. 

## 2. Lista vs BST

**Pregunta.** ¿Qué información usa un BST para descartar una parte del árbol que una lista desordenada no tiene? Saber si el valor buscado está a la izquierda o derecha de la raíz. 

## 3. Conteo Manual de Comparaciones

Árbol balanceado de ejemplo con inserción `8, 4, 12, 2, 6, 10, 14`.
```text
                    [8]
                /       \
               [4]      [12]
               / \      /  \
             [2] [6]   [10]  [14]
```
```text
[1]-[2]-...-[7]
```

Árbol degenerado de ejemplo con inserción `1, 2, 3, 4, 5, 6, 7`.
**Actividad.** Cuenta cuántos nodos se comparan al buscar `14` en ambos árboles.

1. ¿14 > 8? Sí -> Acceder al valor del nodo de la derecha. -> ¿14 > 12? Sí -> Acceder al valor del nodo a la derecha. -> ¿14 > 14? No. 
¿Son iguales? Sí. Break. Total de comparaciones: 3. 

2. 14 > val para cualquier valor del 1 al 7. Así que se compara 7 veces dando True. Luego la derecha del 7 es None. Break. Total de comparaciones: 7.

**Pregunta.** ¿Qué cambió: los datos o la forma del árbol? Ambos. El segundo comienza con una raíz sin hijos izquierdos. Además, ningún nodo tiene hijo izquierdo. Entonces solo puedes moverte en una dirección, al igual que en una lista. 

## 4. Altura

**Pregunta.** ¿Por qué la altura es más importante para búsqueda que la cantidad total de nodos por sí sola? Porque la cantidad total de nodos se vuelve irrelevante si están en un lado del árbol (o de algún subárbol que se genere después de un nuevo nodo pero que no sea de interés) que no es en el que necesitamos buscar. En BST se tiene como operación clave comparar el valor buscado con la raíz para así predecir de que lado va a estar un valor buscado. 

## 5. Árbol balanceado y árbol degenerado

**Pregunta.** Describe con tus palabras qué forma tiene un BST degenerado y por qué puede aparecer al insertar valores ordenados. Un árbol degenerado cumple que ningún nodo tiene más de un hijo. Eso lo que genera es que solo crezca hacia un lado, lo que vuelve trivial visualizar que cualquier elemento distinto de la raíz va a estar exclusivamente a su izquierda o derecha. De ahí que el insertar valores ordenados que cumplan además ser siemmpre mayores a la raíz va a generar por defecto un árbol degenerado. 

## 6. Búsqueda y altura

**Pregunta.** ¿Qué relación hay entre profundidad, altura y número de comparaciones? Si el valor buscado está asociado a un valor cuya profundidad sea la misma que la altura, hay n+1 comparaciones donde n es la altura - profundidad y la comparación adicional es con la raíz. De hecho en cualquier otro caso, si k es la profundidad, hay k+1 comparaciones. La altura en dado caso dice la máxima profundidad en el árbol, habla de la hoja situada en la fila de ramas más larga. 

## 7. Experimentos

**Pregunta.** ¿La diferencia de comparaciones crece cuando aumenta el tamaño del árbol degenerado? Sí, pero depende de dónde esté el valor buscado. En el peor caso, buscar el último elemento de un BST degenerado tendrá complejidad O(n). En uno balanceado, por cada nodo exploramos la mitad. Entonces la complejidad es O(log_sub2(n)). 

## 8. Animaciones

**Pregunta.** ¿Qué muestran las animaciones sobre comparaciones acumuladas y altura recorrida? Muestran la relación ente ambas con ilustraciones detalladas según el paso. Entre más altura, más comparaciones. 

## 9. Complejidad

**Pregunta.** ¿Por qué no basta decir “BST es O(log n)” sin hablar de balance? Porque solo es logarítmico cuando el BST está balanceado.

## 10. Problemas Relacionados

**Company Queries I:** Practica la estructura de árbol en la estructura de una empresa. EL número de consultas nos dice el nivel al que queremos acceder, pero en este caso se necesita ver el k-ésimo antecesor. Así, podemos recorrer el árbol descartando los izquierdos y contando las diferencias de profundidad. 

## 11. evaluar.py y pruebas

**Pregunta.** ¿Qué problema resuelve permitir `tests_extra`? Poder verificar con pytest nuevos casos en vez de solo diseñarlos, además permite deshacer el desastre de estar copiando documentos en otras carpetas o modificándolos y descartando los cambios del stash en el pull-request. 

## 12. Revisión técnica de PR

**Pregunta.** ¿Qué debe incluir un comentario técnico útil en el PR? Comando, salida y una observación construcitva. Personalmente buscaría que el comentario tenga un formato amigable de leer, junto con descripciones claras de los errores si es que hubo.

## 13. Patrón descubierto

**Pregunta.** Explica el patrón con tus palabras. El patrón para detectar la eficiencia lo resumiría 
1. Órden de inserción: Los BST son susceptibles a cambios muy grandes según el lugar dónde se inserte un nuevo nodo. Esto naturalmente produce ineficiencias en contraste con otras estructuras como las colas.
2. Altura: Hemos visto que la relación entre la complejidad y la altura es directamente proporcional en cualquier caso. Más aún, en un BST degenerado es O(n) que no es para nada eficiente una vez que la altura es muy grande.
3. Comparaciones: En BST degenerados necesitamos demasiadas comparaciones entre más cercano sea el valor buscado al final. 

## 14. Cierre

1. ¿Un BST siempre es mejor que una lista? En términos de búsqueda e inserciones, no cuando el BST es degenerado. 
2. ¿Qué relación hay entre altura y comparaciones? Una relación directamente proporcional. Crece de forma lineal en el peor caso y logarítmica en el mejor.
3. ¿Cómo se degenera un BST? Insertando solamente valores ordenados mayores/menores a la raíz.
4. ¿Qué evidencia experimental usarías para justificar tu respuesta? La prueba que hice en 'test_estudiante.py'.
5. ¿Qué problema relacionado practicarías después? Me gustó el de encontrar el antecesor k-ésimo. 


