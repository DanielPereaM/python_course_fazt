#la funcion dir() me muestra todas las acciones que se pueden hacer con la variable
myStr = "hello World Daniel"

#print(dir(myStr))

print(myStr.capitalize())
print(myStr.center(50))
print(myStr.title())
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.replace("hello", "bye").upper())
print(myStr.count(" "))

print(myStr.startswith("hello"))
print(myStr.endswith("World"))

#split(), separar los strings según se asigne el separador
print(myStr.split())

ejemploSplit = "Daniel&Perea&26&Cali"
print(ejemploSplit.split("&"))

ejemploDaniel = "America.Deportivo Cali.Nacional.Millonarios.Pereira.Once Caldas"
print(ejemploDaniel.split("."))

#find(), encuentra el indice(la posicion) de la primera coincidencia 
print(myStr.find("h"))

#len(), longitud de la cadena de texto.
print(len(myStr))
print(myStr.__len__())


