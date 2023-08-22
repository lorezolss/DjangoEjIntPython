# Arma un diccionario con las palabras y su frecuencia en una frase dada
def arma_diccionario(lista):
    diccionario = {}
    for palabra in lista:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    for palabra, frecuencia in diccionario.items():
        print (f'{palabra} = {frecuencia}')
    return diccionario

def mayor_frecuencia (dic):
    pass

cadena = input("Ingrese una frase: ")
lista = cadena.split(' ')
dic = arma_diccionario(lista)
palabra, frecuencia = mayor_frecuencia(dic)
print(f'En la frase ingresada, la palabra más repetida fue {palabra} con {frecuencia} veces.')