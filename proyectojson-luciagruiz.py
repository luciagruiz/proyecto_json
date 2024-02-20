import json

def cargar_datos():
    with open("nba.json") as file:
        data = json.load(file)
    return data

#1. Listar información: Mostrar la lista de equipos de la NBA que juegan en la conferencia especificada por el usuario.
def listar_equipos_por_conferencia(conferencia, equipos):
    equipos_conferencia = []
    for equipo in equipos:
        if equipo["conference"].lower() == conferencia.lower():
            equipos_conferencia.append(equipo["teamName"])
    return equipos_conferencia

def mostrar_equipos_conferencia():
    datos = cargar_datos()
    conferencia_usuario = input("\nIntroduce la conferencia (Este/Oeste): ")
    equipos_conferencia = listar_equipos_por_conferencia(conferencia_usuario, datos)
    
    if equipos_conferencia:
        print(f"\nEquipos de la conferencia {conferencia_usuario}:")
        for equipo in equipos_conferencia:
            print("- ", equipo)
    else:
        print(f"\nNo se encontraron equipos en la conferencia {conferencia_usuario}.")

#2. Contar información: Pedir al usuario que ingrese una altura y contar el total de jugadores en la liga que tengan esa altura o mas.
def contar_jugadores_por_altura(altura, equipos):
    total_jugadores = 0
    jugadores_altura = []
    for equipo in equipos:
        for jugador in equipo["players"]:
            if jugador["height_cm"] == altura:
                total_jugadores += 1
                jugadores_altura.append((jugador["name"], equipo["teamName"]))
    return total_jugadores, jugadores_altura

def contar_jugadores_por_altura_mayor(altura, equipos):
    total_jugadores = 0
    for equipo in equipos:
        for jugador in equipo["players"]:
            if jugador["height_cm"] > altura:
                total_jugadores += 1
    return total_jugadores

def contar_jugadores_altura():
    try:
        equipos = cargar_datos()
        altura_usuario = int(input("\nIntroduce una altura en centímetros: "))
        total_jugadores_altura, jugadores_altura = contar_jugadores_por_altura(altura_usuario, equipos)
        total_jugadores_altura_mayor = contar_jugadores_por_altura_mayor(altura_usuario, equipos)

        if jugadores_altura:
            print(f"\nJugadores que miden {altura_usuario} cm:")
            print("\n{:<20}| {:<25}".format("Jugador", "Equipo"))
            print("-" * 55)
            for jugador, equipo in jugadores_altura:
                print("{:<20} {:<25}".format(jugador, equipo))
        else:
            print(f"\nNo se encontraron jugadores de {altura_usuario} cm")
        print(f"\nTotal de jugadores con altura igual a {altura_usuario} cm: {total_jugadores_altura}")
        print(f"Total de jugadores con altura mayor a {altura_usuario} cm: {total_jugadores_altura_mayor}")
    except ValueError:
        print("La altura debe ser un valor numérico.")

#3. Buscar o filtrar información: Pedir al usuario que ingrese el nombre de un jugador y mostrar en qué equipo juega.
def buscar_equipo_por_jugador(nombre_jugador, equipos):
    for equipo in equipos:
        for jugador in equipo["players"]:
            if jugador["name"].lower() == nombre_jugador.lower():
                return equipo["teamName"]
    return None

def buscar_equipo_jugador():
    equipos = cargar_datos()
    nombre_jugador = input("\nIntroduce el nombre de un jugador: ")
    equipo_jugador = buscar_equipo_por_jugador(nombre_jugador, equipos)
    if equipo_jugador:
        print(f"\n{nombre_jugador} juega en el equipo: {equipo_jugador}")
    else:
        print(f"\nNo se encontró información sobre {nombre_jugador}")

#4. Buscar información relacionada: Pedir al usuario que ingrese una edad y mostrar la lista de jugadores que tengan esa edad.
def buscar_jugadores_por_edad(edad, equipos):
    jugadores_por_edad = []
    for equipo in equipos:
        for jugador in equipo["players"]:
            if jugador["age"] == edad:
                jugadores_por_edad.append((jugador["name"], equipo["teamName"]))
    return jugadores_por_edad

def buscar_jugadores_edad():
    try:
        equipos = cargar_datos()
        edad_usuario = int(input("\nIntroduce una edad: "))
        jugadores_edad = buscar_jugadores_por_edad(edad_usuario, equipos)
        if jugadores_edad:
            print(f"\nJugadores de {edad_usuario} años:")
            print("\n{:<20}| {:<25}".format("Jugador", "Equipo"))
            print("-" * 55)
            for jugador, equipo in jugadores_edad:
                print("{:<20} {:<25}".format(jugador, equipo))
        else:
            print(f"\nNo se encontraron jugadores de {edad_usuario} años")
    except ValueError:
        print("La edad debe ser un valor numérico entero positivo.")

#5. Ejercicio libre: Mostrar el promedio de altura de los jugadores de cada equipo, el jugador más alto y el más bajo de cada equipo.
def promedio_altura_por_equipo(equipos):
    promedios = {}
    for equipo in equipos:
        jugadores = equipo["players"]
        mas_alto = max(jugadores, key=lambda x: x["height_cm"])
        mas_bajo = min(jugadores, key=lambda x: x["height_cm"])
        total_altura = sum(jugador["height_cm"] for jugador in jugadores)
        promedio = total_altura / len(jugadores)
        promedios[equipo["teamName"]] = {
            "promedio": promedio,
            "mas_alto": mas_alto,
            "mas_bajo": mas_bajo
        }
    return promedios

def promedio_altura_equipo():
    equipos = cargar_datos()
    promedios_altura = promedio_altura_por_equipo(equipos)
    print("\nPromedio de altura por equipo:")
    print("\n{:<25}| {:<25}| {:<25}| {:<25}".format("Equipo", "Promedio de altura (cm)", "Máxima altura (cm)", "Mínima altura (cm)"))
    print("-" * 105)
    for equipo, info in promedios_altura.items():
        nombre_mas_alto = info['mas_alto']['name']
        altura_mas_alto = info['mas_alto']['height_cm']
        nombre_mas_bajo = info['mas_bajo']['name']
        altura_mas_bajo = info['mas_bajo']['height_cm']
        print("{:<25} {:<26.2f} {:<21} {:<5} {:<21} {:<5}".format(equipo, info['promedio'], nombre_mas_alto, altura_mas_alto, nombre_mas_bajo, altura_mas_bajo))

def menu():
    opciones = {
        "1": mostrar_equipos_conferencia,
        "2": contar_jugadores_altura,
        "3": buscar_equipo_jugador,
        "4": buscar_jugadores_edad,
        "5": promedio_altura_equipo,
        "6": salir
    }
    var = 0
    while var == 0:
        print("\nSeleccione una opción:")
        print("1. Listar equipos por conferencia")
        print("2. Contar jugadores por altura")
        print("3. Buscar equipo por jugador")
        print("4. Buscar jugadores por edad")
        print("5. Promedio de altura por equipo")
        print("6. Salir")
        opcion = input("\nIntroduce una opción: ")

        if opcion == "6":
            var = var + 1
        
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("\nOpción no válida. Por favor, selecciona una opción válida.")

def salir():
    print("Saliendo del programa")

menu()
