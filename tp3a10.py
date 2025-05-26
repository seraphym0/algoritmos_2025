
# notificaciones de ejemplo
cola = [
    {'hora': '12:00', 'aplicacion': 'Facebook', 'mensaje': 'Has recibido una solicitud de amistad'},
    {'hora': '13:15', 'aplicacion': 'Twitter', 'mensaje': 'Alguien indicó que le gusta tu post'},
    {'hora': '14:00', 'aplicacion': 'Instagram', 'mensaje': 'Tu reel llegó a los 1000 me gustas'},
    {'hora': '15:30', 'aplicacion': 'Whatsapp', 'mensaje': 'Has recibido un mensaje'},
    {'hora': '16:45', 'aplicacion': 'Twitter', 'mensaje': 'Splinter Experto En Python te siguió'},
    {'hora': '18:00', 'aplicacion': 'Facebook', 'mensaje': 'Revisa tu muro'},
]

# definiciones de las actividades

def eliminarnotisfacebook(cola):
    nueva_cola = []
    for noti in cola:
        if noti['aplicacion'].lower() != 'facebook':
            nueva_cola.append(noti)
    return nueva_cola

def twittsdepython(cola):
    resultados = []
    for noti in cola:
        if (noti['aplicacion'].lower() == 'twitter' and 
            'python' in noti['mensaje'].lower()):
            resultados.append(noti)
    return resultados

def horas(hora, inicio, fin):
    return inicio <= hora <= fin

def notifhoras(cola, hora_inicio='11:43', hora_fin='15:57'):
    pila = []
    contador = 0
    for noti in cola:
        if horas(noti['hora'], hora_inicio, hora_fin):
            pila.append(noti)
            contador += 1
    return pila, contador


# acciones

cola = eliminarnotisfacebook(cola)

print("Notificaciones de Twitter con 'Python':")
for notif in twittsdepython(cola):
    print(notif)

pila, cantidad = notifhoras(cola)
print(f"\nNotificaciones entre 11:43 y 15:57: {cantidad}")