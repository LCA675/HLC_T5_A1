num1=int(input("Introduzca un número: "))
num2=int(input("Introduzca otro número: "))
if num1>num2:
    print("El primer número es mayor al segundo; ", num1 ," > ", num2)
elif num1<num2:
    print("El segundo número es mayor al primero; ", num2 ," > ", num1)
else:
    print("Los números introducidos son iguales; ", num1 ," = ", num2)
