#entrada
texto = input("ingrese el texto")
numero = int(input("ingrese el numero"))

#salida
print("hola mundo")
print(f"texto con variable{texto}")

numero = 1

if(numero == 1):
    print("primer camino")
    # action
elif(numero == 0):
    print("segundo camino")
    #action
else:
    print("tercer camino")
    #action

#entrada
numero = int(input("solictud de numero"))
if numero % 2 == 0:
     print(f"el numero {numero}"
           f" es divisible por 2")
elif numero % 3 == 0:
    print(f"el numero {numero}"
          f" es divisible por 3")
else:
    print("no es divisible ni por 2 ni por 3")



cantidad_libros = int(input("ingrese la cantidad de libros que desea comprar."))
precio_unitario = float(input("ingrse el precio unitario de cada libro: "))
nivel_academico = input("ingrese su nivel academico ('primaria','secundaria','universidad'): ").lower()

# calcular costo total andtes de descuentos
costo_total = cantidad_libros * precio_unitario

# aplicar descuento del 5% si la cantidad de libro es 3 o mas
if cantidad_libros >= 3:
    costo_total*= 0.95

# aplicar descuento adicional del 10% si el nivel acade,ico es "universidad"
if nivel_academico == "universidad":
    costo_total *= 0.9

# aplicar descuento adicional del 7% si el costo es $50 o mas
if costo_total >= 50:
    costo_total *= 0.93

# imprimir recibo detallado
print("\nrecibo detallado:")
print(f"cantidad de libro:{cantidad_libros}")
print(f"precio unitario: ${precio_unitario:.2f}")
print(f"costo total antes de descuentos: ${cantidad_libros * precio_unitario:.2f}")
print(f"costo total despues de descuentos: ${costo_total:.2f}")


