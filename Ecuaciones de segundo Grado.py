
import math

print("Tomando la formula general")
A=int(input(" Introduce el valor de A: "))
B=int(input(" Introduce el valor de B: "))
C=int(input(" Introduce el valor de C: "))

#Se calcula el discriminante (El valor dentro de la Raiz Cruadra)

Raiz=((B * B) - (4 * A * C))

#Calculamos la Raiz y comprobamos que tenga solucion

if Raiz<0:
    print("No hay solucion Real, ya que la Raiz es igual a 0 o es negativa")
else:
    Resultado1 = (-B + math.sqrt(Raiz)) / (2 * A)
    Resultado2 = (-B - math.sqrt(Raiz)) / (2 * A)

    print("*** Soluciones ***")
    print("Solucion X1: ", Resultado1)
    print("Solucion X2: ", Resultado2)
