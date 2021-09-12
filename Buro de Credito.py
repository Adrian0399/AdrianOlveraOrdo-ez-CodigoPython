
print("Calcular prestamo")

Edad=int(input("Cual es su edad: "))

if Edad >=18:
    print("Usted es mayor de edad, y podra solicitar el prestamos")
    Ingresos = float(input("En pesos cual es la cantidad de dinero que usted GANA mensualmente: "))
    Egresos = float(input("En pesos cual es la cantidad de dinero que usted GASTA mensualmente: "))
    DineroRestante = Ingresos - Egresos
    Prestamo = float(input("Que cantidad desea obetener del prestamos: "))
    Meses = float(input("A cuantos meses desea pagar el prestamo: "))
    CuotaMensual = Prestamo / Meses
    if DineroRestante > CuotaMensual:
        print("El prestamo ha sido Aprobado por el Banco")
        print("La cantidad solicitada es de: ", Prestamo)
        print("El numero de mensualidades son: ", Meses)
        print("Sus cuotas seran de : ", CuotaMensual)
    if DineroRestante < CuotaMensual:
        print("El prestamo ha sido RECHAZADO por el Banco")

else: print("Por ser menor de edad, no podemos ofrecerle un prestamo")
