import random #Importar funcion que tira un valor aleatorio
import funciones


def modofacil():

    x=random.randint(1, 20) #Variable con la funcion random, que tira un valor aleatorio de tipo entero
    cont=0 #contador para el for
    print("Bienvenido a adivina el número fácil. Dependiendo de la cantidad de jugadores que hayan en la consola en esta ocasión\nel juego se repetirá, recuerde que si pierde uno, al haber más de un jugador, no podrán jugar en caso de que uno tenga\n menos créditos de los que pide el juego.\n")

    for n in range(12):    
        num=input("Ingresar un número, e intentar acertar el número aleatorio o ingresar x para salir: \n")
        print("")

        while not num.isnumeric() or int(num)>20:
            if num == "X".lower(): #Si el valor es el string "x", rompe la excepcion.
                break
            num=input("Ingresar variables numéricas, e intentar acertar el número aleatorio: \n")
            print("")

        if num == "X".lower(): #Si el valor es el string "x", rompe el for.
            break

        if int(num)==x: #Si num es de tipo entero y su valor es igual que el de x, ganas la partida
            print (f"Usted acertó, el número era: {x}. \nUsted ha ganado!\n")
            nom=input("Ingresar el nombre del jugador: ")

            for item in funciones.jugador:
                if (nom == item['nombre']):
                    item["puntaje"]=item["puntaje"]+25

            break
        elif int(num)>x: #Si no seguis jugando, con menos intentos. En este caso muestra si el valor ingresado es mayor o menor
            cont=cont+1
            print ("Valor incorrecto, el número ingresado es mayor al número a adivinar. \nLe quedan",10-cont,"Oportunidades.\n")     
        else:
            cont=cont+1
            print ("Valor incorrecto, el número ingresado es menor al número a adivinar. \nLe quedan",10-cont,"Oportunidades.\n")
            
        if cont == 10:
            print("Intentarlo en otra ocasión. GAME OVER PAPÁ. \n")
            nom=input("Ingresar el nombre del jugador: ")

            for item in funciones.jugador:
                if (nom == item['nombre']):
                    item["puntaje"]=item["puntaje"]-25
            break

def mododificil(): #Aca el codigo es igual, pero sin la parte de mostrar si el valor ingresado es mayor o menor que el valor de x
    x=random.randint(1, 20)

    cont=0
    print("Bienvenido a adivina el número. Dependiendo de la cantidad de jugadores que hayan en la consola en esta ocasión\nel juego se repetirá, recuerde que si pierde uno, al haber más de un jugador, no podrán jugar en caso de que uno tenga\n menos créditos de los que pide el juego.\n")

    for n in range(12):    
        num=input("Ingresar un número, e intentar acertar el número aleatorio o ingresar x para salir: \n")
        print("")
        
        while not num.isnumeric() or int(num)>20:
            if num == "X".lower():
                break
            num=input("Ingresar variables numéricas, e intentar acertar el número aleatorio: \n")
            print("")
            
        if num == "X".lower():
            break

        if int(num)==x:
            print (f"Usted acertó, el número era: {x}. \nUsted ha ganado!\n")
            nom=input("Ingresar el nombre del jugador: ")

            for item in funciones.jugador:
                if (nom == item['nombre']):
                    item["puntaje"]=item["puntaje"]+75
            break    
        else:
            cont=cont+1
            print(f"Número incorrecto, le quedan {10-cont} oportunidades.\n")
            
        if cont == 10:
            print("Intentarlo en otra ocasión. GAME OVER PAPÁ. \n")
            nom=input("Ingresar el nombre del jugador: ")

            for item in funciones.jugador:
                if (nom == item['nombre']):
                    item["puntaje"]=item["puntaje"]-75
            break

def ahorcado():
    print("")
    selecciones = ["QATAR" , "ALEMANIA", "DINAMARCA","BRASIL","BELGICA","FRANCIA","CROACIA","ESPAÑA","SERBIA","INGLATERRA","SUIZA","HOLANDA","ARGENTINA","IRAN","COREADELSUR","JAPON","ARABIASAUDITA","ECUADOR", "URUGUAY","CANADA","GHANA","SENEGAL","PORTUGAL","POLONIA","TUNEZ","MARRUECOS","CAMERUN","ESTADOSUNIDOS","MEXICO","GALES","AUSTRALIA","COSTARICA"]
    selec_aleatoria = selecciones[random.randint(0,31)]
    palabra = ""
    cont = 3

    while cont > 0:
        cont_fallas = 0

        for letra in selec_aleatoria:
            if letra in palabra:
                print(letra,end="")
            else:
                print("_ ", end="")
                cont_fallas += 1

        if cont_fallas == 0:
            print(" GANASTE")
            nom=input("Ingresar el nombre del jugador: ")

            for item in funciones.jugador:
                if (nom == item['nombre']):
                    item["puntaje"]=item["puntaje"]+50
            
            print("\nFin del juego / Siguiente jugador\n")
            break

        letra=input(" Ingrese UNA letra: ")
        palabra += letra.upper()

        if letra.upper() not in selec_aleatoria:
            cont-=1
            print(" ERRASTE")
            print("Te quedan", +cont, "vidas")

        if cont == 0:
            print("¡GAME OVER!, era: ",selec_aleatoria)
            nom=input("Ingresar el nombre del jugador: ")

            for item in funciones.jugador:
                if (nom == item['nombre']):
                    item["puntaje"]=item["puntaje"]-50
            print("\nFin del juego / Siguiente jugador\n")
            