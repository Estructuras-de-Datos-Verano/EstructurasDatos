# Práctica 01: Representar para operar mejor

## Objetivos

Al terminar esta práctica podrás:

- Explicar informalmente qué es una estructura de datos.
- Distinguir problema, representación, algoritmo y resultado.
- Medir tiempos simples con `time.perf_counter`.
- Comparar búsquedas en `list` y `set`.
- Comparar conteos con `dict` y `Counter`.
- Usar una rama de GitHub para entregar cambios mediante pull request.

## Instrucciones generales

Trabaja en tu rama personal del repositorio del curso. Puedes discutir ideas con tus compañeros, pero cada entrega debe incluir tus propias respuestas y conclusiones.

Tiempo sugerido: 60 a 90 minutos.

## Ejercicio 1: Búsqueda

1. Abre el notebook `notebooks/clase_01_estructuras_y_eficiencia.ipynb`.
2. Ejecuta las celdas de importación y generación de datos.
3. Mide la búsqueda de un valor presente y un valor ausente en una lista.
4. Repite la medición usando un conjunto.
5. Escribe una conclusión breve:
   - ¿Cuál estructura fue más rápida?
   - ¿Cambió algo entre buscar un valor presente y uno ausente?
   - ¿Qué operación estamos intentando hacer eficiente?

## Ejercicio 2: Conteo de frecuencias

1. Usa la misma lista de datos.
2. Cuenta frecuencias con un diccionario.
3. Cuenta frecuencias con `Counter`.
4. Verifica que ambos resultados representen la misma información.
5. Responde:
   - ¿Qué hace más explícito el diccionario?
   - ¿Qué hace más cómodo `Counter`?
   - ¿En qué caso preferirías cada opción?

## Ejercicio 3: Problema, representación, algoritmo, resultado

Elige uno de estos escenarios:

- Una red social pequeña.
- Rutas entre puntos de una ciudad.
- Calificaciones de estudiantes.
- Repeticiones de palabras en textos.

Para tu escenario, completa:

| Elemento | Tu respuesta |
| --- | --- |
| Problema | |
| Representación de datos | |
| Algoritmo | |
| Resultado esperado | |
| Operación que debe ser eficiente | |

## Ejercicio 4: Actividad de GitHub

1. Clona el repositorio del curso si aún no lo tienes.
2. Crea una rama con el formato `clase-01-tu-nombre`.
3. Edita el `README.md` del proyecto del curso y agrega:
   - Tu nombre.
   - Una frase sobre qué esperas aprender.
   - Una pregunta que te dejó la clase.
4. Guarda tus cambios con un commit claro.
5. Sube la rama a GitHub.
6. Abre un pull request.
7. Solicita revisión de al menos una persona.

## Preguntas de reflexión

Responde en el notebook o en un archivo Markdown dentro de tu rama:

1. ¿Por qué una lista no siempre es la mejor representación?
2. ¿Qué ganamos al cambiar de lista a conjunto?
3. ¿Qué se pierde o cambia cuando usamos un conjunto?
4. ¿Por qué un diccionario es natural para contar?
5. ¿Qué relación ves entre estructuras de datos y Programación Orientada a Objetos?

## Entrega

Entrega mediante un pull request que incluya:

- Tus respuestas de reflexión.
- El notebook ejecutado o una versión con tus respuestas guardadas.
- El cambio solicitado en el `README.md` del proyecto.

## Criterios de evaluación

| Criterio | Puntos |
| --- | ---: |
| Ejecuta correctamente los experimentos del notebook | 30 |
| Interpreta los resultados con claridad | 25 |
| Distingue problema, representación, algoritmo y resultado | 20 |
| Usa adecuadamente rama, commit y pull request | 15 |
| Presentación y claridad de la entrega | 10 |

Total: 100 puntos.
