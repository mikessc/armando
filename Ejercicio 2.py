def imprimir (tablas):
    print('**********************************************')
    print('*** Tablas del 1 al 12 ***')
    print('**********************************************\n')
    print(tablas)

def multiplicar (x, y):
    return x * y

def main ():
    tablas = []
    for A in range(1,13):
        for B in range(1,11):
            mult = str(A) + "x" + str(B) + "=" + str(multiplicar(A,B))
            tablas.append(mult)
    imprimir(tablas)
            
main()
