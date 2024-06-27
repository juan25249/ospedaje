"""ejercicio 1 obtener un numero por teclado y vereficar si es divisible por dos y por tres"""
numero = int(input("digite un numero:"))
if numero != 0 and numero % 2 == 0 and numero % 3 == 0:
    print(f"el numero{numero} es divisible entre 2 y 3")
else:
    print(f"el numero{numero} es divisible por 2 y 3")

"""ejercicio 2 obtener tres numero por teclado y verificar cual es el mayor de los tres"""
num1 = int(input("ingrese el numero 1"))
num2 = int(input("ingrese el numero 2"))
num3 = int(input("ingrese el numero 3"))
if num1 >= num2 and num1 >= num3:
    print("el numero",num1,"es el mayor de los tres")
if num2 >= num1 and num2 >= num3:
    print("el numero", num2, "es el mayor de los tres")
else:
    print("el numero",num3," es el mayor de los tres")

"""ejercicio 3 obtener un numero por teclado y verificar si es par o impar"""
numero = int(input("digite el numero"))

if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")

"""ejercicio 4 pepito perez fue a la tienda a comprar un  kilo de carne donde su costo o valor es de 25000 el tendero le cometo que si compraba dos kilos o mas iba a tenr el 35% de descuentos obtener el valor a pagar si pepito compro 2.5 kilos de carne"""

valor_carne = 25000
cantidad_carne = 2.5 #kg

total_antes = valor_carne * cantidad_carne
total_despues = 0
if (cantidad_carne >=2):
    total_despues = total_antes - (total_antes * 0.35)
print("el precio total a pagar de pepito"
      f" por los 2.5 kg de carne es: ${total_despues}")

print("el precio total a pagar de pepito")


"""ejercicio 5 si andres fue a comprar 5 huevos a la tienda y en la tienda solo habian  tres huevos
entonces andres andres le toca A ir a otra tienda B llevar los tres huevos a la casa C comprar otra cosas determinar la respuesta de la mama para cada punto"""

cantidad_de_huevo = 5
if cantidad_de_huevo <=3 :
    print("a:ir a otra tienda")
    print("b: llevar los tres huevos")
    print("c: llevar otra cosa")
    opcion = input("que opcion escojio andres?:").lower()
if opcion == "a":
    print("y los que faltan?")
elif  opcion == "b":
    print("porque te demoras en la tienda? de seguro estabas jugando")
else:
    print("yo solo te pedi huevos")

