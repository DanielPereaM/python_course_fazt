tupla = (1, 2, 3, 4, 5,5,6,6,6,7,7,7,8,9,10,11)
# print(tupla)

locations = {
    (35.12312, 39.0000): "Tokio",
    (40.7285711,-74.0373074): "New York"
}
# tuple() constructor 
#También es posible usar el constructor tuple () para hacer una tupla.

#y = tuple((1, 2, 3))
#print(y)

# count(), El método count(),
# devuelve el número de veces que aparece un valor especificado en la tupla.
print(tupla.count(7))

# index(), el método index() encuentra la primera aparición del valor especificado.

print(tupla.index(7))