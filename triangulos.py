import math #comenzamos con importar la libreria math para algunos calculos en la area de las figuras geometricas

#aqui se puede ver una serie de funciones que calculan su respectiva figura geometrica
def cuadrado():  #esta funcion es para el calculo del area de un cuadrado
    L=float(input("ingrese los valores del cuadrado: "))   #esta linea de comando es para que se pueda ingresar los valores del cuadrado
    area_cuadrado=(L**2)   #el area de esta figura es el tamaño de los lados del cuadrado elevado a 2
    print("el area del cuadrado es: ",area_cuadrado)  #aqui se imprime en la consola de python el resultado del area

def triangulo(): #calculo del triangulo
    A=float(input("ingrese la altura del triangulo: ")) #A es la altura del triangulo
    B=float(input("ingrese la base del triangulo: ")) #B es la base del triangulo
    area_triangulo=(A*B)/2  #es altura por base, todo esto entre 2 para obtener el area
    print("el area del triangulo es: ",area_triangulo) #imprime el resultado

def rectangulo(): #calculo del rectangulo
    a=float(input("ingrese la altura del rectangulo: ")) #mismo proceso que el triangulo solo que son la division
    b=float(input("ingrese la base del rectangulo: "))
    area_rectangulo=(a*b)
    print("el area del rectangulo es: ",area_rectangulo) #imprime el resultado

def pentagono(): #calculo del pentagono
    l=float(input("ingrese el tamaño de los lados: "))  #aqui se ingresa el tamaño de los lados del pentagono
    P=float(l*5) #P en este caso es el perimetro del pentagono, uno de los valores necesarios para calcular si area
    Apotema=float(input("ingrese el apotema del pentagono: ")) #el apotema del pentagono es otro valor necesario para calcular su area
    area_pentagono=(P*Apotema)/2 #como se puede apreciar aqui lo cual es el apotema por el perimetro, todo esto entre dos
    print("el area del pentagono es: ",area_pentagono) #imprime el resultado

def hexagono(): #calculo del hexagono
    lados_hexagono=float(input("ingrese el tamaño de los lados: ")) #mismo proceso que el pentagono solo que en este caso el perimetro se calcula con 6 lados envez de 5
    p=float(lados_hexagono*6)
    apotema=float(input("ingrese el apotema del hexagono: "))
    area_hexagono=(p*apotema)/2
    print("el area del hexagono es: ",area_hexagono) #imprime el resultado

def circulo(): #calculo del circulo
    R=float(input("ingrese el radio: ")) #valores de radio del circulo
    area_circulo=math.pi*(R**2) #aqui se importe de la libreria math (math.pi) el cual es el valor de pi
    print("el area del circulo es: ",area_circulo) #imprime el resultado

def trapecio(): #calculo del trapecio
    Base_mayor=float(input("ingrese la base mayor:"))  #el calculo de area de una trapecio es algo diferente a las otras figuras geometricas, la base mayor es la parte inferior del trapecio
    base_menor=float(input("ingrese la base menor: "))  #la base menor es la parte superior del trapecio
    Altura_trapecio=float(input("ingrese la altura: "))  #altura del trapecio 
    area_trapecio=((Base_mayor+base_menor)*Altura_trapecio)/2 
    print("el area del trapecio es: ",area_trapecio) #imprime salida

def paralelogramo(): #calculo del paralelogramo
    Base=float(input("ingrese la base: ")) #ingrese la base del paralelogramo
    Altura_paralelogramo=float(input("ingrese la altura: ")) #ingrese la altura del paralelogramo
    area_paralelogramo=Base*Altura_paralelogramo
    print("el area del parlelogramo es: ", area_paralelogramo) #imprime la salida

#de aqui en adelante son las funciones para obtener un menu operacional en la consola de python
def menu(): #comenzamos definiendo la funcion del menu
    print("\n".join([       #todo esto es el texto que aparecera en el menu
        "\n..........",      #esto es decorativo
        "Seleccione una opcion: ",
        "1 - cuadrado",
        "2 - triangulo",
        "3 - rectangulo",
        "4 - pentagono",
        "5 - hexagono",
        "6 - circulo",
        "7 - trapecio",
        "8 - paralelogramo",
        "\n0 -salir"
    ]))

while True:  #se comienza con un while True para que la funcion anterior funcione
    menu()
    option=input("ingrese el numero de la figura a calcular: ")  #esta entrada de texto es lo que mostrara para asi colocar un numero de la opcion a querer realizar
    functionlist={   #el functonlist es la lista de funciones que se conectan a las funciones del calculo de las figuras geometricas
        "1":"cuadrado()",  #como se puede ver que ingresando el numero 1 me llama a la funcion cuadrado
        "2":"triangulo()",
        "3":"rectangulo()",
        "4":"pentagono()",
        "5":"hexagono()",
        "6":"circulo()",
        "7":"trapecio()",
        "8":"paralelogramo()"
    }
    if option in functionlist.keys():  #este if es para obtener un cierre con el numero 0
        eval(functionlist[option])
    elif option=="0":  #aqui es donde se aplica el cierre del menu
        break
else:
    print("la opccion seleccionada no es correcta: ")
