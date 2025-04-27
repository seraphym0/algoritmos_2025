def usarlafuerza(mochila, cantobjetos=0):
    if not mochila:
        return False, cantobjetos
    
    objeto = mochila.pop()
    cantobjetos += 1

    if objeto == "sable de luz":
        return True, cantobjetos
    else:
        return usarlafuerza(mochila, cantobjetos)

# Como la actividad deja elegir, se asume que el Jedi en cuestión es Anakin Skywalker

mochila = []
print("Escriba los objetos que están en la mochila, uno por uno. Anakin los va a sacar de la mochila en orden inverso. Escriba 'fin' para dejar de añadir objetos.")
while True:
    objeto = input().strip().lower()
    if objeto == "fin":
        break
    mochila.append(objeto)

encontrado, objeto = usarlafuerza(mochila)

if encontrado:
    print(f"Anakin encontró un sable de luz despues de {objeto} objetos.")
else:
    print(f"Anakin no encontró un sable de luz.")