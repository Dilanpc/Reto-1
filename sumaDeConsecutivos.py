def mayor_suma(lista):
    sumas = []
    n = len(lista)
    for i in range(n-1):
        sumas.append(lista[i] + lista[i+1])
    return max(sumas)


# texto = input("Ingrese lista separada por ',': ")
# lista = [int(a) for a in texto.split(",")]
# print("La mayor suma de números consecutivos es", mayor_suma(lista))
