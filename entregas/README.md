# Entregas por alumno

Esta carpeta organiza longitudinalmente el trabajo entregado durante el curso.
Cada alumno tiene un identificador estable y una subcarpeta por clase:

```text
entregas/<alumno>/clase_XX/
```

El archivo [`alumnos.csv`](alumnos.csv) resume nombres y clases. Cada carpeta
de alumno contiene además un README con enlaces a sus entregas. La vista por
clase se encuentra en [`../docs/entregas_por_clase/`](../docs/entregas_por_clase/).

> [!IMPORTANT]
> El contenido dentro de cada `clase_XX/` corresponde al trabajo entregado
> durante el curso. Los índices no constituyen una evaluación académica.

Los archivos derivados se regeneran desde la raíz con:

```bash
python3 scripts/generar_indices.py
```

