
personajes = [
    {"nombre": "Tony Stark","heroe": "Iron Man","genero": "M","peliculas": 10},
    {"nombre": "Steve Rogers","heroe": "Capitán América","genero": "M","peliculas": 9},
    {"nombre": "Thor Odinson","heroe": "Thor","genero": "M","peliculas": 9},
    {"nombre": "Bruce Banner","heroe": "Hulk","genero": "M","peliculas": 8},
    {"nombre": "James Rhodes","heroe": "War Machine","genero": "M","peliculas": 7},
    {"nombre": "Natasha Romanoff","heroe": "Black Widow","genero": "F","peliculas": 8},
    {"nombre": "Clint Barton","heroe": "Hawkeye","genero": "M","peliculas": 6},
    {"nombre": "Peter Quill","heroe": "Star-lord","genero": "M","peliculas": 5},
    {"nombre": "Gamora","heroe": "Gamora","genero": "F","peliculas": 5},
    {"nombre": "Rocket Raccoon","heroe": "Rocket","genero": "M","peliculas": 6},
    {"nombre": "Groot","heroe": "Groot","genero": "M","peliculas": 6},
    {"nombre": "Drax","heroe": "Drax el Destructor","genero": "M","peliculas": 5},
    {"nombre": "Bucky Barnes","heroe": "Winter Soldier","genero": "M","peliculas": 6},
    {"nombre": "Wanda Maximoff","heroe": "Scarlet Witch","genero": "F","peliculas": 6},
    {"nombre": "Sam Wilson","heroe": "Falcon","genero": "M","peliculas": 5},
    {"nombre": "JARVIS","heroe": "Vision","genero": "M","peliculas": 5},
    {"nombre": "Scott Lang","heroe": "Ant-Man","genero": "M","peliculas": 5},
    {"nombre": "T'Challa'","heroe": "Black Panther","genero": "M","peliculas": 4},
    {"nombre": "Peter Parker","heroe": "Spider-Man","genero": "M","peliculas": 6},
    {"nombre": "Steven Strange","heroe": "Dr. Strange","genero": "M","peliculas": 4},
    {"nombre": "Nebula","heroe": "Nebula","genero": "F","peliculas": 5},
    {"nombre": "Mantis","heroe": "Mantis","genero": "F","peliculas": 4},
    {"nombre": "Loki Laufeyson","heroe": "Loki","genero": "M","peliculas": 6},
    {"nombre": "Hope Van Dyne","heroe": "Wasp","genero": "F","peliculas": 4},
    {"nombre": "Carol Danvers","heroe": "Capitana Marvel","genero": "F","peliculas": 3},
    {"nombre": "Matt Murdock","heroe": "Daredevil","genero": "M","peliculas": 1},
    {"nombre": "Wade Wilson","heroe": "Deadpool","genero": "M","peliculas": 2},
    {"nombre": "James 'Logan' Howlett","heroe": "Wolverine","genero": "M","peliculas": 1},
    {"nombre": "Reed Richards","heroe": "Mr. Fantástico","genero": "M","peliculas": 1},
    {"nombre": "Sue Storm","heroe": "Invisible Woman","genero": "F","peliculas": 1},
    {"nombre": "Johnny Storm","heroe": "Human Torch","genero": "M","peliculas": 1},
    {"nombre": "Ben Grimm","heroe": "The Thing","genero": "M","peliculas": 1},
]

def posicion(pila, nombres):
    posiciones = {}
    for i in range(1, len(pila) + 1):
        personaje = pila[-i]
        if personaje['nombre'] in nombres:
            posiciones[personaje['nombre']] = i
    return posiciones
nombres_buscados = ['Rocket Raccoon', 'Groot']
posiciones = posicion(personajes, nombres_buscados)
print("Posiciones desde la cima:", posiciones)


def peliculas(pila):
    resultado = []
    for personaje in pila:
        if personaje.get("peliculas", 0) > 5:
            resultado.append((personaje["nombre"], personaje["peliculas"]))
    return resultado
resultado2 = peliculas(personajes)
print("Personajes con más de 5 películas:")
for nombre, cantidad in resultado2:
    print(f"{nombre}: {cantidad}")


def blackwidow(pila):
    for personaje in pila:
        if personaje["heroe"] == "Black Widow":
            return personaje["peliculas"]
    return 0
cantidad = blackwidow(personajes)
print(f"La Viuda Negra fué parte de {cantidad} películas.")


def iniciales(pila, iniciales):
    resultado = []
    for personaje in pila:
        if personaje['nombre'][0].upper() in iniciales:
            resultado.append(personaje)
    return resultado
personajes_filtrados = iniciales(personajes, {'C', 'D', 'G'})
print("Personajes cuyos nombres (no de heroe) empiezan con C, D o G:")
for p in personajes_filtrados:
    print(f"{p['nombre']} ({p['heroe']})")