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
    a = 1
    while a == 1:
        n = input('Digite el numero de la funcion que desea ejecutar:\n'
                  '1=Esto corre la función operaciones\n'
                  '2=Condicional if y else\n'
                  '3=Condicional if y else modificado\n'
                  '4=Ciclo while\n'
                  '5=Ciclo for\n')
        options = {1: operaciones,
                   2: condicionalif,
                   3: condicionalmod,
                   4: ciclowhile,
                   5: ciclofor}
        print("Esto es options: ", type(options))
        options[int(n)]()

        a = input('Desea continuar,Si=1 No=0:\n')
        a = int(a)
    #operaciones()
    #condicionalif()
    #condicionalmod()
    #ciclofor()
    #ciclowhile()

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
    elif n == 8:
        print('El numero que ingreso es igual que 8')
    else:
        print('El numero que ingreso es mayor que 8')

def condicionalmod():
    print('Ud ha ingresado al ejemplo del condicional modificado')
    n = input('Por favor ingrese un numero:\n')
    n = float(n)
    #print('El numero que ingreso es:\n{}'.format(n))
    print('El numero que ingreso es: ', n)

    if n < 8 and n > -8:
        print('El numero que ingreso esta entre 8 y -8')
    elif n == 8:
        print('El numero que ingreso es igual que 8')
    else:
        print('El numero que ingreso o es mayor que 8 o menor igual que -8')

def ciclofor():
    print('Ud ha ingresado al ejemplo del ciclo for')
    n = input('Por favor ingrese un numero:\n')
    n = int(n)

    for x in range(n):
        print('Este es el ciclo : ', x)

    print('Siguiente for:\n')

    for x in range(3, n):
        print('Este es el ciclo : ', x)

    print('Siguiente for:\n')

    for x in "Hola":
        print(x)

def ciclowhile():
    print('Ud ha ingresado al ejemplo del ciclo while')
    n = input('Por favor ingrese un numero:\n')
    n = int(n)

    while (n < 8):
        print('Esto es un ciclo while ')
        n += 1


if __name__ == "__main__":
    gestiona()
