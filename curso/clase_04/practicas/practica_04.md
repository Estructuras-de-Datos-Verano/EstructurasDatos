# Práctica 04: Pilas abstractas, polimorfismo y pytest

## Objetivos

Al terminar esta práctica podrás:

- Explicar qué es una clase abstracta como contrato.
- Implementar `PilaLista`, `PilaDeque` y `PilaTupla`.
- Comparar ventajas y desventajas de varias implementaciones.
- Usar polimorfismo con funciones que reciben cualquier pila.
- Escribir pruebas básicas con `assert`.
- Ejecutar pruebas con `pytest`.
- Usar `pytest.raises` y `pytest.mark.parametrize`.

## Instrucciones generales

Trabaja en tu rama personal. Puedes discutir ideas con tus compañeros, pero tu notebook, resumen y evidencia de pruebas deben ser tuyos.

No modifiques directamente `main`.

## Ejercicio 1: Completar el notebook

Abre:

```text
notebooks/clase_04_pilas_abstractas_pytest.ipynb
```

Ejecuta las celdas en orden y completa las preguntas de reflexión.

## Ejercicio 2: Implementar pilas

Completa o revisa las implementaciones:

- `PilaLista`
- `PilaDeque`
- `PilaTupla`

Todas deben respetar:

```python
push(elemento)
pop()
peek()
esta_vacia()
tamano()
```

`pop()` y `peek()` sobre pila vacía deben lanzar `IndexError`.

## Ejercicio 3: Completar pruebas básicas

Revisa:

```text
tests/test_pilas.py
```

Las pruebas deben verificar:

- Una pila recién creada está vacía.
- Después de `push`, la pila no está vacía.
- `tamano` aumenta y disminuye.
- `pop` respeta LIFO.
- `peek` muestra la cima sin eliminarla.
- `pop` sobre pila vacía lanza `IndexError`.
- `peek` sobre pila vacía lanza `IndexError`.
- La misma prueba puede aplicarse a varias implementaciones.

## Ejercicio 4: Ejecutar pytest

Desde la carpeta `clase_04/`, ejecuta:

```bash
pytest
```

Guarda la evidencia:

```bash
pytest > evidencia_pytest.txt
```

## Ejercicio 5: Reflexión

Crea un archivo `resumen.md` con:

1. Cuál implementación fue más clara.
2. Cuál implementación parece más eficiente.
3. Qué aprendiste de `pytest`.
4. Qué prueba te pareció más importante.
5. Qué duda te queda.

## Entrega individual

Entrega mediante Pull Request:

```text
entregas/nombre/clase_04/
├── clase_04_pilas_nombre.ipynb
├── resumen.md
└── evidencia_pytest.txt
```

## Actividad GitHub

1. Crea una rama con el formato:

```text
clase-04-tu-nombre
```

2. Trabaja en tu carpeta de entrega.
3. Haz commit con un mensaje claro.
4. Abre Pull Request.
5. Revisa el PR asignado por `asignar_revisiones.py`.
6. Deja al menos un comentario constructivo.

## Checklist de entrega

- [ ] Ejecuté el notebook en orden.
- [ ] Implementé o revisé `PilaLista`.
- [ ] Implementé o revisé `PilaDeque`.
- [ ] Implementé o revisé `PilaTupla`.
- [ ] Ejecuté `pytest`.
- [ ] Guardé `evidencia_pytest.txt`.
- [ ] Escribí `resumen.md`.
- [ ] Trabajé en una rama propia.
- [ ] Abrí Pull Request.
- [ ] Revisé el PR asignado.
- [ ] No trabajé directamente sobre `main`.

## Criterios de evaluación

| Criterio | Puntos |
| --- | ---: |
| Clase abstracta e interfaz | 20 |
| Implementaciones de pila | 25 |
| Pruebas con `assert` y `pytest` | 25 |
| Reflexión comparativa | 15 |
| GitHub y revisión | 15 |

Total: 100 puntos.
