# Notebook clase 14 - Leonardo Daniel Arenas Serafín


## 1. Motivación

#### Si llegan muchas tareas mientras también atendemos tareas urgentes, ¿qué desventaja tendría mantener toda la lista siempre ordenada?
Que mientras estamos atendiendo debemos de ir ordenando la lista al mismo tiempo. 
#### ¿Qué operación domina en dos de estos escenarios?
Domina la operación de comparar los valores de los elementos para descubrir el orden de prioridad

## 2. Operación dominante

#### ¿Qué costo se repite si extraemos mínimos desde una lista sin ordenar?
Se repite la operación de comparar todos los elementos de la lista para poder encontrar el mínimo, después es el costo de extraerlo y volver a hacer la lista con los nuevos ordenes.

## 3. Cola FIFO vs cola de prioridad

#### ¿Cuándo sería incorrecto usar una cola FIFO?
Cuando el elemento de prioridad de salida no es el primero que entró.

## 4. Descubrimiento manual

| Valor que llega | Arreglo provisional | Comparación necesaria | Arreglo después de reparar | Intercambios |
| ---: | --- | --- | --- | ---: |
| 7 | `[7]` | no tiene padre | `[7]` | 0 |
| 3 | `[7, 3]` | `3 < 7` | `[3, 7]` | 1 |
| 9 | ` [3, 7, 9]` | `7 < 9` | ` [3, 7, 9]` | 0 |
| 1 | ` [3, 7, 9, 1]` | `1 < 9`, `1 < 7`, `1 < 3` | `[1, 3, 7, 9]` | 3 |
| 6 | `[1, 3, 7, 9, 6]` | `6 < 9`, `6 < 7`, `3 < 6` | `[1, 3, 6, 7, 9]` | 2 |
| 5 | `[1, 3, 6, 7, 9, 5]` | `5 < 9`, `5 < 7`, `5 < 6`, `3 < 5` | `[1, 3, 5, 6, 7, 9]` | 3 |

#### Dibuja el árbol, identifica padre e hijos y luego simula una extracción: retirar raíz, mover último, elegir hijo menor e intercambiar hasta restaurar `padre <= hijos`.
                  1
               /     \
              3       5
             / \     /
            6   7   9

Simulación de extracción. Retirar 1 y guardarlo. Mover último:
                  9
               /     \
              3       5
             / \    
            6   7  
Comparar: 9 y 3
                  3
               /     \
              9       5
             / \    
            6   7  
Comparar: 9 y 6
                  3
               /     \
              6       5
             / \    
            9   7 

#### Completa la fila correspondiente a insertar `9` y explica por qué se detiene la reparación.
Porque 9 es mayor a su padre asociado, por lo que no es necesario hacer reparaciones.

#### Qué permanece estable después de insertar un valor?
Se mantiene estable la cantidad de nodos y la altura

## 5. Qué es un heap

#### ¿Por qué un heap no es un BST?
Porque el heap es una especie de lista, es una secuencia que simplemente está ordenda de acuerdo a un cierto criterio, tiene una base de BST en cuanto a la esstructura matemática, pero difieren en cuanto al orden parcial se refiere. La principal diferencia es que en el árbol se sigue el comportamiento invariante de que a la izquierda están valores menores y a la derecha valores mayores, mientras que un heap simplemente sigue el orden de que el padre debe ser menor o igual a los hijos.

## 6. Propiedad de min-heap

#### ¿Los hermanos deben estar ordenados entre sí?
No, pues se podría decir que esta estructura no es un buen orden, sino que es un orden parcial, existe un mínimo global porque todos los valores provienen de una raíz, pero no existe máximo, solo maximal y no puedes comparar todos los elementos entre sí. De la misma forma, si quitas la raíz global, deja de haber mínimo y solo hay minimales.

## 7. Árbol binario completo

#### ¿Qué ventaja da esta forma para almacenar el árbol?
Da la ventaja de que simpre tendremos un árbol balanceado y con alturas AVL.

## 8. Representación por arreglo

####  Para `[2, 5, 4, 9]`, ¿qué valor está en el índice 2?
4, pues se ordena de izquierda a la derecha. La raíz es 2, el cual es el índice 0, el hijo izquierdo es 5, el índice 1 y el hijo derecho es 4, el índice 2.

## 9. Fórmulas de índices

#### ¿Cuáles son los hijos del índice 2?
Los hijos del índice dos son, a la izquierda 5 y a la derecha 4.

## 10. Inserción

#### Si insertas `1` en `[2, 5, 4, 9, 8, 7]`, ¿con qué valores esperas que se compare antes de llegar a su posición final?
Se va a comparar con 4 que es su padre, y posteriormente con 2 que es la raíz, para aspi llegar a la raíz, su posición final

#### ¿Por qué no insertamos directamente en la raíz?
Porque queremos llevar una estructura de prioridad basada en el mínimo que solamente se compare con los padres.

## 11. Sift-up

#### ¿Cuándo se detiene sift-up?
Cuando el valor actual se vuelve mayor o igual a su padre o cuando se llega a la raíz

## 12. Extracción del mínimo

#### ¿Por qué se mueve el último elemento?
Porque el último elemento en el mejor de los casos es la raíz, por lo que se extrae, y si no, como queremos mantener el orden de menores, existe la posibilidad de que el último no sea el más grande, pues se va ordenando en orden de llegada de izquierda a derecha y se compara con el padre, pero no se compara con los hermanos, por lo que si queremos llevar un mejor orden entre hermanos para ir preparando futras extracciones debemos de compararlos al llevar el último a la raíz y reparar.

## 13. Sift-down

#### ¿Por qué debemos elegir el hijo menor?
Porque esta estructura le da prioridad a los mínimos, por lo que si queremos llevar este orden, siempre se debe de elegir al menor, ya que al elegir cualquier hijo puede llevar a que se siga violando la regla del orden.

## 14. Visualizaciones ipywidgets

#### ¿Qué relación observas entre la celda del arreglo y el nodo resaltado?
Que son el mismo, pues el árbol y el arreglo son exactamente la misma estructura.

## 15. Comparación BST, AVL y heap

#### ¿Qué estructura elegirías para cada escenario y qué operación justifica tu decisión?
- Escenario A: Elegiría AVL, pues se busca tener un orden total sobre todos los elementos, además que buscamos tener un recorrido ordenado
- Escenario B: Elegiría heap, pues lo que nos importa es tener una prioridad todo el tiempo, tener un mínimo accesible.

#### ¿Qué elegirías para búsquedas arbitrarias y qué para extraer mínimos?
Heap, ya que al hacer búsquedas arbitrarias no necesitamos tener un orden total de los elementos y para extraer mínimos solo necesitamos saber cuál es y tener acceso a él fácilmente.

## 16. Complejidad

#### ¿Por qué sift-up y sift-down son logarítmicos?
Porque por cada paso y cada operación se recorre un nivel del árbol y cada nivel del árbol se ramifica en un orden 2 exponencial, por eso es que al tener n elementos, solo hay log2(n) niveles y eso hace que su complejidad sea logarítmica.

## 17. Last Stone Weight

#### ¿Cuál es la operación dominante y el resultado del ejemplo?
La operación dominante siempre es comparar. Pues siempre debemos comparar los elementos del árbol para encontrar los 2 máximos y una vez encontrados debemos compararlos para ver cuál es mayor o si son iguales. El resultado del ejemplo es `[1]`

#### Pseudocódigo:

      ultima_piedra(piedras: list[int]) -> int:
         pesos = []
         heap = HeapMin()
         para cada piedra en piedras
            pesos.append(-piedra)
         para cada peso en pesos
            heap.insertar(peso)
         mientras heap.tamaño > 1
            a = heap.extraer_min()
            b = heap.extraer_min()
            si no a == b
               heap.insertar(abs(a-b))
         si heap esta vacía
            regresa 0
         else
            regresa heap.minimo()



## 18. Pruebas

#### Diseña, sin escribir todavía el código completo, una entrada que obligue a `_bajar` a elegir el hijo derecho y explica qué afirmaciones comprobarías.
        test()
        heap = [6,5,4,7]
        assert heap._bajar() == [4,5,6,7]

Se elige al hijo derecho porque si se eligiera el izquierdo, 5 quedaría como padre de 4 y esto no es posible.
        
#### ¿Qué error específico detecta una extracción con varios descensos?
padre >= hijos

## 19. Revisión técnica

#### ¿Qué alerta usarías para indicar que el diff contiene archivos de otro alumno y por qué?
`WARNING`, pues debería alertar al compañero que podría haber un error a la hora de subir documentos y alterar la entrega, ya sea empalmando los archivos o subiendo cosas que no son propias, lo cual podría perjudicarle.

#### ¿Qué debe incluir `revision_nombre_revisor.md`?
Debe de incluir los puntos que vienen en el flujo recomendado, debe incluir la salida de la terminal al ejecutar `pytest -v`, debe incluir aspectos a mejorar, fortalezas, conclusión, comentarios, tips.

## 20. Preparación para Dijkstra

#### Después de procesar C y descubrir una distancia 2 hacia D, ¿qué elemento debería salir antes: B con 4 o D con 2? Justifica usando la operación dominante.
D con 2, ya que sería el nuevo mínimo.
#### ¿Qué guardaría la prioridad en Dijkstra?
Guardaría cuál es el camino más corto, guardaría valores de números que indiquen el costo de un camino.

## 21. Cierre

#### ¿Qué criterio usarás para elegir una estructura en un problema nuevo?
Usaré el cirterio de primero analizar qué es lo que el problema nuevo pide, qué es lo que se necesita optimizar, qué es lo que tiene prioridad y qué es lo que no es relevante. Para así comparar complejidad en las operaciones necesarias y elegir una estructura.