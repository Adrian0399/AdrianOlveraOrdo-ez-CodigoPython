
print("Calcular Resistencia Total de 2 transistores en parelelo")
R1 = input ("Ingresar el valor de la Resistencia 1: ")
R2 = input ("Ingresar el valor de la Resistencia 2: ")
R1 = int (R1)
R2 = int (R2)

RT = (( (R1 * R2) / (R1 + R2) ))

print("\n La resistencia total es: ", RT)
