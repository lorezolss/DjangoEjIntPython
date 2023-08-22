# Arma un diccionario con las palabras y su frecuencia en una frase dada
diccionario = {}
cadena = input("Ingrese una frase: ")
lista = cadena.split(' ')
for palabra in lista:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1
for palabra, frecuencia in diccionario.items():
    print (f'{palabra} = {frecuencia}')