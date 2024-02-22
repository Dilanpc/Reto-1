def mismosCaracteres(lista):
    n = len(lista)
    listCaracteres = []
    for i in range(n):
        listCaracteres.append(caracteres(lista[i])) #obtener los caracteres de cada palabra

    grupos = []
    visited = set()
    for i in range(n):#hacer grupos con las palabras que tienen los mismos caracteres
        if not (i in visited):
            visited.add(i)
            grupos.append([i])
            for j in range(n):
                if i == j:
                    continue
                if compara_listas(listCaracteres[i], listCaracteres[j]):
                    visited.add(j)
                    grupos[-1].append(j)
    
    #Elegir el grupo más grande
    mayor = grupos[0]
    for i in range(len(grupos)):
        if len(grupos[i]) > len(mayor):
            mayor = grupos[i]

    #Cambiar los índices por su contenido:
    palabras = []
    for i in range(len(mayor)):
        palabras.append(lista[mayor[i]])
    return palabras

    


def caracteres(word):
    caracteres = []
    for i in word.lower():
        if 96 < ord(i) < 123: #Verificar que sea letra
            caracteres.append(i)
    return caracteres

def compara_listas(first, second) -> bool: #compara listas sin importar el orden de sus elementos
    if len(first) != len(second): return False

    visited = set()
    for i in range(len(first)):
        found = False
        for j in range(len(first)):
            if j in visited or found: continue

            if first[i] == second[j]:
                visited.add(j)
                found = True
    return len(visited) == len(first)

# palabras = input("Ingrese plabras separadas por ',': ").split(",")

# print(mismosCaracteres(palabras))

# lista1 = [1,2,3,4,5,6,7,8,9]
# lista2 = [2,8,1,9,3,7,6,5,5]

# print(compara_listas(lista1, lista2))

"""
La función caracteres() retorna los caracteres de una palabra, en esta, primero
se convierten todas las letras en minúscula y usando código ASCII se verifica
si es letra. 
En la función mismoCaracteres() se crea otra lista para guardar los caracteres de 
cada palabra usando la función caracteres(), luego se buscan los conjuntos de caracteres
que sean iguales usando comparar_listas() y se guardan sus indices, como pueden haber varios 
caraceres que sean iguales por grupos como [amor, roma, perro, pero] donde se obtiene un 
grupo de [amor, roma] y [perro, pero], se crea una lista "grupos" que contendra los 
diversos grupos que se formen, luego se elige el grupo más grande y se convierten los 
índices a las palabras que representan y se retornan.
"""