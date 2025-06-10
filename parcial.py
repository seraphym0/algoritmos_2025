from super_heroes_data import superheroes
from collections import deque

class Superheroe:
    def __init__(self, heroesinfo):
        self.heroes = heroesinfo

    def listaheroes(self):
        """Actividad 1 listado ordenado"""
        ordenados = sorted(self.heroes, key=lambda h: h["name"])
        return [h["name"] for h in ordenados]

    def ordenheroes(self, nombres):
        """Activ 2 posiciones de Rocket y The Thing"""
        posiciones = {}
        for nombre in nombres:
            for i, h in enumerate(self.heroes):
                if h["name"] == nombre:
                    posiciones[nombre] = i
                    break
            else:
                posiciones[nombre] = -1  # no encontrado
        return posiciones

    def villanos(self):
        """Act 3 lista de villanos"""
        return [h for h in self.heroes if h["is_villain"]]

    def villanos1980(self):
        """Act 4 villanos antes del 1980"""
        cola = deque([h for h in self.heroes if h["is_villain"]])
        villanos_antes_1980 = []
        while cola:
            v = cola.popleft()
            if v.get("first_appearance", 9999) < 1980:
                villanos_antes_1980.append(v)
        return villanos_antes_1980

    def initheroes(self, iniciales):
        """Act 5 lista por iniciales"""
        iniciales = [ini for ini in iniciales]
        encontrados = []
        for h in self.heroes:
            alias = (h["alias"])
            real_name = (h["real_name"])
            if any(alias.startswith(ini) or real_name.startswith(ini) for ini in iniciales):
                encontrados.append(h)
        return encontrados

    def namerealheroes(self):
        """Act 6 nombres reales"""
        return sorted(self.heroes, key=lambda h: (h["real_name"]))

    def fechaheroes(self):
        """Act 7 lista por fecha de aparición"""
        return sorted(self.heroes, key=lambda h: h["first_appearance", 999])

    def antman(self, alias_objetivo, nuevo_nombre_real):
        """Act 8 modiicación de Ant-Man"""
        for h in self.heroes:
            if h.get("alias") == alias_objetivo:
                h["real_name"] = nuevo_nombre_real
                return h
        return None

    def biografiaheroes(self, palabras):
        """Act 9 palabras en la bio"""
        palabras = [p for p in palabras]
        encontrados = []
        for h in self.heroes:
            bio = (h["short_bio"])
            if any(p in bio for p in palabras):
                encontrados.append(h)
        return encontrados

    def borrarheroes(self, nombres):
        """Act 10 eliminacion de personajes"""
        eliminados = []
        nuevos_heroes = []
        nombres_set = set(nombres)
        for h in self.heroes:
            if h["name"] in nombres_set:
                eliminados.append(h)
            else:
                nuevos_heroes.append(h)
        self.heroes = nuevos_heroes
        return eliminados


if __name__ == "__main__":
    gestor = Superheroe(superheroes)

    print("----- Punto 1:")
    for h in gestor.listaheroes():
        print(h)

    posiciones = gestor.ordenheroes(["The Thing", "Rocket Raccoon"])
    print("----- Punto 2:")
    for nombre, pos in posiciones.items():
        print(f"{nombre}: {pos}")
    print()

    print("----- Punto 3:")
    for v in gestor.villanos():
        print(f"{v['alias']} ({v['name']})")
    print()

    print("----- Punto 4:")
    for v in gestor.villanos1980():
        print(f"{v['alias']} - {v['first_appearance']}")
    print()

    print("----- Punto 5:")
    for h in gestor.initheroes(["Bl", "G", "My", "W"]):
        print(f"{h['alias']} ({h['real_name']})")
    print()

    print("----- Punto 6:")
    for h in gestor.namerealheroes():
        print(h["real_name"], "-", h["alias"])
    print()

    print("----- Punto 7:")
    for h in gestor.fechaheroes():
        print(f"{h['alias']} - {h['first_appearance']}")
    print()

    print("----- Punto 8:")
    modificado = gestor.antman("Ant Man", "Scott Lang")
    if modificado:
        print(f"Modificado: {modificado['alias']} ahora es {modificado['real_name']}")
    else:
        print("No se encontró Ant Man.")
    print()

    print("----- Punto 9:")
    for h in gestor.biografiaheroes(["time-traveling", "suit"]):
        print(f"{h['alias']} - {h['short_bio']}")
    print()

    eliminados = gestor.borrarheroes(["Electro", "Baron Zemo"])
    print("Eliminados:")
    if eliminados:
        for h in eliminados:
            print(f"{h['alias']} - {h['name']}")
    else:
        print("No se eliminaron personajes.")