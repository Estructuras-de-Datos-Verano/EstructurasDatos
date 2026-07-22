def posiciones_menor_cercano(numeros: list[int]) -> list[int]:
    
    resultado = []
    pila = []  
    
    for i in range(len(numeros)):
        
        
        while pila and numeros[pila[-1]] >= numeros[i]:
            pila.pop()
            
        if not pila:
            resultado.append(0)
        else:
            
            resultado.append(pila[-1] + 1)
            
        pila.append(i)
        
    return resultado
if __name__ == "__main__":
    ejemplo_numeros = [2, 5, 1, 4, 8, 3, 2, 5]
    posiciones = posiciones_menor_cercano(ejemplo_numeros)
    
    print(f"Números de entrada: {ejemplo_numeros}")
    print(f"Posiciones menores: {posiciones}")


