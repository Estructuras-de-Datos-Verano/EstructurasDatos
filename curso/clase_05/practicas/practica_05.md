# Práctica 05: Colas, FIFO y pruebas con pytest

## Objetivos

Al terminar esta práctica podrás:

- Explicar la diferencia entre una pila y una cola.
- Reconocer el comportamiento FIFO.
- Implementar o revisar `ColaLista` y `ColaDeque`.
- Identificar por qué `pop(0)` puede ser costoso.
- Escribir pruebas básicas con `assert`.
- Ejecutar pruebas con `pytest`.
- Usar `pytest.raises` y `pytest.mark.parametrize`.
- Practicar el flujo de trabajo con GitHub.

## Instrucciones generales

Trabaja en tu rama personal. Puedes discutir ideas con tus compañeros, pero tu notebook, resumen y evidencia de pruebas deben ser tuyos.

No modifiques directamente `main`.

## Ejercicio 1: Completar el notebook

Abre:

```text
notebooks/clase_05_colas_fifo_pytest.ipynb
```

Ejecuta las celdas en orden y responde las preguntas marcadas.

## Ejercicio 2: Implementar o revisar colas

Revisa:

```text
src/colas.py
```

Las clases principales son:

- `ColaLista`
- `ColaDeque`

Ambas deben respetar:

```python
encolar(elemento)
desencolar()
frente()
esta_vacia()
tamano()
```

`desencolar()` y `frente()` sobre cola vacía deben lanzar `IndexError`.

## Ejercicio 3: Completar pruebas

Revisa:

```text
tests/test_colas.py
```

Las pruebas deben verificar:

- Una cola recién creada está vacía.
- Después de `encolar`, la cola no está vacía.
- `tamano` aumenta y disminuye.
- `desencolar` respeta FIFO.
- `frente` muestra el primer elemento sin eliminarlo.
- `desencolar` sobre cola vacía lanza `IndexError`.
- `frente` sobre cola vacía lanza `IndexError`.
- La misma prueba puede aplicarse a `ColaLista` y `ColaDeque`.

Agrega al menos una prueba propia en el espacio marcado.

## Ejercicio 4: Ejecutar pytest

Desde la carpeta `clase_05/`, ejecuta:

```bash
pytest
```

Guarda la evidencia:

```bash
pytest > evidencia_pytest.txt
```

## Ejercicio 5: Reflexión

Crea un archivo `resumen.md` con respuestas a:

1. ¿Cuál es la diferencia más importante entre una pila y una cola?
2. ¿Cuál implementación fue más clara para ti?
3. ¿Cuál implementación parece más eficiente para muchas extracciones?
4. ¿Qué aprendiste de `pytest` al probar dos implementaciones?
5. ¿Dónde usarías una cola en un problema de Matemáticas Aplicadas?
6. ¿Qué duda te queda?

## Entrega individual

Entrega mediante Pull Request:

```text
entregas/nombre/clase_05/
├── clase_05_colas_nombre.ipynb
├── resumen.md
└── evidencia_pytest.txt
```

## Actividad GitHub

1. Crea una issue o toma una issue asignada.
2. Crea una rama con el formato:

```text
clase-05-tu-nombre
```

3. Trabaja en tu carpeta de entrega.
4. Haz commit con un mensaje claro.
5. Abre Pull Request.
6. Revisa el PR asignado por `asignar_revisiones.py`.
7. Deja al menos un comentario constructivo.

## Checklist de entrega

- [ ] Ejecuté el notebook en orden.
- [ ] Revisé o completé `ColaLista`.
- [ ] Revisé o completé `ColaDeque`.
- [ ] Entiendo la diferencia entre LIFO y FIFO.
- [ ] Entiendo por qué `pop(0)` puede ser costoso.
- [ ] Ejecuté `pytest`.
- [ ] Guardé `evidencia_pytest.txt`.
- [ ] Agregué al menos una prueba propia.
- [ ] Escribí `resumen.md`.
- [ ] Trabajé en una rama propia.
- [ ] Abrí Pull Request.
- [ ] Revisé el PR asignado.
- [ ] No trabajé directamente sobre `main`.

## Criterios de evaluación

| Criterio | Puntos |
| --- | ---: |
| Comprensión de FIFO y comparación con pilas | 20 |
| Implementaciones de cola | 25 |
| Pruebas con `assert` y `pytest` | 25 |
| Reflexión comparativa | 15 |
| GitHub y revisión | 15 |

Total: 100 puntos.

