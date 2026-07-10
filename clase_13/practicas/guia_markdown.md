# Guía de Markdown para la Clase 13

Markdown no es decoración: es una herramienta para comunicar decisiones técnicas.

> [!NOTE]
> Usa esta guía para `notebook.md`, `discusion.md`, `reporte_pytest.md` y `revision_nombre.md`.

## Encabezados

```markdown
# Título principal
## Sección
### Subsección
```

## Listas

Lista sin orden:

```markdown
- Implementación
- Pruebas
- Revisión
```

Lista numerada:

```markdown
1. Leo el problema.
2. Diseño el algoritmo.
3. Escribo pruebas.
```

## Tablas

```markdown
| Caso | Rotación | Nueva raíz |
| --- | --- | --- |
| LL | derecha | hijo izquierdo |
| RR | izquierda | hijo derecho |
```

Resultado esperado:

| Caso | Rotación | Nueva raíz |
| --- | --- | --- |
| LL | derecha | hijo izquierdo |
| RR | izquierda | hijo derecho |

## Bloques de código

````markdown
```python
def altura(nodo):
    return 0 if nodo is None else nodo.altura
```
````

## Citas

```markdown
> Una rotación preserva el inorden del BST.
```

> Una rotación preserva el inorden del BST.

## Checkboxes

Sintaxis:

```markdown
- [ ] Pendiente
- [x] Hecho
```

Ejemplo:

- [ ] Ejecutar pruebas públicas.
- [x] Escribir el primer borrador de la discusión.

## Alertas de GitHub

```markdown
> [!NOTE]
> Información útil.

> [!TIP]
> Consejo práctico.

> [!IMPORTANT]
> Algo que no debe pasarse por alto.

> [!WARNING]
> Riesgo probable.

> [!CAUTION]
> Riesgo alto o posible pérdida de trabajo.
```

> [!IMPORTANT]
> Usa alertas con intención. Si todo es importante, nada destaca.

## Details

````markdown
<details>
<summary>Ver explicación</summary>

Una rotación cambia enlaces locales, pero conserva el orden inorden.

</details>
````

<details>
<summary>Ver explicación</summary>

Una rotación cambia enlaces locales, pero conserva el orden inorden.

</details>

## Enlaces

```markdown
[Guía de GitHub](guia_github.md)
```

[Guía de GitHub](guia_github.md)

## Enlaces internos

```markdown
[Ir a alertas](#alertas-de-github)
```

[Ir a alertas](#alertas-de-github)

## Emojis

Los emojis pueden usarse con moderación en comentarios informales. En documentos técnicos del curso, prefiere claridad verbal.

Ejemplo aceptable:

```markdown
Buen avance. El caso LR ya queda cubierto.
```

## Referencias oficiales

- GitHub Flavored Markdown: https://github.github.com/gfm/
- Basic Writing and Formatting: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
- Task Lists: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-task-lists
- Details: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections
- Code Blocks: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks
