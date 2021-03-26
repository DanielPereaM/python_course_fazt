cart = {
    "nombre": "Libro",
    "cantidad": 25,
    "precio": 50
}

persona = {
    "nombre": "Daniel",
    "apellido": "Perea",
    "edad": 26,
    "aficiones": "criptomonedas",
    "equipo": "América de Cali"
}

# print(dir(persona))

# algunos métodos más utilizados en los diccionarios

# keys(), 
# El método  keys() devuelve un diccionario con las claves especificadas.

# print(persona.keys())

# items(), el método items(),
# devuelve un objeto de vista. El objeto de vista contiene los pares clave-valor del diccionario, como tuplas en una lista.

# print(persona.items())


# clear(), el método clear(), remueve todos los elementos del diccionario.

#persona.clear()


productos = [
    {"nombre":"chocoso", "tipo":"pastel", "precio": 1500},
    {"nombre":"tampico", "tipo": "bebida", "precio": 2000}
    ]
print(productos)