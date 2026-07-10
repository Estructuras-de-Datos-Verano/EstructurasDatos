Notebook - Clase 06.
---
### Lectura estratégica
Entrada:
- Un entero `n` con la cantidad de niños, numerados del `1` al `n`.

Salida:
- Una secuencia de `n` enteros que indica el orden en que se eliminan los niños.

Restricción principal:
- `1 <= n <= 2 * 10^5`, por lo que la solución debe ser eficiente en tiempo y memoria.
---
## Ingeniería inversa del algoritmo
---

### ¿Qué está pidiendo el problema?
El problema pide simular un juego circular con n niños numerados del 1 al n, en cada turno se salva a uno y se elimina al siguiente; al final, se debe imprimir el orden en que fueron eliminados.

---

### ¿Qué información debemos recordar?
- Los niños que todavía siguen participando
- El orden circular actual
- Quién fue salvado en cada paso
- Quién fue eliminado
- El orden acumulado de eliminaciones
---
### ¿Qué operaciones realizo continuamente?
- Mover al primer niño al final de la lista (lo salvo);
- Quitar al siguiente niño (lo elimino);
- Registrar ese niño en la respuesta;
- Repetir hasta que no queden niños.

---

### ¿Existe una estructura de datos que implemente naturalmente esas operaciones?
La cola

---

### ¿Cómo resolvería este problema con papel y lápiz?
Yo lo resolvería con los siguientes pasos 🤓☝️(busqué los emojis en google y los pegué, no es chatgpt):

- Escribo los números en círculo 1,2,3,…,n. 
- Salto al primer niño, lo salvo
- Elimino al siguiente
- Anoto el número eliminado;
- Sigo desde el siguiente niño, repitiendo hasta terminar.
---


## Modelado

### Cuando un niño se salva, ¿desaparece del problema?
No desaparece, se reubica

---

### Cuando un niño se elimina, ¿vuelve a participar?
No, queda fuera del ciclo y no se considera en los pasos que siguen.

---
### ¿Qué significa avanzar en un círculo si estamos usando una estructura lineal?
Avanzar significa ir al siguiente elemento en el orden, sacar el primero y tratándolo como si fuera el último, así el orden continúa de forma circular.

---

### ¿Qué operación se repite una y otra vez?
Mover el primer elemento al final, salvar, y luego sacar el nuevo primero para eliminarlo.

---

## Pseudocódigo

Completa los espacios marcados:

```text
función orden_eliminacion(n):
    validar n
    vivos = cola con números de 1 a n
    eliminados = lista vacía

    mientras vivos no esté vacía:
    si longitud de vivos == 1:
        último = sacar el frente de vivos
        agregar último a eliminados
    si no:
        salvado = sacar el frente de vivos
        agregar salvado al final de vivos
        eliminado = sacar el frente de vivos
        agregar eliminado a eliminados

regresar eliminados
```
