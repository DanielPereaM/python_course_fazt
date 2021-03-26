demo_list = [26, "Daniel", 1.77, "Masculino", True, [5.0, 3.6, 4.5]]
colors = ["rojo", "verde", "amarillo", "azul"]


""" print(number_list)
print(type(number_list))
 """

""" r = list(range(1,11))
print(r)
print(dir(colors)) """

# list() constructor
# También es posible utilizar el constructor list () al crear una nueva lista.

number_list = list((1, 2, 3, 4))

#append(). agrega su argumento como un solo elemento al final de  lista o arreglo, 
#solo permite agregar un solo elemento, la lista aumentara en un elemento

#colors.append(["violeta","marron","blanco"])

#extend(). el método extend(),
# itera sobre su argumento agregando cada elemento a la lista, 
#la longitud de la lista aumentará en la cantidad de elementos que haya en el argumento iterable 

# colors.extend(["violeta","blanco"])

# insert(), el metodo insert(),
# inserta un elemento en la lista en el indice especificado.

# colors.insert(1, "gris")

# pop(), el método pop() 
# elimina el ultimo valor de la lista o el valor de indice que se indique

#colors.pop(0)

# sort(), el método sort() ordena la lista de forma ascendete por defecto. 
# sintaxis list.sort(reverse=True|False, key=myFunc)

#colors.sort(reverse = False)

# index(), el método index() 
# devuelve la posición en la primera aparición del valor especificado

# print(colors.index("rojo"))

# count(). el método count(),
#devuelve el número de elementos con el valor especificado.

print(colors.count("rojo"))


