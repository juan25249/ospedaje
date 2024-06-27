#ejercicio de calcular el indice de masa corporal (imc)

import math


peso = float(input("Ingrese su peso en Kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))

IMC = round(peso/math.pow(estatura,2),1)

print("Su IMC es de " + str(IMC))




#ejercicio de convertir de grado celsios a grado fahrenheit

celsius = int(input('Ingrese la temperatura en grados Celsius: '))
fahrenheit = 9.0/5.0 * celsius +32
print('{} grados Celsius son {} grados Fahrenheit'.format(fahrenheit, celsius))
# ejercicio de calculadora basica

n1 = float(input("Introduce tu primer número: "))
n2 = float(input("Introduce tu segundo número: "))

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?

    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) dividir los dos numeros 

    """)
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de", n1, "+", n2, "es igual a", n1 + n2)
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de", n1, "-", n2, "es igual a", n1 - n2)
    elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de", n1, "*", n2, "es igual a", n1 * n2)
    elif opcion == 4:
        print(" ")
        print("RESULTADO: El producto de", n1, "/", n2, "es igual a", n1 / n2)
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")



