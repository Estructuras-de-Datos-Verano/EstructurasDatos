# Discusión - Leonardo Daniel Arenas Serafín

### 1. Lectura estratégica

El problema te está pidiendo que lleves una cuenta de quienes son los niños que van saliendo en orden y cuáles son los que quedan a salvo por cada ronda.

### 2. Elección de estructura

#### ¿Por qué una cola?
Porque una cola permite llevar un orden circular para cada ronda.

#### ¿Qué otra estructura consideraste?
Personalmente consideré una lista, pues es la primera estructura natural que se me ocurre al pensar en llevar un orden

#### ¿Por qué la descartaste?
La descarté porque es muy difícil poder acceder a cada elemento de la lista e ir eliminando en medio de ésta, gastaría muchísimos recursos y no sería sencillo.

### 3. Diseño del algoritmo

```text
Primero debemos crear un deque que contenga los primeros n enteros positivos naturales no negativos al menos no cero e inicializar una lista vacía para los eliminados.
Después, mientras not deque.esta_vacia.
Tomamos el primer niño del deque y lo encolamos al deque.
Tomamos al siguiente niño y lo eliminamos, entonces lo metemos a la lista de eliminados.
Regresamos la lista de los niños eliminados.
```

### 4. Pruebas

#### Escoge una prueba pública: `test_caso_minimo()`

#### Explica qué propiedad verifica: 
Verifica la propiedad que está en el orden de eliminación. Esta funcion `modulo.orden_eliminacion()` tiene dos if, el primero verifica si el círculo solo tiene un elemento, el segundo verfica que esto no pase. Entonces este test verifica que cuando en efecto el círculo solo tenga un elemento, entonces se corra el primer if y haga lo que la función establece: Se elimina al único niño y se agrega a la lista de eliminados.

#### Propón una prueba adicional: 
Mi propuesta es verificar que al operar con los niños del deque, en efecto el deque se vea modificado y que no sea necesario actualizarlo manualmente.

### 5. Complejidad

####  ¿Cuántos niños se eliminan?

Todos, n

####   ¿Cuántas veces se mueve o procesa cada niño?

Depende, una mitad se procesa una vez. De la segunda mitad, la mitad se procesa dos veces (es decir, un cuarto del total). De la otra mitad (del otro cuarto), la mitad se procesa 3 veces (un octavo) y así sucesivamente hasta terminar con un solo niño y ese niño se procesará log2(n) piso veces, pues este es el número de cuántas veces se puede partir a la mitad el círculo. De esta manera, ¿cuántas operaciones hay?
hay n/2 niños de 1, hay n/4 niños de 2, entonces son n/2 operaciones, hay n/8 niños de 3 entonces hay 3n/8 operaciones, así hasta log2(n). n * (SUMA de m=1 hasta log2(n) de m/2**m)
De esta forma, tendría una complejidad de O(n * (SUMA de m=1 hasta log2(n) piso de m/2**m))
####   ¿Qué estructura permite que esas operaciones sean eficientes?

El deque, pues puede acceder al inicio y final de la lista.

####  ¿Cuánta memoria adicional se usa?

Nada, pues no se crean nuevaos deques ni nuevas listas, sino que solamente se modifican las ya existentes

### 6. Contraste

Si el problema cambiara ligeramente, ¿seguirías usando una cola?

¿Por qué?


#### Propuesta Cambio 1. Supongamos que en vez de tomar al primer niño, tomaramos al último
Entonces seguiría utilizando el deque porque simplemente habría que voltear el orden y seguir utilizándolo como habituamos

#### Propuesta Cambio 2.  Supongamos que ahora queremos eliminar al niño qu está justo en el medio
Entonces ya no utilizaría el deque porque éste es útil para acceder a los extremos de la lista, pero no para acceder al medio. 


1. Si se eliminara cada tercer niño, ¿la cola seguiría siendo natural?
Sí, pues el orden círculas seguiría manteniéndose
2. Si necesitáramos consultar siempre el menor número vivo, ¿la cola bastaría?
No, pues la cola solo puede acceder a los extremos, pero no sabe nada acerca del valor de sus elementos, solamente sabe de su posición extrema.
3. Si el círculo cambiara dinámicamente con inserciones en medio, ¿qué parte del modelo se rompería?
La parte de que al salvar a un niño lo encolaramos, pues solo se puede al final y no al medio.
4. ¿Qué prueba pública te da más confianza y cuál falta?
Me da confianza la prueba del `test_caso_minimo()` pues me hace ver cómo es que siempre termina el problema. Hace falta ver qué pasa cuando n > 2 * 10 ** 5, pues habíamos establecido esta restricción

### 7. Pregunta abierta

¿Qué pasaría si en vez de seguir el algoritmo de salvar al primero y eliminar al segundo, agregamos un randomizer para que decida al al azar cuál niño eliminar? ¿Qué cambiaría en la logística del código?