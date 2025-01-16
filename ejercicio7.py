def suma(num1, num2):
    return num1+num2

def numero():
    num1=float(input("Introduzca un número: "))
    num2=float(input("Introduzca otro número: "))
    resultado=suma(num1, num2)
    print("La suma entre los dos numeros es: ", resultado)

numero()