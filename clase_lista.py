#crear lista
lista_vacia  = []
lista_numeros = [1,2,3,4,5]
lista_strings = ['a','b','c']
lista_mixta = [1,'dos',3.0,True]
print(lista_strings)


#acceso a elementos
lista = ['a','b','c','d']
primar_elemento = lista[0]
segundo_elemento = lista[1]
print(segundo_elemento)

#modificando elementos
lista = ['a','b','c','d']
lista[2] = 'Z'
print(lista)


#palindromo
texto = input("digite un texto:").lower().replace("","")


if texto == texto[::-1]:
    print("es una palabra palindroma")
else:
    print("NO es una palabra palindroma")

#cortar lista
lista = [1,2,3,4,5]
sub_lista = lista[1:4]
print(sub_lista)

#unir listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista_concatenada = lista1 + lista2
print(lista_concatenada)

#verificacion de elemento en lista
lista = ['a','b','c']
existe_a = 'a' in lista
existe_x = 'x' in lista
print(existe_x)

#ordenar lista
lista_numeros = [3,1,4,1,5,9,2,6,5,3]
lista_numeros.sort()
print(lista_numeros)


#agregar elementos
lista = ['a','b','c']
lista.append('d')
lista.insert(1,'x')
print(lista.append('d'))

#eliminar elementos
lista = ['a','b','c','d']
elemento_eliminado = lista.pop(2)
lista.remove('b')
print(elemento_eliminado)

#lomgitud de lista
lista = [1,2,3,4,5]
longitud = len(lista)
print(longitud)

#ejercicio imposible
lista_precio = [40000,8000,4000,25000,6000]
resultado_total = sum(lista_precio)
print(resultado_total)
elemento_eliminado = lista_precio.pop(2)
print(elemento_eliminado)
resultado_total = sum(lista_precio)
print(resultado_total)


#operaraciones de conjuntos (union,intersection;diferencia
conjunto1 = {1,2,3,4,5}
print(conjunto1)
conjunto2 = {3,4,5,6,7}
print(conjunto2)
union = conjunto1.union(conjunto2)
print(union)
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)
diferencia = conjunto1.difference(conjunto2)
print(diferencia)

#longitud
conjunto = {1,2,3,4,5}
print(conjunto)
longitud = len(conjunto)
print(longitud)

#inmutabilidad como las tuplas
conjunto_inmutable = frozenset([1,2,3,4])
print(conjunto_inmutable)

#modificar elemento
mi_diccionario = {'nombre':'juan','edad':25,'ciudada':'ejemplo'}
mi_diccionario ['edad'] = 26
mi_diccionario['ocupacion'] = 'estudiante'


#eliminar elementos
del mi_diccionario['edad']
print(mi_diccionario)

#longitud
longitud = len(mi_diccionario)















