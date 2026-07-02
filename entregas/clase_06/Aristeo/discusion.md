# Notebook de discusion - Aristeo
---

## Lectura estratégica.
Tenemos una implementación interesante de las colas, es evidente como su funcionamiento es distinto al de las pilas siendo algo practicamente opuesto en su comportamiento, con un FIFO en lugar de un LIFO.

## Elección de estructura.
Una cola es importante para la ejecución del problema pues es lo más eficiente en problemas de este tipo al usar FIFO
Había considerado el uso de pilas para el programa
Decidí no usar pilas porque encontré que el LIFO no era lo adecuado para el problema

---
## Diseño del algoritmo.
La idea del algoritmo es primero validar, luego elegir de la n cantidad de niños uno entre dos y "eliminarlo" teniendo registro de las eliminaciones, luego devolver el orden de eliminación en la salida del código

---
## Complejidad.

### ¿Cuántos niños se eliminan?
Se eliminan los n niños, uno de cada dos hasta que no queda nadie

---
### ¿Cuántas veces se mueve o procesa cada niño?
Una vez por juego, es eliminado y agregado a el orden de salida.

---
### ¿Qué estructura permite que esas operaciones sean eficientes?
Las colas hacen que sea más eficiente operar al tener la propiedad de FIFO

---
### ¿Cuánta memoria adicional se usa?
Solo una lista extra por juego, la de los eliminados, es bastante eficiente

---
## Contraste.
El juego mediante el uso de colas es muy eficiente, lleva menos tiempo del que se llevaría usando pilas en lugar de colas.

---
## Pregunta abierta.
¿De que forma se podrian implementar las colas en problemas de la vida diaria?
