from functools import reduce

lista = [1,2, 3, 4, 5]
suma = sum(lista)
longitud = len(lista)
maximo = max(lista)
minimo = min(lista)
ordenar = sorted(lista)
reversa = list(reversed(lista)) #lista[::-1]
enumerar = list(enumerate(lista))
mapear = list(map(lambda x: x +1, lista))
mapred = reduce(lambda x,y: x+y, lista)
filtrado = list(filter(lambda x: x % 2 ==1, lista))

#print("suma: ", suma)
#print("largo: ", longitud)
#print("maximo:", maximo)
#print("minimo: ", minimo)
#print("ordenar: ", ordenar)
#print("reversa:", reversa)
#print("enumerar: ", enumerar)
#print("mapear:", mapear)
#print("mapred: ", mapred)
# print("filtrado:", filtrado)


#any() all()

#lista = [true, false, true, false]
#any_list = any(lista)
#print("Any:", any_list)

#all_list =all(lista)
#print("all", all_list)

#zip()
#lista1 = [1,2,3]
#lista2 = ["a","b","c"]
#lista_cpx =list(zip(lista1, lista2))
#pint(lista_cpx)

#insert() remove() append() pop() count()
lista = [1,2,3,4,5]
lista.insert(0, 38)
print(lista)

lista.remove(3)
print(lista)

lista.append(333)
print (lista)

lista.pop()
print(lista)

ocurrencias =lista.count(4)
print(ocurrencias)