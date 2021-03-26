#sets conjuntos de datos que no estan ordenado ni indexidos, no permite duplicados
colors = {"rojo","negro","blanco"}
print(type(colors))
print("rojo" in colors)


#methods

# add(), el método add() agrega un elemento al conjunto 
print(colors)
colors.add("violeta")

#remove(), el método remove() elimina el elemento seleccionado
colors.remove("rojo")
print(colors)

# clear(), el método clear(), remueve todos lo elementos del conjunto.

colors.clear()
print(colors)