def area(base, altura, precio):
    resul=(base*altura)/2
    coste=resul*precio
    return  resul, coste

def datos():
    base=float(input("Introduzca la base de un triángulo en metros: "))
    altura=float(input("Introduzca la altura de un triángulo en metros: "))
    precio=float(input("Introduzca el precio por metro cuadrado del triángulo: "))
    resul, coste=area(base, altura, precio)
    print ("El área del triángulo es: ", resul, "m^2 ,y el precio total sería: ", coste," €")

datos()