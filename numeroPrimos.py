def get_primos(lista):
    primos = []
    for i in range(len(lista)):
        if multiplos(lista[i])==1:
            primos.append(lista[i])
    if 1 in primos: primos.remove(1)
    return primos
        
def multiplos(n):
    multiplos = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            multiplos += 1
    return multiplos

texto = input("Ingrese lista separada por ',': ")
lista = [int(a) for a in texto.split(",")]
print(get_primos(lista))

"""
Explicación:
La función 'get_primos' itera en los elementos de la lista ingresada y comprueba la 
cantidad de múltiplos que tiene usando la función 'multiplos()', esta función obtiene
la cantidad de productos entre enteros que resulten en el número ingresado, no 
cuenta repeticiones: 2 * 4 y 2 * 8 se cuentan como 1, esto hace que solo sea necesario
calcular hasta la raiz cuadrada del número, a partir de ahí se repetiran las operaciones.
De este modo, todos los números naturales tendrán al menos una operación (al multiplicar 
por 1),si no es primo, tendrá más. Recolectamos todos los número que tengan 1 "múltiplo"
y excluimos el 1 en caso de que esté.
"""