# Revisión clase 14 hecha por Leo

## 1. Resumen.
Se realizó la práctica de mi compañero sobre MinHeaps, la correcta implementación y las respuestas cortas y concisas nos quieren decir que se entendió bien la estructura

## 2. Revisión conceptual.
Se entendió todo correctamente, esto se ve reflejado en la discusión 

## 3. Revisión de implementación.
Está correctamente implementada, me gustó que agregara comentarios para ayudar al revisor.

## 4. Revisión de pruebas.
Muy bien las pruebas, efectivamente revisa lo que se pide. Sin embaro, estaría extra pero perfecto que agregara su nombre en las pruebas para facilitar al revisor

## 5. Salida completa de `pytest -v`.

Ejecutando:
C:\Users\0254049\AppData\Local\Programs\Python\Python313\python.exe -m pytest -v C:\Users\0254049\Documents\GitHub\EstructurasDatos\clase_14\tests C:\Users\0254049\Documents\GitHub\EstructurasDatos\entregas\clase_14\LEO\test_estudiante.py

============================================= test session starts =============================================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0254049\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0254049\Documents\GitHub\EstructurasDatos\clase_14
configfile: pytest.ini
collected 16 items                                                                                             

clase_14\tests\test_publico_heap.py::test_heap_nuevo_esta_vacio PASSED                                   [  6%]
clase_14\tests\test_publico_heap.py::test_insertar_un_valor_y_consultar_minimo PASSED                    [ 12%]
clase_14\tests\test_publico_heap.py::test_insertar_varios_conserva_minimo_y_propiedad PASSED             [ 18%]
clase_14\tests\test_publico_heap.py::test_extraer_minimo_devuelve_orden_creciente PASSED                 [ 25%]
clase_14\tests\test_publico_heap.py::test_vacio_lanza_error_al_consultar_o_extraer PASSED                [ 31%]
clase_14\tests\test_publico_heap.py::test_duplicados_y_negativos PASSED                                  [ 37%]
clase_14\tests\test_publico_heap.py::test_construir_heap_reemplaza_contenido PASSED                      [ 43%]
clase_14\tests\test_publico_heap.py::test_varios_sift_up PASSED                                          [ 50%]
clase_14\tests\test_publico_heap.py::test_varios_sift_down PASSED                                        [ 56%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras0-0] PASSED                               [ 62%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras1-5] PASSED                               [ 68%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras2-0] PASSED                               [ 75%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras3-1] PASSED                               [ 81%]
clase_14::test_varios_cambios_por_insercion_LEO <- ..\entregas\clase_14\LEO\test_estudiante.py PASSED    [ 87%]
clase_14::test_extraccion_varios_niveles_LEO <- ..\entregas\clase_14\LEO\test_estudiante.py PASSED       [ 93%]
clase_14::test_ultima_piedra_caso_extremo_LEO <- ..\entregas\clase_14\LEO\test_estudiante.py PASSED      [100%]

============================================= 16 passed in 0.04s ==============================================
PS C:\Users\0254049\Documents\GitHub\EstructurasDatos> 

#### Comando ejecutado:
py evaluar.py entregas/clase_14/LEO clase_14/tests entregas/clase_14/LEO/test_estudiante.py      

#### Interpretación
La implementación de mi compañero está perfectamente hecha

## 6. Fortalezas.
Buen código, buenas pruebas, se entendió correctamente lo que se explica en la práctica, es muy veloz para hacer las prácticas y lo hace bien

## 7. Mejoras.
Siento que estaría mucho mejor que las respuestas de notebook y discusión fueran más profundas y reflexivas, pues parte de este curso es aprender a redactar y discutir, además que así se facilita el aprendizaje

## 8. Conclusión.
Muy buena práctica, faltó reflexión, pero fuera de eso perfectos

## 9. Respuesta del autor con checklist.

- [ X ] Resumí el enfoque sin reescribir la solución.
- [ X ] Revisé propiedad de heap, índices, sift-up y sift-down.
- [ X ] Revisé nombres, firmas, docstrings y errores.
- [ X ] Ejecuté tests públicos y propios con `pytest -v`.
- [ X ] Incluí la salida completa.
- [ X ] Separé fortalezas de mejoras accionables.
- [ X ] Cerré con una conclusión.