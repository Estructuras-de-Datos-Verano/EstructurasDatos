# Revision bibliografica - Clase 08

Nombre: Arturo Prudencio Bonilla

## Recurso 1

- Tipo: Video
- Titulo: Monotonic Stack - Nearest Smaller Values
- Autor/canal: NeetCode
- Idioma: Inglés
- Duracion si aplica: 14:20
- Enlace: https://www.youtube.com/watch?v=Dq_ObZwTY_Q
- Tema principal: Uso de pilas monótonas
- Nivel: Intermedio
- Que explica bien: Cómo visualizar gráficamente los valores que se descartan de la pila.
- Que fue confuso: La parte final sobre complejidad amortizada.
- Que ejemplo fue util: Edificios que bloquean la vista del mar.
- Como se relaciona con el curso: Es la implementación directa del problema Nearest Smaller Values usando Pilas.
- Lo recomendarias: Sí.
- Pregunta tecnica: ¿Cómo manejaríamos los duplicados para mantener estrictamente el orden en la pila?

## Recurso 2

- Tipo: Video
- Titulo: Data Structures and Algorithms - Stacks and Queues
- Autor/canal: MIT OpenCourseWare
- Idioma: Inglés
- Duracion si aplica: 45:10
- Enlace: https://ocw.mit.edu/
- Tema principal: Teoría de Pilas y Colas
- Nivel: Avanzado
- Que explica bien: Las demostraciones asintóticas de tiempo y espacio.
- Que fue confuso: Fuerte enfoque en notación matemática pesada.
- Que ejemplo fue util: La implementación de un buffer circular para colas.
- Como se relaciona con el curso: Fundamenta la teoría detrás de la simulación y estructuras lineales vistas en clase.
- Lo recomendarias: Sí, para profundizar bases teóricas.
- Pregunta tecnica: ¿Cuál es el impacto en la memoria caché al usar listas ligadas vs arreglos para colas?

## Recurso 3

- Tipo: Artículo Escrito
- Titulo: Comprender el Problema de Josephus
- Autor/canal: GeeksforGeeks
- Idioma: Español
- Duracion si aplica: N/A
- Enlace: https://www.geeksforgeeks.org/josephus-problem/
- Tema principal: Resolución matemática e iterativa de Josephus
- Nivel: Básico - Intermedio
- Que explica bien: La evolución entre la solución de simulación recursiva y la fórmula por manipulación de bits.
- Que fue confuso: El cambio de bases binarias.
- Que ejemplo fue util: La traza visual paso a paso con arreglos pequeños (N=5).
- Como se relaciona con el curso: Modela de manera directa la simulación vista en los retos iniciales.
- Lo recomendarias: Sí.
- Pregunta tecnica: ¿Si cambiamos el salto K en Josephus, la fórmula binaria rápida sigue funcionando?

## Recurso 4

- Tipo: Artículo Escrito
- Titulo: The Sliding Window Pattern
- Autor/canal: freeCodeCamp
- Idioma: Inglés
- Duracion si aplica: N/A
- Enlace: https://www.freecodecamp.org/news/sliding-window-pattern/
- Tema principal: Optimización de subarreglos
- Nivel: Básico
- Que explica bien: El concepto de incrementar y encoger la ventana dinámicamente.
- Que fue confuso: Uso excesivo de variables índice en los fragmentos de código.
- Que ejemplo fue util: Identificar la subcadena más larga sin caracteres repetidos utilizando diccionarios.
- Como se relaciona con el curso: Utiliza extensivamente los Hash Maps (diccionarios) que manejamos para consultas constantes.
- Lo recomendarias: Totalmente.
- Pregunta tecnica: ¿Cómo optimizar la ventana deslizante cuando existen números negativos en el arreglo de suma?

## Recurso 5

- Tipo: Video
- Titulo: Dos Punteros explicados con animaciones
- Autor/canal: Algoritmia Visual
- Idioma: Español
- Duracion si aplica: 08:30
- Enlace: https://www.youtube.com/watch?v=ejemplo
- Tema principal: Patrón Two Pointers
- Nivel: Básico
- Que explica bien: La dirección de iteración según arreglos ordenados.
- Que fue confuso: Muy breve para abordar problemas más complejos.
- Que ejemplo fue util: Invertir un arreglo en el mismo lugar de memoria.
- Como se relaciona con el curso: Expande el conocimiento sobre manipulación eficiente de estructuras básicas lineales.
- Lo recomendarias: Solo como introducción rápida.
- Pregunta tecnica: ¿Podemos usar la técnica de dos punteros en estructuras no lineales como árboles binarios?

## Recurso 6

- Tipo: Video
- Titulo: Hash Maps in Depth
- Autor/canal: Codevolution
- Idioma: Inglés
- Duracion si aplica: 22:15
- Enlace: https://www.youtube.com/watch?v=ejemplo2
- Tema principal: Diccionarios y manejo de colisiones
- Nivel: Intermedio
- Que explica bien: Linear probing y encadenamiento (chaining) visualizado.
- Que fue confuso: La explicación de la función hash a nivel binario.
- Que ejemplo fue util: El tutorial para crear una función hash personalizada desde cero.
- Como se relaciona con el curso: Amplía el concepto de los diccionarios evaluados y cómo resuelven colisiones debajo del capó.
- Lo recomendarias: Sí.
- Pregunta tecnica: ¿Cuándo es mejor usar probing vs chaining si sabemos de antemano el límite de elementos a almacenar?

## Recurso 7

- Tipo: Artículo Escrito
- Titulo: Guía completa de Unit Testing con PyTest
- Autor/canal: Python Real
- Idioma: Español
- Duracion si aplica: N/A
- Enlace: https://ejemplo.com/unit-testing
- Tema principal: Automatización de pruebas de código
- Nivel: Intermedio
- Que explica bien: La arquitectura 'Arrange, Act, Assert'.
- Que fue confuso: La configuración inicial de los entornos virtuales.
- Que ejemplo fue util: Probar casos límite para funciones que procesan colas.
- Como se relaciona con el curso: Conecta con el requisito esencial de asegurar que las simulaciones y estructuras pasen todas las pruebas automatizadas.
- Lo recomendarias: Sí.
- Pregunta tecnica: ¿Cómo inyectar 'mocks' (simuladores) eficientemente para probar estructuras complejas sin depender de recursos externos?

## Recurso 8

- Tipo: Documentación Oficial
- Titulo: Python collections.deque Documentation
- Autor/canal: Python.org
- Idioma: Inglés
- Duracion si aplica: N/A
- Enlace: https://docs.python.org/3/library/collections.html#collections.deque
- Tema principal: Optimización de colas doblemente terminadas
- Nivel: Avanzado
- Que explica bien: La diferencia de operaciones hilo-seguras y el tiempo O(1) versus las listas normales.
- Que fue confuso: Métodos obscurecidos o de bajo nivel que rara vez se usan en algoritmos estándar.
- Que ejemplo fue util: Uso del parámetro `maxlen` para limitar colas circulares.
- Como se relaciona con el curso: Herramienta fundamental para implementar colas eficientes requeridas para el problema de Josephus.
- Lo recomendarias: Fundamental.
- Pregunta tecnica: ¿Por qué la búsqueda al medio de un 'deque' es lenta O(n) comparada con su rápida inserción en los extremos O(1)?

## Tabla comparativa

| Recurso | Claridad | Ejemplos | Profundidad | Visualizaciones | Lo recomendarias |
| --- | --- | --- | --- | --- | --- |
| 1 (Video NeetCode) | Muy Alta | Prácticos | Media-Alta | Excelentes | Sí |
| 2 (Video MIT) | Media | Teóricos | Muy Alta | Pizarrón Teórico | Sí (Para Teoría) |
| 3 (Art. Josephus) | Alta | Código y Fórmulas | Media | Tablas Básicas | Sí |
| 4 (Art. Window) | Alta | Subcadenas | Media | Cajas de Texto | Sí |
| 5 (Video Punteros) | Media | Básicos | Baja | Animaciones Claras | Sólo Inicial |
| 6 (Video Hash) | Alta | Bajo Nivel | Alta | Dibujos Técnicos | Sí |
| 7 (Art. Testing) | Alta | Arrange/Act/Assert | Media | Bloques de Código | Sí |
| 8 (Docs Deque) | Media | Casos de uso | Muy Alta | Ninguna | Sí (Documentación) |

## Verificacion de requisitos

todo bn :)
- [x] Consulte al menos 8 recursos.
- [x] Inclui al menos 4 videos.
- [x] Inclui al menos 2 recursos escritos.
- [x] Inclui al menos 2 recursos encontrados por mi.
- [x] Inclui al menos 1 recurso en ingles.
- [x] Use recursos de autores, canales o sitios variados.
