# Reflexion tecnica - Clase 08

Nombre: Arturo Prudencio Bonilla

## Ideas recurrentes

Que ideas aparecieron en varios recursos?

- La necesidad de sacrificar memoria espacial (usando estructuras auxiliares como pilas, diccionarios o colas) para optimizar un monton la complejidad de tiempo (pasando de iteraciones anidadas cuadráticas a tiempo lineal).

## Comparacion critica

Compara al menos dos recursos.

| Aspecto | (NeetCode Video) | (GeeksforGeeks Artículo) |
| --- | --- | --- |
| Claridad | Excelente, paso a paso. | me parece aceptable, pero muy directo al algoritmo |
| Ejemplos | Visualización dibujada en pantalla | Fragmentos de código  |
| Profundidad | Se enfoca en la lógica detrás del patrón | Detalla MUUUCHO la complejidad Big-O |
| Visualizaciones | Dibujos interactivos de los punteros  | Tablas de estados estáticas |
| Codigo | Python muy legible e idiomático |  Múltiples lenguajes, a veces redundante |

## Recurso mas util

Cual fue el recurso mas util para ti y por que?

- El video de MIT OpenCourseWare; fue el más valioso porque no solo explica el código de una estructura, sino la demostración teórica de por qué una pila monótona garantiza la correctitud matemática al evaluar Nearest Smaller Values

## Recurso menos recomendable

Cual fue el recurso menos recomendable o menos claro y por que?

- El artículo introductorio en Medium, ya que pasaba por alto los casos límite y presentaba un código que fallaba con arreglos vacíos o valores duplicados, asumiendo demasiadas condiciones ideales.

## Relacion con el curso

Como se conecta esta investigacion con Josephus, Nearest Smaller Values, pilas, colas, diccionarios o pruebas?

- Los problemas vistos en clase son las fundaciones. Josephus nos introdujo empíricamente a la noción de Simulación mediante el uso de colas. Nearest Smaller Values materializó el poder de la Información monotónica usando pilas. Explorar patrones formaliza lo que ya hicimos intuitivamente y las pruebas unitarias son la única forma de validar las optimizaciones obtenidas al usar diccionarios o colas

## Preguntas nuevas

Formula al menos tres preguntas tecnicas que quieras resolver en las siguientes clases.

1. ¿Cómo impacta el proceso de recolección de basura al rendimiento al utilizar diccionarios masivos frente a arreglos de tamaño fijo?
2. ¿Cuándo se vuelve contraproducente el "overhead" de memoria de usar una pila o cola comparado con simples ciclos anidados en arreglos muy pequeños?
3. En implementaciones del mundo real, ¿se prefieren aproximaciones iterativas usando pilas, o llamadas recursivas apoyadas por la pila del sistema?

## Que explicarias diferente

Si tuvieras que explicar uno de los temas investigados a otro estudiante, que cambiarias respecto a los recursos que consultaste?

- Creo que para el patrón de Información monotónica, no comenzaría escribiendo código. Pediría al estudiante que resolviera "Nearest Smaller Values" físicamente usando cartas con valores como las del poker o parecido. Cuando se descartara físicamente una carta alta demostraría de inmediato la lógica de limpiar elementos inútiles de la pila
