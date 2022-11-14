jugador = []

def add_jugador():
    nombre=input("Ingresar nombre del jugador: ")
    puntaje=100
    data = {
        "nombre": nombre,
        "puntaje": puntaje
    }
    jugador.append(data)
    for item in jugador:
        print("-----------------------------\n")
        print(f"Nombre: {item['nombre']}\n")
        print(f"Puntaje: {item['puntaje']}\n")

def show_jugador():
    for item in jugador:
        print("-----------------------------\n")
        print(f"Nombre: {item['nombre']}\n")
        print(f"Puntaje: {item['puntaje']}\n")
        
