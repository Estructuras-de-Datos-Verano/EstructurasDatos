# Notebook Clase 06  -  Leonardo Daniel Arenas Serafín

## Lectura estratégica

### ¿Qué está pidiendo el problema?

El problema te está pidiendo que lleves una cuenta de quienes son los niños que van saliendo en orden y cuáles son los que quedan a salvo por cada ronda. 

### ¿Qué información debemos recordar?

Mientras voy avanzando debo recordar quienes son los niños que ya saqué en orden para poder hacer lo que pide el problema, y debo recordar quienes son los niños restantes para poder realizar la siguiente ronda.

---

## Ingeniería inversa del algoritmo

### ¿Qué está pidiendo exactamente el problema?

El problema te está pidiendo que lleves una cuenta de quienes son los niños que van saliendo en orden y cuáles son los que quedan a salvo por cada ronda. 

### ¿Qué información debo recordar mientras avanzo?

Mientras voy avanzando debo recordar quienes son los niños que ya saqué en orden para poder hacer lo que pide el problema, y debo recordar quienes son los niños restantes para poder realizar la siguiente ronda.

###  ¿Qué operaciones realizo continuamente?

Primero debemos inicializar una lista vacía para el output y crear el círculo con los primeros n enteros. Ya hecho esto, primero debes elegir del círculo uno por uno niños para eliminar o salvar, para después ir agregando cuáles son los niños que van siendo eliminados a la lista creada y regresar a tu círculo los niños salvados. Repetimos el mismo proceso hata tener n==0.

###  ¿Existe una estructura de datos que implemente naturalmente esas operaciones?

Sí, la cola. Pues la cola va tomando el primer niño que ingresó y lo desencola o encola.

###  ¿Cómo resolvería este problema con papel y lápiz?

Escribiendo los niños en un círulo e ir borrando cuáles van saliendo y escribiéndolos en una lista aparte.

---

## Modelado

### Cuando un niño se salva, ¿desaparece del problema?

Desaparece del problema en el sentido que queda fuera del sistema circular de eliminación, pero la información de su orden de eliminación queda guardada en una lista.

###  Cuando un niño se elimina, ¿vuelve a participar?

No.

###  ¿Qué significa avanzar en un círculo si estamos usando una estructura lineal?

Significa seguir con el siguiente niño hasta agotar el ciclo y poder empezar de nuevo. Este proceso es posible porque cada vez que tomamos al niño del frente, el círculo se actualiza por detrás, creando un "círculo" que termina cuando todos los niños son eliminados

###  ¿Qué operación se repite una y otra vez?

círculo.leftpop() pues cada vez queremos tomar al niño siguiente para decidir qué hacer con él

for i in range(n), m = círculo.leftpop() -> lista.append(m) -or- círculo.encolar(m). 
n = círculo.tamano()

---

## Pseudocódigo

```text
función orden_eliminacion(n):
    validar n
    vivos = cola con números de 1 a n
    eliminados = lista vacía

    mientras vivos no esté vacía:
        si solo queda un niño:
            eliminarlo y guardarlo
        si no:
            encolar a vivos vivos.popleft()
            agregar a eliminados vivos.poplef()

    regresar eliminados
```
