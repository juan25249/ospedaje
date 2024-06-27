 #1.Impreme los numeros del 1 al 5 utilizando un bucle for.
mi_lista = [1,2,3,4,5,6]

for elemento in mi_lista:
    if elemento == 6:
        break
    print(elemento)

#2.Imprime los cuadrados de los numeros del 1 al 4
mi_lista = [1,2,3,4]

nueva_lista = [elemento ** 2 for elemento in mi_lista]
print(nueva_lista)

#3.Suma los numeros pares del 1 al 10
mi_lista = [1,2,3,4,5,6,7,8,9,10]
suma_par = 0
for elemento in mi_lista:
    if elemento % 2 == 0:
        suma_par += elemento
print(suma_par)

#4.imprime los elmentos de la lista [10,20,30,40,50].
mi_lista = [10,20,30,40,50]
print(mi_lista)

#5.imprime los caracteres de la cadena de texto "DevZeros"
mi_texto = "DevZeros"

for caracter in mi_texto:
    print(caracter)

#while
#1. solicita al usuario que ingrese un numero positivo
#luego, imprime la tabla


int(input('ingrese numero positivo: '))
contador = 1
while contador < 11:
    print(contador * 5)
    contador += 1

#2.implementa un juego de adivinanza
import random

numero = random.randint(1, 100)
nTeclado = int(input("dijite un numero del 1 al 100:"))

while(numero != nTeclado):
    if nTeclado > numero:
      print("el numero digitado es mayor que el esperado")
    elif numero > nTeclado:
      print("el numero digitado es menor que el esperado")
    nTeclado = int(input("dijite un numero: del 1 al 100:"))
print("has ganado")