# Notebook - Clase 06 - Gustavo 

### Ingeniería inversa al algoritmo

## 1. ¿Qué está pidiendo exactamente el problema?

    El orden exacto de la eliminación de cada niño del círculo.

## 2. ¿Qué información debo recordar mientras avanzo?

    Quienes siguen vivos, es decir, los niños que no fueron eliminados tras la selección. El estado de las personas, si es que hay que saltarla por si se salva o eliminarla porque fue seleccionada y el orden circular que tiene.

## 3. ¿Qué operaciones realizo continuamente

    Avazar, seguir seleccionando. Eliminar, sacar algún niño que fue seleccionado. Salvar, no sacar algún niño.

## 4. ¿Existe una estructura de datos que implemente naturalmente esas operaciones?  

    Sí, la estructura perfecta para esto es una Cola (Queue). Una cola sigue el principio FIFO (Primero en entrar, primero en salir). Modelar un círculo de saltos con una cola es muy natural:

## 5. ¿Cómo resolvería este problema con papel y lápiz?

    Dibujas el círculo, supongamos una cantidad finita como n=7 y ver como va avazando realizando las pruebas necesarias.

## 6. Escribir únicamente después el pseudocódigo.



---

### Preguntas del Modelado

## 1. Cuando un niño se salva, ¿desaparece del problema?

    No. El niño que se salva simplemente pospone su destino. En la implementación, esto equivale a sacarlo del frente de la fila y volviéndolo a formar al final. De esta manera, permanece dentro del círculo y volverá a ser evaluado cuando la ronda dé la vuelta completa y llegue nuevamente su turno.

## 2. Cuando un niño se elimina, ¿vuelve a participar?

    No, su participación termina definitivamente. Cuando a un niño le toca ser eliminado, se extrae de la estructura (la cola) y nunca se vuelve a insertar

## 3. ¿Qué significa avanzar en un círculo si estamos usando una estructura lineal?

    Significa crear una ilusión de rotación continua.

## 4. ¿Qué operación se repite una y otra vez?

    La rotación y el salto
--- 

### Cierre

## 1. Si se eliminara cada tercer niño, ¿la cola seguiría siendo natural?

    Sí, conceptualmente seguiría siendo natural, pero empezaría a perder eficiencia si el salto crece mucho.

## 2. Si necesitáramos consultar siempre el menor número vivo, ¿la cola bastaría?

    No, la cola sería completamente insuficiente.


## 3. Si el círculo cambiara dinámicamente con inserciones en medio, ¿qué parte del modelo se rompería?

    Se rompería la regla de oro de la cola: las operaciones de tiempo constante.

## 4. ¿Qué prueba pública te da más confianza y cuál falta?

     La prueba de orden_eliminacion(7) [2, 4, 6, 1, 5, 3, 7] es excelente porque obliga al algoritmo a dar más de una vuelta completa al círculo.

