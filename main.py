#Funcion para ingresar paises
def Paises():
    noDePaises = int(input('Escribe el numero de paises a agregar: '))
    paises = []
    for i in range (0, noDePaises):
        paises.append(input('Introduce el nombre del pais: '))

    ordenada = sorted(paises)
    print(ordenada)

listPaises = Paises()

