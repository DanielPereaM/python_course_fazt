#Strings, cadenas de texto
print("Hello World")
print('Hello World')
print("""Hello World""")
print('''Hello World''')
print(type("Hello World"))
print("Daniel"+" "+"Perea")

#Numbers

# Integer
print(30)
print(type(30))

#Float
print(26.5)
print(type(26.5))

#Boolean
True 
False

#List, las listas son mutables quiere decir que sus datos puede cambiar
[10, 20, 30, 55]
["Hello", "Bye", "Adios"]
["Daniel", "Perea", 26, False]
print(type([1, 2]))


#Tuples, las tuplas son inmutables, los datos no pueden cambiar
print(10, 20, 30, 40)
print("Daniel", "Perea", 26, False)
print(type(("America", "Nacional", "Millonarios", "Santa Fe")))

#Dictionaries, diccionarios
print({
    "nombre": "Daniel", 
    "apellido": "Perea", 
    "nickname": "dperea18"
})

print(type({
    "nombre": "Daniel", 
    "apellido": "Perea", 
    "nickname": "dperea18"
}))

#Dato None
print(None)
print(type(None))



str1 = "Hello World"
str2 = 'Hello world'
if (str1 == str2):
    print("Igual")
else:
    print("No son iguales")