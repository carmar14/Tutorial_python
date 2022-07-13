
def prueba():
    a = 5
    b = 3.6
    c = a + b
    tipo = type(c)
    # ----------con # comentamos lineas---------------------
    # ----------con '''''' comentamos bloques de codigo------
    print("el contenido de la variable es: ", c)
    print("El tipo de la variable es:", tipo)

def gestiona():
    #operaciones()
    condicionalif()

def operaciones():
    print('Ud ha ingresado al ejemplo de operaciones basicas')
    a = input('Por favor ingrese un numero:\n')
    #print(type(a))
    a = float(a)
    #print(type(a))
    b = input('Por favor ingrese un numero:\n')
    b = float(b)
    c, d = suma(a, b)
    print('El resultado de la suma es: ', c)
    print('El resultado de la resta es: ', d)

def suma(c, d):
    s = c + d
    r = c - d
    return s, r

def condicionalif():
    print('Ud ha ingresado al ejemplo del condicional')
    n = input('Por favor ingrese un numero:\n')
    n = int(n)
    #print('El numero que ingreso es:\n{}'.format(n))
    print('El numero que ingreso es: ', n)

    if n < 8:
        print('El numero que ingreso es menor que 8')
    else:
        print('El numero que ingreso es mayor o igual que 8')


if __name__ == "__main__":
    gestiona()
