1. Lectura estratégica

El problema describe un proceso iterativo donde se eliminan elementos siguiendo una regla fija: en un grupo ordenado, se conserva un elemento y se elimina el siguiente, repitiendo hasta que quede uno o hasta vaciar la estructura.

La clave no está en “simular niños”, sino en modelar un sistema de procesamiento secuencial con eliminación periódica.

El objetivo real es capturar el orden de salida bajo una regla determinista, no simplemente recorrer una lista.

2. Elección de estructura
¿Por qué una cola?

Una cola FIFO representa exactamente el comportamiento del sistema:

El elemento que entra primero es el primero en ser procesado.
Permite “rotar” el sistema sin acceder a posiciones intermedias.
Las operaciones necesarias son constantes: push, pop, front.

El patrón del problema es:

atender al primero,
reinsertarlo si sobrevive,
eliminar al siguiente.

Esto encaja naturalmente con una cola.

¿Qué otra estructura consideraste?

Una lista dinámica o un arreglo indexado.

¿Por qué se descartó?

Porque eliminar elementos intermedios en una lista implica:

desplazamientos de elementos,
costo O(n) por eliminación,
complejidad total O(n²) en simulaciones directas.

Esto rompe el requisito de eficiencia cuando n es grande.

3. Diseño del algoritmo

El algoritmo no se basa en búsqueda ni comparación, sino en transformación repetitiva del estado.

En cada iteración del sistema:

El primer elemento se extrae y se reinserta al final (sobrevive temporalmente).
El siguiente elemento se elimina definitivamente.
Se registra su salida.

Este ciclo mantiene la estructura estable mientras reduce su tamaño de forma controlada hasta la terminación.

4. Pruebas


def test_caso_minimo():
    assert modulo.orden_eliminacion(1) == [1]

Verifica:

No hay ciclos de eliminación.
El único elemento debe ser retornado directamente.
Sirve para validar que el algoritmo no falla en condiciones límite.

prueba adicional: 

def test_caso_potencia_de_dos():
    assert modulo.orden_eliminacion(8) == [2, 4, 6, 8, 3, 7, 5, 1]

Verificar que el algoritmo no depende de “casos felices” como n impar.
Detectar errores en la alternancia (salvar/eliminar).
Observar si la simulación mantiene consistencia en ciclos completos.

5. Complejidad

### ¿Cuántos niños se eliminan?

Se eliminan exactamente **n** niños. En cada iteración del algoritmo se elimina uno, y el proceso termina cuando ya no queda ningún niño en la cola (o cuando queda uno, si solo se busca el ganador).


Tiempo

O(n)

Cada elemento entra y sale de la cola un número constante de veces. Las operaciones de cola son O(1), por lo que el costo total es lineal.

Memoria

O(n)

Se almacena la cola completa de elementos vivos, más una lista auxiliar para el orden de salida.

6. Contraste

Si el problema cambiara ligeramente, por ejemplo:

eliminar cada tercer elemento,
o reinserción condicional más compleja,

la cola seguiría siendo válida mientras el acceso siga siendo exclusivamente frontal.

Sin embargo, si se llega a introducir: acceso al mínimo,inserciones en posiciones arbitrarias, o eliminación basada en condiciones globales,

la cola deja de ser suficiente porque no permite manipulación interna eficiente.

7. Pregunta abierta

¿Qué estructura de datos permite modelar eficientemente sistemas donde los elementos deben mantenerse en orden?



### ¿Cuántas veces se mueve o procesa cada niño?

Cada niño puede pasar varias veces por el frente de la cola mientras sigue vivo. En cada turno solo puede ocurrir una de dos cosas:

- Se mueve al final de la cola (se salva).
- Es eliminado y deja de participar.

Aunque algunos niños se muevan más veces que otros, cada iteración realiza un número constante de operaciones sobre la cola, y en total el algoritmo realiza un número proporcional a **n** de iteraciones.


### Discusión: ¿Por qué una cola deja de funcionar aquí?

En el problema del **Josephus**, una cola FIFO es adecuada porque los niños siempre se atienden en el mismo orden en que les toca participar. El primero de la cola se procesa, se mueve al final si sobrevive o se elimina si pierde. El orden nunca cambia.

En **Nearest Smaller Values**, la situación es diferente. Para cada elemento, debemos encontrar el valor más cercano que sea menor y esté a su izquierda. No basta con revisar los elementos en el orden en que llegaron, sino que debemos conservar únicamente aquellos que todavía pueden ser una respuesta válida.

Cuando aparece un número más pequeño, algunos valores anteriores dejan de ser útiles porque nunca volverán a ser la respuesta para los elementos siguientes. En una cola FIFO no es posible eliminar esos candidatos del final; solo permite retirar elementos del frente.

Por esta razón, una cola no modela correctamente las operaciones que necesita este problema.

**Pregunta para la siguiente clase:**

¿Qué estructura de datos permite conservar los candidatos que aún son útiles y eliminar rápidamente los que ya no sirven?

---

## Cierre

### 1. Si se eliminara cada tercer niño, ¿la cola seguiría siendo natural?

Sí. La cola seguiría siendo una buena elección. En lugar de mover un niño al final antes de eliminar al siguiente, se moverían dos niños al final y se eliminaría al tercero. El patrón cambia, pero las operaciones siguen siendo `desencolar()` y `encolar()`.

### 2. Si necesitáramos consultar siempre el menor número vivo, ¿la cola bastaría?

No. Una cola solo permite acceder al elemento que está al frente, no al menor de todos los elementos. Para esa operación sería más adecuada una estructura como una cola de prioridad (heap).

### 3. Si el círculo cambiara dinámicamente con inserciones en medio, ¿qué parte del modelo se rompería?

La cola dejaría de representar correctamente el problema, ya que solo permite insertar al final y eliminar por el frente. Si fuera necesario insertar o eliminar niños en posiciones intermedias, se requeriría otra estructura, como una lista enlazada o un árbol balanceado, dependiendo de las operaciones necesarias.

### 4. ¿Qué prueba pública te da más confianza y cuál falta?

La de  varios niños (por ejemplo, n = 7 u 8), porque permite verificar que el patrón de "uno se salva y el siguiente se elimina" se repite correctamente.

Aún falta probar casos límite, como:

- n = 1 (solo hay un niño).
- n = 2 (se elimina uno y el otro gana).
- Un valor grande de n (por ejemplo, n = 200000) para comprobar que el algoritmo sigue siendo eficiente.