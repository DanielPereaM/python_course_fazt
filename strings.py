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

#index(), indice de la letras o palabras

print(myStr.index("D"))

#isnumeric(), funcion indica si la variable es un numero True o si no es False.
print(myStr.isnumeric())

#isalpha(), funcion indica si la varibale es alfanumerico True o si no es False.

print(myStr.isdecimal())

#[index], imprimir el valor seleccionado segun el index.

print(myStr[4])
print(myStr[-2])


#Concatenation
userName ="Daniel1808"
print("Mi nombre de usuario es: "+userName)
print(f"Mi nombre de usuario es: {userName}")
print("Mi nombre de usuario es: {0}".format(userName))