
print("Calcular determinante de una matriz 2x2")

print ("Tomando en cuenta el valor de 'X' y 'Y' en la matriz 2x2")
M1 = input("Ingresar el valor de la posicion 1,1 en la matriz: ")
M2 = input("Ingresar el valor de la posicion 1,2 en la matriz: ")
M3 = input("Ingresar el valor de la posicion 2,1 en la matriz: ")
M4 = input("Ingresar el valor de la posicion 2,2 en la matriz: ")

M1 = float (M1)
M2 = float (M2)
M3 = float (M3)
M4 = float (M4)

Determinante = ((M1 * M4) - (M2 * M3))

print("\n La determinante de la matriz es : ", Determinante)



