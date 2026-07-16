# Reflexión técnica - Clase 08

Nombre: Santiago Vázquez Serna

## Ideas recurrentes

¿Qué ideas aparecieron en varios recursos?

Casi todas las optimizaciones (sean pilas monótonas o hash maps) sacrifican el uso de más memoria ram O(n) en espacio a cambio de reducir dramáticamente el tiempo de ejecución. Descartar cálculos repetidos entendiendo el "invariante" de la estructura. Guardar solo lo que tiene potencial de ser usado después. Iterar arreglos dentro de otros arreglos O(n^2) casi siempre es señal de que se omitió una propiedad estructural de los datos.

## Comparación crítica

Compara al menos dos recursos.

| Aspecto | CP-Algorithms (Escrito) | NeetCode (Video) |
| --- | --- | --- |
| Claridad | Denso, usa notación formal matemática. | Muy intuitivo, lenguaje del día a día. |
| Ejemplos | Plantea ecuaciones algorítmicas abstractas. | Resuelve un ejercicio explícito de LeetCode. |
| Profundidad | Demuestra formalmente los teoremas de complejidad. | Analiza la complejidad, pero sin pruebas formales. |
| Visualizaciones | Ninguna. | Usa dibujos y simulaciones manuales gráficas en pantalla. |
| Código | C++ altamente optimizado, a veces críptico. | Python muy limpio y legible. |

## Recurso más útil

¿Cuál fue el recurso más útil para ti y por qué?

CP-Algorithms me pareció el más útil proque hace que los algoritmos se vean casi como lemas, demostrando por qué funcionan para todos los casos límite.

## Recurso menos recomendable

¿Cuál fue el recurso menos recomendable o menos claro y por qué?

El de Makigas, porque aunque son buenos para un público primario que desconoce en su totalidad el tema, para el nivel universitario se vuelven lentos porque omiten las matemáticas detrás de las estructuras, centrándose solo en la sintaxis y no en la lógica detrás.

## Relación con el curso

¿Cómo se conecta esta investigación con Josephus, Nearest Smaller Values, pilas, colas, diccionarios o pruebas?

Toda la investigación siempre vuelve a cómo el modelado inicial del problema (clase 06) determina el éxito del algoritmo. Para Nearest Smaller Values, necesitábamos una Pila, lo que está haciendo verdaderamente esta investigación es formalizar que dicho patrón es universal y tiene nombre (Pila Monótona).

## Preguntas nuevas

Formula al menos tres preguntas técnicas que quieras resolver en las siguientes clases.

1. Si una estructura mantiene un orden estricto borrando elementos (como la Pila Monótona), ¿cómo podemos recuperar esos elementos si necesitamos retroceder en el tiempo?
2. La documentación dice que Python implementa los Diccionarios como Tablas Hash muy eficientes. Si la dispersión de datos es muy mala, ¿cómo Python evita matemáticamente colapsar a un rendimiento lineal O(n)?
3. Para problemas donde se cruzan la Ventana Deslizante y la Pila Monótona (una estructura que caduque por tiempo y descarte por valor), ¿cómo se implementa el código en Python evitando bugs de invariancia?

## Qué explicarías diferente

Si tuvieras que explicar uno de los temas investigados a otro estudiante, ¿qué cambiarías respecto a los recursos que consultaste?

Al explicar las Estructuras Monótonas, no empezaría mostrando la Pila ni el código. Empezaría escribiendo una lista de números en el pizarrón y jugaría un juego de "eliminación" basado en relaciones de orden (ej: "si yo mido 1.80m y tú estás detrás de mí y mides 1.60m, ¿alguien de enfrente te podrá ver?").