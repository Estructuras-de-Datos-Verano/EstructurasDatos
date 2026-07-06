# Notebook - Clase 06
## Lectura Estratégica
```text
Entrada:
- Estructura que represente a los niños (puede ser con nombres o números iniciales, da igual)

Salida:
- Lista ordenada acorde a los eliminados

Restricción principal:
- La complejidad va a ser muy alta si tratamos de poppear y pushear manualmente cada vez. Además, la cantidad de niños no debe pasar 2x10^5
```
## Ingeniería Inversa 
1. ¿Qué está pidiendo exactamente el problema?
Entregar una lista ordenada de cómo fueron eliminados los participantes del juego. En términos técnicos, por cada par se elimina el segundo y cada segundo eliminado debe entrar a una lista/estructura FIFO.
2. ¿Qué información debo recordar mientras avanzo?
Lo que escribí arriba, junto con recordar que podemos terminar usando un algortimo de complejidad elevada que al llegar a 2*10^5 falle.
3. ¿Qué operaciones realizo continuamente?
Como el primer niño se va a salvar, hay que moverlo al final y el segundo es el que no se salva, entonces este sale de la lista y se añade a la lista de eliminados. Esto debe repetirse con cada par hasta llegar al final.
4. ¿Existe una estructura de datos que implemente naturalmente esas operaciones? Un deque porque podemos insertar y borrar elementos de cualquier extremo.
5. ¿Cómo resolvería este problema con papel y lápiz? Hago un círculo de niños, tacho los que toca sacar, los escribo y luego los o tachados forman el nuevo circulo.
6. Escribir únicamente después el pseudocódigo.
Función SecuenciaJosephus(n):
    Crear una cola_circular con los números desde 1 hasta n
    Crear una lista vacía llamada resultado

    Mientras cola_circular no esté vacía:
        // El primer niño se salva: se saca del frente y se va al final
        niño_salvado = desencolar_frente(cola_circular)
        encolar_atrás(cola_circular, niño_salvado)

        // El segundo niño muere: se saca del frente y se registra
        niño_eliminado = desencolar_frente(cola_circular)
        agregar_a_lista(resultado, niño_eliminado)

    Devolver resultado
## Modelado
### Preguntas de modelado
1. Cuando un niño se salva, ¿desaparece del problema? No, se conserva en el círculo
2. Cuando un niño se elimina, ¿vuelve a participar? No
3. ¿Qué significa avanzar en un círculo si estamos usando una estructura lineal? Que el último elemento se convierte en el primero
4. ¿Qué operación se repite una y otra vez? Iterar sobre los elementos, mandar al final a quien se salve, eliminar a quien muere y añadirlo a la lista de eliminados.
### Sobre la pregunta del orden de eliminados
- La estructura del pseudocódigo respeta siempre la regla de eliminar 1 de 2 porque el primero se salva (lo manda al final) y siempre el siguiente lo elimina. Como estamos en un "círculo", no importa incluso si la cantidad de niños resulta impar porque eso iniciaría otra iteración.
## Pseudocódigo

Completa los espacios marcados:

```text
función orden_eliminacion(n):
    validar n
    vivos = cola con números de 1 a n
    eliminados = lista vacía

    mientras vivos no esté vacía:
        si solo queda un niño:
            eliminarlo y guardarlo
        si no:
            // TODO: mover al final al niño que se salva
            niño_salvado = desencolar_frente(vivos)
            encolar_atrás(vivos, niño_salvado)
            
            // TODO: eliminar al siguiente niño
            niño_eliminado = desencolar_frente(vivos)
            
            // TODO: guardar el eliminado
            guardar niño_eliminado en eliminados
    regresar eliminados
```