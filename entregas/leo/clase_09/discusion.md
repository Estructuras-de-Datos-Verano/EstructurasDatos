# Discusion clase 09 - Leonardo Daniel Arenas Serafin

## 1. De secuencias a relaciones.
Las secuencias son estructuras que guardan y priorizan el orden de almecenamiento de los datos, mientras que las relaciones son estructuras que guardan y priorizan la información de cómo dos objetos se relacionan o interactuán entre sí.

## 2. Problemas CSES.
- Building Roads: problema en el que debemos conectar todos los las ciudades (vértices) con caminos (aristas) de forma que todas las ciudades existentes estén conectadas entre sí y que no haya más de un camino entre dos mismas ciudad. 
- Counting Rooms: problema en el que conforme a un mapa dado de muros y suelo, debemos de contar cuantas habitaciones hay en dicho mapa, contando que el suelo son los vértices y su continuidad (es decir, que no haya un muro en medio) son las aristas.
- Labrynth: problema en el que al igual que el de Counting Rooms, los vértices son las opciones de "camino" o suelo que hay y las aristas simbolizan la continuidad de dicho suelo, sin embargo aquí debemos de encontrar cuál es el camino más eficiente para llegar de punto a a punto b. Abre a la pregunta de ¿cómo es que podemos optimizar el camino?
- Message Route: problema en el que los vértices son computadoras y las aristas representan si existe una conexión entre ellas. El objetivo es ver si es posible mandar un mensaje de computadora a a computadora b, y si sí, cuál es el camino a seguir.

## 3. Elección de representación.
Los vértices generalmente se representan con círculos llamdos nodos, y las aristas con líneas que unen dichos vértices. En el archivo "entregas/clase_09/LEO/grafo_visual.png" hay un ejemplo de esto.
Para hacer estas relaciones hay dos formas de hacerlo, mediante una lista o mediante una matriz. La lista es mejor opción cuando no tenemos tantos vértices y queremos mantener la simplicidad, en cambio la matriz se vuelve muy útil a la hora de almacenar la información para muchos vértices. En particular, considero que la matriz es muy útil para casos en donde hayan relaciones dirigidad, es decir, que las aristas tengan sentido, pues la matriz puede llevar esta información con mucha facilidad.

## 4. Polimorfismo.
Definimos primeramente una clase abstracta de grafos para poder implementar polimorfismo a ambas representaciones de grafos. Esto porque ambas estructuras en realidad son la misma, y a la hora de trabajar con ellas es muy útil tener acceso a los mismos métodos.

## 5. NetworkX.
Una herramienta muy útil en donde podemos visualizar los grafos de una forma muy didáctica. Nosotros hemos hecho nuestra propia implementación de grafos, la cual debe de ser diferente a cualquier otra implementación existente. Esto podría causar problemas ya que al trabajar con el mismo concepto, pero con diferentes implementaciones puede llevar a confusiones y mal entendidos. Por eso es que importamos esta biblioteca externa, para poder mantener una convención entre los usuarios y que sea muy práctico el utilizar esta estructura. 

## 6. Pruebas.
Se realizaron 25 prubas de las cuales todas pasaron. Yo diseñé las pruebas de test_todo_contiene_arista(), test_todo_vertice_sin_vecinos(), test_todo_mismas_vecindades_en_ambas_implementaciones(), test_todo_arista_duplicada_no_aumenta_conteo() y creé las pruebas de test_consistencia_vecinos_y_aristas_LEO(), test_vertices_funciona_LEO(). Estas pruebas dejan en evidencia que la implementación está correcta.

## 7. Patrón descubierto.
El patrón que se observa es que uno tiene que guardar la información de relaciones en estructuras que permitan la almacenación de datos sin tener que guardar el orden necesariamente. Por ejemplo, en esta clase utilizamos los diccionarios para llevar el conteo de aristas y usamos matrices para guardar información sobre la existencia de relaciones.


## 8. Pregunta abierta.
Hasta ahora lo más complicado con lo que hemos trabajado es con matrices, las cuales tienen dimensión 2. ¿Habrá implementaciones de relaciones en donde se trabaje con relaciones de dimensión 3 o más, es decir, que trabajen con tensores?
