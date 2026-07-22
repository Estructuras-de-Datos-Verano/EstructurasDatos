# Arturo Prudencio Bonilla - Discusion

## 1. Problema y primera idea.
    El problema nos pide un algoritmo capaz de devolver una lista con las posiciones de los numeros mas cercanos desde la izquierda y mas pequños para cada numero del arreglo
## 2. Por qué la solución ingenua repite trabajo.
    Porque necesita recorrer todas las posiciones a¿hasta agotar el array para cada elemento 
## 3. Información útil e información descartable.
    Necesitamos optimizar el problema por lo que es util guardar aquellos numeros que tenemos certeza que nos pueden servir para comparar depsues y debemos desechar aquellos que no nos irven
## 4. Elección de esructura.
    Elegimos una pila porque nos ayuda y es natural para guardar a nuestros candidatos, ya que siempre compararemos el ultimo que entro primero, este comportamiento es propio de la pila 
## 5. Variante: Nearest Greater Values.
    A diferencia del problema que resolvimos, este problema buscaria los valores mas grandes (con el mismo comportamiento); precisamente porque es el mismo comportamiento, yo pienso que debe ser algo analogo a la implementacion que ya hicimos 
## 6. Contraejemplo: Maximum Subarray Sum.
    No siempre vamos a poder usar la pila para todos los problemas y creo que este problema nos hace ver esto, puesto a que no creo que sea la mejor structura para lamcenar nuestros datos, porque es cierto que este problema nos demanda mas cosas que comparar 
## 7. Sliding Window.
    En este problema 
## 8. Invariante.   
    Hay cosas que no cambian, por ejemplo en nuestro problema, hay cosas invariantes en la pila y estas son las mas utiles (al menos para este problema) pues son los candidatos que no fueron sacados por un nuevo numero 
## 9. Pruebas.
    En la pruebas hicimos multiples testeos, sobre todo nos apoyamos ene le ejemplo ofocial y probamos casos extremos, como por ejemplo que pasa si solo hay un eleemtno o si un mismo numero se repite multiples veces; en general hicimos pruebas que corroboranque nuestro codigo esta bien blindado y que en efecto se comorta como queremos y que el signo usado para comparar es el correcto
## 10. Complejidad.
Sobre la complejida podmeos decir que de no haberlo optimizado como lo hicimos, necesitariamos un doble ciclo por lo que esto se acercaria $O(n^{2})$

Como lo hicimso buscando guardar candidatos e infromacion util para proximos numeros, nos alejamos de $O(n^{2})$, inclsuo podemos pensar que se acerca a $O(n)$
## 11. Cómo descubrimos el algoritmo.
    Primero tuve que entender que si nos servia y que no, al entender eso pude pensar y reflexionar sobre que estructura usar y guidaod por el notebook conclui qu en efecto la pila es la mejor opccion, asi, empece a pensar en un pseudocodigo y despues de codnfundirme con el del notebook por fin entendi que debeiamos hacer, bverificar cada dato y hacer un clico mientras ciertas circusntancias se cumplieran y explotar al maximo nuestra capacidad de guardar datos utiles.
## 12. Pregunta abierta.
    ¿Que estrcutura parece mejor para el problema de Sliding Window?