# Revisión técnica de la entrega de Santiago Saldívar

**Resultados de la ejecución**
Corrí tu archivo de pruebas con pytest y me da gusto confirmar que las 12 pruebas pasaron sin ningún problema en 0.03 segundos[cite: 7]. Esto demuestra que la lógica fundamental del árbol está sólida.

**Sobre tu código (Implementación)**
* Tu método `_balancear` está muy bien estructurado. Es fácil de leer cómo separas y manejas los cuatro escenarios de desbalance (LL, RR, LR, RL) evaluando si los valores son positivos o negativos[cite: 5].
* Vi que en tus métodos `_rotar_izquierda` y `_rotar_derecha` no solo reasignas los punteros de los nodos, sino que actualizas la altura de ambos nodos involucrados al instante. Esto es clave para que el algoritmo no pierda la cuenta al ir creciendo[cite: 5].

**Sobre tus pruebas de software**
* Me parecieron muy buenas tus 3 pruebas adicionales[cite: 7, 8]. 
* Destaco en especial tu prueba `test_agregado_3_insercion_balanceada_persiste`[cite: 7, 8]. Es una excelente idea comprobar a mano la estructura exacta de un árbol que ya entra balanceado, para confirmar que el código no hace rotaciones "fantasma" o innecesarias.
* Concuerdo con tu conclusión: el único caso importante que te faltó probar es uno con muchísimos nodos[cite: 7]. Hubiera estado genial agregar un `for` con mil números para ver cómo se comportaba la memoria y el balance.

**Respuesta a tu pregunta abierta**
* **¿Qué significa AVL?** No es un término técnico complejo, ¡son apellidos! Las siglas provienen de los inventores de este algoritmo: los matemáticos soviéticos Georgy **A**delson-**V**elsky y Evgenii **L**andis. Ellos diseñaron esta estructura en 1962.

¡Gran trabajo con tu entrega!