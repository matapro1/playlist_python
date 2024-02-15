# Diccionario vacío para almacenar la playlist
playlist = {}  
# Lista vacía de canciones en la playlist
playlist['canciones'] = []  

# Función principal
def app():
    # Agregar playlist
    agregar_playlist = True

    while agregar_playlist:
        # Solicitamos al usuario que ingrese un nombre para la playlist
        nombre_playlist = input('¿Cómo deseas nombrar la playlist 🎶?\n')

        if nombre_playlist:
            # Asignamos el nombre de la playlist al diccionario
            playlist['nombre'] = nombre_playlist  
            # Ya tenemos un nombre, desactivamos el flag agregar_playlist
            agregar_playlist = False
    
    # Llamamos a la función para agregar canciones después de que el usuario haya ingresado el nombre de la playlist
    agregar_canciones(nombre_playlist)

# Función para agregar canciones a la playlist
def agregar_canciones(nombre_playlist):
    # Bandera para agregar canciones
    agregar_cancion = True

    while agregar_cancion:
        # Preguntamos al usuario qué canción desea agregar
        pregunta = f'\r\nAgrega canciones para la playlist {nombre_playlist}:\r\n'
        pregunta += 'Escribe "x" para dejar de agregar canciones:\r\n'

        cancion = input(pregunta)

        if cancion.lower() == 'x':
            # Dejar de agregar canciones si el usuario ingresa 'x'
            agregar_cancion = False
            
            # Mostrar resumen de la playlist
            mostrar_resumen(nombre_playlist)
        else:
            # Agregamos las canciones a la lista de canciones en el diccionario de la playlist
            playlist['canciones'].append(cancion)

# Función para mostrar un resumen de la playlist
def mostrar_resumen(nombre_playlist):
    # Imprimimos el nombre de la playlist
    print(f'Playlist: {nombre_playlist}\r\n')
    # Imprimimos el encabezado de las canciones
    print('Resumen de tus Canciones:\r\n')
    # Iteramos sobre la lista de canciones y las imprimimos
    for cancion in playlist['canciones']:
        print(cancion)

# Llamamos a la función principal para iniciar la aplicación
app()
