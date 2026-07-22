### Entrada, salida y restricciones

Completa en tu copia del notebook:

```text
Entrada:
- el núnero de los niños enumerados del 1 hasta el n

Salida:
- el lugar en el que fueron eliminados los niños de acuerdo a su número

Restricción principal:
- que el numero de eliminados sea igual al numero de niños, y que al menos haya un niño
```

Dato importante del enunciado: `1 <= n <= 2 * 10^5`.

Eso significa que una solución demasiado lenta puede fallar aunque sea correcta en ejemplos pequeños.




# Ingeniería inversa del algoritmo

Esta sección será permanente en las siguientes clases.

Antes de escribir una sola línea de código, responde:

1. ¿Qué está pidiendo exactamente el problema?
 - hacer un progama donde los niños enumerados en un circulo se vallan eliminando uno de cada 2
2. ¿Qué información debo recordar mientras avanzo?
 - recordar siempre el objetivo y no desviarse en ambigüedades
3. ¿Qué operaciones realizo continuamente?
 - la operacion de elegir a un niño al azar de cada 2 para eliminarlo
4. ¿Existe una estructura de datos que implemente naturalmente esas operaciones?
 - una pila es util para este ejercicio en particular
5. ¿Cómo resolvería este problema con papel y lápiz?
 - enumerando los niños y de cada 2 niños circularia a uno para eliminarlo
6. Escribir únicamente después el pseudocódigo.

entrada
  lista de niños

verificar si no esta vacía 
mientras la lista tenga mas de un niño 
  tomar al primer niño y mandarlo al final de la lista
  tomar al segundo y eliminarlo de la lista y agregarlo a la lista de eliminados
cuando solo tenga un niño eliminarlo y agregarlo a la lista de eliminados

regresar lista de eliminados



### Preguntas de modelado

Responde antes de seguir:

1. Cuando un niño se salva, ¿desaparece del problema?
- no, ahora ese niño "competira" con el otro para salvarse
2. Cuando un niño se elimina, ¿vuelve a participar?
- no el sistema lo elimina de la ronda de juego
3. ¿Qué significa avanzar en un círculo si estamos usando una estructura lineal?
- significa que ganaste tu ronda y sobreviviste en el juego y jugaras otra ronda
4. ¿Qué operación se repite una y otra vez?
- justo, la de eliminarotros jugadores una y otra vez hasta eliminar el último


## 4. Diseñar el algoritmo en español

Antes del pseudocódigo, escríbelo en lenguaje natural.

Una versión posible es:

```text
Crear una cola con los niños del 1 al n.
Mientras haya niños vivos:
    mover al final al niño que se salva
    eliminar al siguiente niño
    guardar el eliminado en la respuesta
Regresar la respuesta
```

Ahora explica con tus palabras por qué esto respeta la regla de eliminar uno de cada dos.
R = esto respeta la regla por que de los  2 siguientes niños uno lo pasas para atrás es decir se slava y al otro lo eliminas


## Complejidad

Discute:

- ¿Cuántos niños se eliminan?
  - de n niños se eliminan n
- ¿Cuántas veces se mueve o procesa cada niño?
  - n + n/2 + n/4 + .... hasta que ya no queden niños
- ¿Qué estructura permite que esas operaciones sean eficientes?
  - la pila
- ¿Cuánta memoria adicional se usa?
  - muy poca


## Cierre

Preguntas de contraste para discutir:

1. Si se eliminara cada tercer niño, ¿la cola seguiría siendo natural?
  - si solo cambia el numero de interaciones
2. Si necesitáramos consultar siempre el menor número vivo, ¿la cola bastaría?
  - no necesariamente la cola es mas especifica
3. Si el círculo cambiara dinámicamente con inserciones en medio, ¿qué parte del modelo se rompería?
  - se da el caso donde el que mando para taras queda adelante entonces el sistema dice que solo hay un dato y lo manda sin acabar 
4. ¿Qué prueba pública te da más confianza y cuál falta?
  - donde no hay comportamientos raros de los datos

