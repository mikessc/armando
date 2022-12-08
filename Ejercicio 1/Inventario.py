#Armando Carranza

def menu ():
    print('1. Ingresar camiseta')
    print('2. Ver inventario')
    opcion = int(input('Seleccione una opcion: '))
    procesarOpcion(opcion)

def procesarOpcion(opcion):
    if opcion == 1:
        ingresarCamiseta()
    elif opcion == 2:
        imprimir()
    else:
        print('Seleccione una opcion válida')
        menu()

def ingresarCamiseta ():
    camiseta = []
    
    codigo = input('Codigo: ')
    detalle = input('Detalle: ')
    talla = input('Talla: ')
    cantidad = input('Cantidad: ')
    precio = input('Precio Unitario: ')

    camiseta.append('Codigo: ' + codigo)
    camiseta.append(' Detalle: ' + detalle)
    camiseta.append(' Talla: ' + talla)
    camiseta.append(' Cantidad: ' + cantidad)
    camiseta.append(' Precio: ' + precio)

    guardarInfo(camiseta)
    menu()

def guardarInfo (camiseta):
    file = open('inventario.txt', 'a')
    file.write(" ".join(camiseta) + "\n")
    file.close()
    menu()

def imprimir ():
    file = open('inventario.txt', 'r')
    inventario = file.read()
    print(inventario)
    file.close()

def main ():
    print('**********************************************')
    print('*** Inventario de Camisetas conmemorativas ***')
    print('**********************************************')
    menu()

main()
