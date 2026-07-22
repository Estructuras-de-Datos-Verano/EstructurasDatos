### De secuencias a relaciones. 
    Ahora tenemos una nueva froma de almacenar datos, la cual nos dice no solo su posicion, sino que ahora nos da infromacion sobre si se relaciona y como con otros datos
### Problemas CSES.
Hay multiples fromas de implementar esta estructura, tenemos varios ejemplos en esta clase:
| Problema | Nodo | Arista | Dirigido | Ponderado | Pregunta algorítmica |
| --- | --- | --- | --- | --- | --- |
| Building Roads | Una ciudad | Carretera entre 2 ciudades | No | No | Encontrar la cantidad de ciudades conectadas |
| Counting Rooms | Un suelo | Adyacencia entre 2 suelos | No | No | Encontrar el número de conexiones que hay |
| Labyrinth | Suelo, inicio o final | Movimiento válido a otra casilla | No | No | Encontrar el camino más corto (si hay) |
| Message Route | Una computadora | Conexión de red directa | No | No | Búsqueda del camino más corto |

### Elección de representación.
    usamos grafos porque es la froma mas natural de representar esta estrcutura, de hecho es la ideal
### Polimorfismo.
    El polimorfismo en esta clase de nuevo nos ayuda a poder ejecutar pruebas con mayor rapidez y sencillez
### NetworkX.
    Es una libreria que en esta clase nos ayuda a ver una representacion visual de nuestro codigo
### Pruebas.
    Las pruebas en esta clase estan orientadas a ver que nuestras clase funciona de manera esperada con ciertos datos; Las pruebas extras verifican, un caso extremo y uno habitul con mas vertices
### Patrón descubierto.
    Entiendo que para modelar relaciones necesitamos primero sentar bien las baces de como se relacionan nuestro datos y que datos son, serviria contestar primer mentalmente las definiciones; 
    - ¿Que hace que un vertice tenga vecinos? ¿Que es un vertices? ¿Que es una arista?

    Y asi podemos empezar a modelar diferentes tipos de datos en grafos
### Pregunta abierta.
    ¿Como podemos modelar un grafo ponderado con la libreria NetworkX?
