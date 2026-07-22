# Arturo Prudencio Bonilla

### 1. Lectura estratégica

- El problema pide un algoritmo que sea capaz de "comer" un numero natural y con el formar una cola, a la cola se le debe poder eliminar el primer termino y poder agregar elementos. 
- Comportamiento del algortimo: con la cola creada, se debe salvar (eliminar y agregar al final de la cola) el primer elemento y se debe eliminar y agregar a una segunda lista el elemento eliminado
- Salida: el algoritmo debe dar como resultado final una lista con todos los eliminados en el orden en que fueron saliendo de la cola original

### 2. Elección de estructura

1. ¿Por qué una cola?
    - Porque es la estructura ideal para poder modificar nuestra lista de datos como necesitamos (eliminar al principio y agregar al final)

2. ¿Qué otra estructura consideraste?
    - PILA 

3. ¿Por qué la descartaste?
    - Porque no funcionaria pues no podriamos eliminar los datos del inicio

### 3. Diseño del algoritmo

- Comportamiento del algortimo: con la cola creada, se debe salvar (eliminar y agregar al final de la cola) el primer elemento y se debe eliminar y agregar a una segunda lista el elemento eliminado
- Salida: el algoritmo debe dar como resultado final una lista con todos los eliminados en el orden en que fueron saliendo de la cola original


### 4. Pruebas

- test_caso_minimo():

    Esta prueba verifica que el comportamiento esperado en el caso en el que solo hay un elemento es correcto
    
- Me gustaria probar el caso maximo si es que es posible con los recursos que tenemos


### 5. Complejidad

Pensando en el numero de operaciones que necesitamos para el numero de datos que entran al algoritmo, pienso que el tiempo y la complejidad es lineal O(n), pues para n datos, necesitamos n operaciones. 

### 6. Contraste

Si el problema cambiara ligeramente, ¿seguirías usando una cola?
- Depende 

¿Por qué?
- Porque tal vez ya no es lo mas natural o mas optimo 

### 7. Pregunta abierta

- ¿Cambiaria mucho el problema si no nos importara el orden circular? 
- ¿Que pasaria si en vez de agregar al salvado al final de la cola se agregara a un tercera lista de salvados?