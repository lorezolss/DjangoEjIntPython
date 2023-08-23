#Lee un valor entero y lo devuelve mientras sea correcto, sino itera hasta que lo sea
def get_int_iterativo():
    ok = False
    while not ok:
        numero = input('Ingrese un numero entero positivo: ')
        try:
            nro = int(numero)
        except ValueError:
            print ('No ingresó un número válido')
        else:
            ok = True
    return nro

def get_int_recursivo():
    numero = input('Ingrese un número entero positivo: ')
    try:
        nro = int(numero)
    except ValueError:
        print ('No ingresó un número válido')
        return get_int_recursivo()
    else:
        return nro
    