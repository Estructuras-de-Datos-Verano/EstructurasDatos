# Reflexion tecnica - Clase 08

Nombre: Aristeo

## Ideas recurrentes

Que ideas aparecieron en varios recursos?

- La idea de que las estructuras de datos no se eligen por costumbre o de forma arbitraria, sino respondiendo directamente a la pregunta o necesidad que el problema plantea (por ejemplo, conservar información útil y descartar la que deja de aportar).
- El impacto crítico de la complejidad algorítmica (Big-O), enfatizando que una solución no solo debe ser correcta por fuerza bruta, sino que debe escalar eficientemente (lineal, cuadrática, etc.) según la estructura subyacente.
- La relevancia de utilizar representaciones visuales e intuitivas (como diagramas de flujo o árboles de decisión) para modelar y entender el espacio de soluciones antes de escribir código.

## Comparacion critica

Compara al menos dos recursos.

| Aspecto | Recurso A: Abdul Bari (Videos) | Recurso B: HackerRank (Estructuras) |
| --- | --- | --- |
| Claridad | Excelente nivel pedagógico para desglosar fórmulas y conceptos abstractos. | Directo y muy enfocado en la aplicación práctica del código. |
| Ejemplos | Teóricos y matemáticos (bucles, polinomios, combinatoria de niños). | Prácticos y orientados a resolver desafíos específicos en su plataforma. |
| Profundidad | Alta, analiza a fondo el comportamiento matemático de Big-O y restricciones. | Baja-Media, asume que ya entiendes los conceptos teóricos de base. |
| Visualizaciones | Sobresalientes mediante trazos manuales y diagramas lógicos de árboles. | Limitadas a la explicación de la sintaxis o interfaces de problemas. |
| Codigo | Abstracto o en pseudocódigo, enfocado puramente en la lógica del algoritmo. | Centrado en la implementación exacta y funcional dentro de un entorno real. |

## Recurso mas util

Cual fue el recurso mas util para ti y por que?

- Los videos de Abdul Bari (en especial el de Complejidad Temporal) porque desmitifican la notación Big-O mediante explicaciones matemáticas muy accesibles, demostrando que un orden cuadrático proviene de un análisis polinomial real en bucles anidados y no de una simple regla memorizada, lo cual es clave para evaluar la eficiencia en nuestro curso.

## Recurso menos recomendable

Cual fue el recurso menos recomendable o menos claro y por que?

- La sección conceptual de HackerRank porque, aunque es una excelente plataforma interactiva para programar y practicar ejercicios, sus explicaciones teóricas son sumamente escuetas y asumen de forma anticipada que el lector ya posee el criterio técnico para decidir por qué una estructura encaja en el escenario propuesto.

## Relacion con el curso

Como se conecta esta investigacion con Josephus, Nearest Smaller Values, pilas, colas, diccionarios o pruebas?

- La investigación conecta con Josephus porque nos obliga a medir con precisión matemática (siguiendo a Abdul Bari) la complejidad temporal real de simular el proceso de eliminación paso a paso. También se relaciona con Nearest Smaller Values porque la pila monótona actúa como un filtro que procesa información bajo restricciones específicas, un concepto análogo a cómo el Backtracking poda ramas inútiles en un árbol de decisiones. Finalmente, comprender el funcionamiento interno de las Hash Tables en HackerRank nos da la intuición de cuándo buscar accesos eficientes O(1) usando los diccionarios de Python vistos en clase.

## Preguntas nuevas

Formula al menos tres preguntas tecnicas que quieras resolver en las siguientes clases.

1. ¿Cómo se calcula matemáticamente y con exactitud la complejidad temporal de un algoritmo que opera bajo un orden de raíz cuadrada ($\mathcal{O}(\sqrt{n})$)?
2. ¿Cómo se traducen las restricciones abstractas de un árbol de Backtracking en condiciones lógicas o condicionales eficientes dentro de un código en Python?
3. ¿Qué penalización en memoria o tiempo de ejecución sufrimos al usar colas doblemente terminadas (`deque`) en lugar de listas nativas cuando el volumen de operaciones de simulación es masivo?

## Que explicarias diferente

Si tuvieras que explicar uno de los temas investigados a otro estudiante, que cambiarias respecto a los recursos que consultaste?

- Al explicar la complejidad temporal, no empezaría memorizando las gráficas de Big-O; en su lugar, usaría el enfoque de Abdul Bari analizando la cantidad de iteraciones reales en bucles con sumas de polinomios, demostrando que la teoría de algoritmos no es una regla arbitraria, sino una consecuencia lógica de contar instrucciones.