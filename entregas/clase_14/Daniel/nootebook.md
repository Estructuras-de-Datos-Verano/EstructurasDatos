## 1. Motivación



**Pregunta:** ¿Qué operación domina en dos de estos escenarios?
- una árbol con un sistema de jerarquia tal que siempre salga el mas grave o mas importante arriba para esto usaría una cola

**Responde esta pregunta en notebook.md.**

## 2. Operación dominante


**Pregunta:** ¿Qué costo se repite si extraemos mínimos desde una lista sin ordenar?
- se ahorra mucho trabajo por que al quitar los minimos la maquina ya no tiene que buscar entre muchas cosas

**Responde esta pregunta en notebook.md.**
## 3. Cola FIFO vs cola de prioridad

**Pregunta:** ¿Cuándo sería incorrecto usar una cola FIFO?
- por ejemplo en el ejemplo del hospital por que que tal si el mas grave llega y enseguida llega alguien que solo tiene gripa, el sistema le dará prioridad a quien tiene gripa y eso estaría mal

**Responde esta pregunta en notebook.md.**
## 4. Descubrimiento manual

**Pregunta:** ¿Qué permanece estable después de insertar un valor?
- que si ese valor es mayor al resto permanece al final de la fila
**Pregunta adicional:** Completa la fila correspondiente a insertar `9` y explica por qué se detiene la reparación.
- AP  = [7, 3, 9], 9 no tiene padre, [3, 7, 9], 1 intercambio
**Responde esta pregunta en notebook.md.**
## 5. Qué es un heap



**Pregunta:** ¿Por qué un heap no es un BST?
- Un BST exige otra relación: todo el subárbol izquierdo es menor que el nodo y todo el derecho es mayor. El heap no ofrece esa separación, así que buscar un valor arbitrario puede requerir revisar muchos nodos.

**Responde esta pregunta en notebook.md.**
## 6. Propiedad de min-heap

- 



**Pregunta:** ¿Los hermanos deben estar ordenados entre sí?
- no nescesariamente siempre y cuando cumplan que el minimo de ambos es menor igual a del padre, todo bien.

**Responde esta pregunta en notebook.md.**
## 7. Árbol binario completo


**Pregunta:** ¿Qué ventaja da esta forma para almacenar el árbol?
- da una forma mas predeterminada de como trabajar directamente sobre al árbol

**Responde esta pregunta en notebook.md.**
## 8. Representación por arreglo


**Pregunta:** Para `[2, 5, 4, 9]`, ¿qué valor está en el índice 2?
- justo el 2

**Responde esta pregunta en notebook.md.**
## 9. Fórmulas de índices


**Pregunta:** ¿Cuáles son los hijos del índice 2?
- 4 y 5 son sus hijos

**Responde esta pregunta en notebook.md.**
## 10. Inserción
**Pregunta adicional:** Si insertas `1` en `[2, 5, 4, 9, 8, 7]`, ¿con qué valores esperas que se compare antes de llegar a su posición final?
- unicamente con el 2 ya que estan ordenados de forma ascendente 



**Pregunta:** ¿Por qué no insertamos directamente en la raíz?
- por que perdemos generalidad acerca de sus hijos

**Responde esta pregunta en notebook.md.**
## 11. Sift-up


**Pregunta:** ¿Cuándo se detiene sift-up?
- significa “hacer subir” el valor recién insertado mientras sea más prioritario que su padre. No recorre todo el arreglo: sigue una sola cadena de ancestros.

**Responde esta pregunta en notebook.md.**
## 12. Extracción del mínimo



**Pregunta:** ¿Por qué se mueve el último elemento?
- se perdería la representación compacta del árbol completo.
**Responde esta pregunta en notebook.md.**
## 13. Sift-down



**Pregunta:** ¿Por qué debemos elegir el hijo menor?
- por que es de donde podemos trabajar

**Responde esta pregunta en notebook.md.**
## 14. Visualizaciones ipywidgets



**Pregunta:** ¿Qué relación observas entre la celda del arreglo y el nodo resaltado?


**Responde esta pregunta en notebook.md.**
## 15. Comparación BST, AVL y heap



**Pregunta:** ¿Qué elegirías para búsquedas arbitrarias y qué para extraer mínimos?

**Responde esta pregunta en notebook.md.**
## 16. Complejidad


**Pregunta:** ¿Por qué sift-up y sift-down son logarítmicos?

**Responde esta pregunta en notebook.md.**
## 17. Last Stone Weight



**Pregunta:** ¿Cuál es la operación dominante y el resultado del ejemplo?

**Responde esta pregunta en notebook.md.**
## 18. Pruebas


**Pregunta:** ¿Qué error específico detecta una extracción con varios descensos?

**Responde esta pregunta en notebook.md.**
## 19. Revisión técnica


**Pregunta:** ¿Qué debe incluir `revision_nombre_revisor.md`?

**Responde esta pregunta en notebook.md.**
## 20. Preparación para Dijkstra



**Pregunta:** ¿Qué guardaría la prioridad en Dijkstra?

**Responde esta pregunta en notebook.md.**
## 21. Cierre


**Pregunta:** ¿Qué criterio usarás para elegir una estructura en un problema nuevo?

**Responde esta pregunta en notebook.md.**
