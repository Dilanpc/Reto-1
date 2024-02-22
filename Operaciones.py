def operar(n1, n2, op):
    if op == "+":
        return n1 + n2
    if op == "-":
        return n1 - n2
    if op == "*":
        return n1 * n2
    if op == "/":
        return n1 / n2
    return "Valor incorrecto"

# x = int(input("Ingrese número 1: "))
# y = int(input("Ingrese número 2: "))
# z = input("Operación (+, -, *, /): ")

# print(x, z, y, "=", operar(x,y,z))

"""
Explicación:
La función 'operar()' recibe 2 números y un caracter, retorna unna operación
entre los dos números según el caracter al activar un 'if'
"""