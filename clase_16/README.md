# Clase 16 — Implementación robusta de Dijkstra

> [!IMPORTANT]
> Una implementación confiable hace explícitos sus contratos, protege sus invariantes y demuestra sus decisiones con pruebas.

La Clase 15 construyó la intuición de Dijkstra. Ahora leeremos y construiremos la versión completa: representación flexible, normalización, copia defensiva, errores claros, entradas obsoletas, reconstrucción y pruebas profesionales.

## Ruta de trabajo

1. Abre `notebooks/clase_16_implementacion_robusta_dijkstra.ipynb`.
2. Registra respuestas en `entregas/clase_16/nombre/notebook.md`.
3. Audita `src/dijkstra_para_revisar.py` antes de modificar tu entrega.
4. Sigue `practicas/practica_16.md` y escribe pruebas antes de cada corrección.
5. Desde `curso-alumnos`, ejecuta:

```bash
python3 evaluar.py entregas/clase_16/nombre clase_16/tests entregas/clase_16/nombre/test_estudiante.py
```

PowerShell:

```powershell
py evaluar.py entregas/clase_16/nombre clase_16/tests entregas/clase_16/nombre/test_estudiante.py
```

## Recursos

- Presentación local: `presentacion/index.html`.
- Explorador de lectura: `src/visualizador_codigo.py`.
- Contratos de referencia: `src/contratos_dijkstra.py`.
- Código para auditar: `src/dijkstra_para_revisar.py`.
- Guías de Markdown, GitHub y revisión: `practicas/recursos/`.

> [!NOTE]
> El código para revisar está incompleto de manera intencional. No lo copies como entrega: convierta cada hallazgo en una prueba reproducible.

