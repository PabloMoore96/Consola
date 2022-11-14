
import juegos
import funciones

if __name__=="__main__":

    num_jugadores = input("¿Cuantos jugadores serán?\n")
    while not num_jugadores.isnumeric():
        num_jugadores = input("\n¿Cuantos jugadores serán? ingresar números:\n")
    
    num_jugadores=int(num_jugadores)

    for i in range(num_jugadores):
        print ("Jugador ",1+i)
        funciones.add_jugador()

    print("")
    option=0

    while not option == 4:   

        op=input("Ingresar una opción: \n1- Juego modo fácil (Con ayuda)\n2- Juego modo difícil (Sin ayuda)\n3- Juego ahorcado\n4- Salir\n")
        print("")
        while not op.isnumeric():
            op=input("Ingresar una opción numérica: \n1- Juego modo fácil\n2- Juego modo dificil\n3- Salir\n")
            print("")
        option=int(op)

        if option == 1:
            for item in funciones.jugador:
                if item['puntaje']<25:
                    print("El puntaje de uno de los jugadores es muy bajo. ")
            
            if item['puntaje']>=25:
                for i in range(num_jugadores):
                    juegos.modofacil()

        elif option == 2:
            
            for item in funciones.jugador:
                if item['puntaje']<75:
                    print("El puntaje de uno de los jugadores es muy bajo. ")
            
            if item['puntaje']>=75:
                for i in range(num_jugadores):         
                    juegos.mododificil()

        elif option == 3:

            for item in funciones.jugador:
                if item['puntaje']<50:
                    print("El puntaje de uno de los jugadores es muy bajo. ")
            
            if item['puntaje']>=50:
                print("Bienvenido a ahorcado. Dependiendo de la cantidad de jugadores que hayan en la consola en esta ocasión\nel juego se repetirá, recuerde que si pierde uno, al haber más de un jugador, no podrán jugar en caso de que uno tenga\n menos créditos de los que pide el juego.\n")
                for i in range(num_jugadores):
                    juegos.ahorcado()

    funciones.show_jugador()    
    print("""
    ###################################
    #                                 #
    #        Gracias por jugar        #
    #                                 #
    ###################################
    """)
    
            
