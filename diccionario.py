#creamos lista en blanco
listakevin = []


#crear diccionario, nombre,edad,grado,ciudad,colegio,telefono

my_diccionario1 = {'nombre':'carlos','edad':17,'grado':'undecimo','ciudad':'cartagena',
                   'colagio':'san pepito perez','telefono':3427360945 }

my_diccionario2 = {'nombre':'pedro','edad':18,'grado':'undecimo','ciudad':'cartagena',
                   'colagio':'san pepito perez','telefono':3427860947 }

my_diccionario3 = {'nombre':'kevin','edad':16,'grado':'undecimo','ciudad':'cartagena',
                   'colagio':'san pepito perez','telefono':3427860945 }

my_diccionario4 = {'nombre':'juan','edad':19,'grado':'undecimo','ciudad':'cartagena',
                   'colagio':'san pepito perez','telefono':3427960945 }

my_diccionario5 = {'nombre':'camilo','edad':17,'grado':'undecimo','ciudad':'cartagena',
                   'colagio':'san pepito perez','telefono':3427840945 }

my_diccionario6 = {'nombre':'andrea','edad':17,'grado':'undecimo','ciudad':'cartagena',
                   'colagio':'san pepito perez','telefono':3426870945 }

my_diccionario7 = {'nombre':'sebastian','edad':17,'grado':'undecimo','ciudad':'cartagena',
                   'colagio':'san pepito perez','telefono':3527860645 }


my_diccionario8 = {'nombre':'kevin','edad':15,'grado':'undecimo','ciudad':'cartagena',
                   'colagio':'san pepito perez','telefono':3627860945 }

my_diccionario9 = {'nombre':'andres','edad':17,'grado':'undecimo','ciudad':'cartagena',
                   'colagio':'san pepito perez','telefono':5427860945 }

my_diccionario10 = {'nombre':'andres felipe','edad':16,'grado':'undecimo','ciudad':'cartagena',
                   'colagio':'san pepito perez','telefono':3527860945 }

listakevin.append(my_diccionario1)
listakevin.append(my_diccionario2)
listakevin.append(my_diccionario3)
listakevin.append(my_diccionario4)
listakevin.append(my_diccionario5)
listakevin.append(my_diccionario6)
listakevin.append(my_diccionario7)
listakevin.append(my_diccionario8)
listakevin.append(my_diccionario9)
listakevin.append(my_diccionario10)

listakevin.remove(my_diccionario5)
listakevin.remove(my_diccionario7)

listakevin[3]['nombre'] ='profesor'

#range(stop9
rango1 = range(5)
print(rango1)

#range(start, stop)
rango2 = range(2,7)
print(rango2)

#range(start, stop , step)
rango3 = range(1,10,2)
print(rango3)

#covertir a lista de numeros
lista_numeros = list(range(5))
print(lista_numeros)











#for con if
mi_lista = [1,2,3,4,5]

for elemento in mi_lista:
    if elemento % 2 == 0:
        print(f"numero par: {elemento}")
    else:
        print(f"numero impar: {elemento}")

#for con string
mensaje = "hola, mundo"

for caracter in mensaje:
    print(caracter)

#for con break
mi_lista = [1,2,3,4,5]

for elemento in mi_lista:
    if elemento == 3:
        break
    print(elemento)

#for con continue
mi_lista = [1,2,3,4,5]

for elemento in mi_lista:
    if elemento == 3:
        continue
    print(elemento)

#for con comprehesion
mi_lista = [1,2,3,4,5]

nueva_lista = [elemento * 2 for elemento in mi_lista]
print(nueva_lista)

#for con zip(iterar dos listas a la vez)
nombres = ["alice", "bob","charlie"]
edades = [25,30,22]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

#while con break
contador = 0

while True:
    print(contador)
    contador += 1
    if contador >= 5:
        break


#while con continue
contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print(contador)


 #1
mi_lista = [1,2,3,4,5]

for elemento in mi_lista:
    if elemento == 3:
        break
    print(elemento)































