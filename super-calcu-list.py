#Calculadora
#opciones 
#1 - sumar todos los elementos de una lista
#2 - encontrar el maximo
#3 - encontrar el minimo 
#4 - filtrar por pares
#5 - filtrar por impares

### ingrese los valores de la lista por pantalla, y ademas la lista pueda tener cualquier tamaño 
#input()

lista = []
suma = 0
maxino = 0 
minimo = 0
n_pares =[]
n_impares =[]
continuo = "si"

condicion ="si"
while condicion == "si": 
    lista.append(int(input("ingrese los valores que desee agregar a la lista: "))) 
    condicion =input("desea seguir cargando valores: si/no ")
print("La lista ingresada es: ", lista)

print(f'''
1 - Sumar todos los elementos de la lista
2 - Encontrar el máximo
3 - Encontrar el mínimo
4 - Filtrar por elementos pares
5 - Filtrar por elementos impares''')


while continuo == "si":
    opcion = (int(input("Ingrese una opción: ")))
    if opcion == 1:
        suma =sum(lista)
        print("la suma de los elementos es: ", suma)
    elif opcion == 2:
        maximo =max(lista)
        print("El maximo es: ", maximo)
    elif opcion == 3:
        minimo =min (lista)
        print("El minimo es:", minimo)
    elif opcion == 4:
        n_pares = list(filter(lambda x: x % 2 == 0, lista))
        print(n_pares)
    elif opcion == 5:
        n_impares = list(filter(lambda x : x % 2 ==1, lista))
        print("Los impares son: ", n_impares)
    continuo = input("desea continuar: si/no ")
    




