from .autenticacion_usuario import AutenticacionUsuario
from .reproduccion import Reproduccion
from .cancion import Cancion
from .biblioteca import Biblioteca
from .artista import Artista
from .album import Album
from .playlist import Playlist
from .artista_manager import ArtistaManager

""" Encapsular todas las funcionalidades del menu """
class Menu:
    def __init__(self):
        self.autenticacion_usuario = AutenticacionUsuario()
        self.reproduccion = Reproduccion()
        self.current_user = None
        self.biblioteca = None

        print("""                                                                      
                                                                                               
                                                                                               
           ..:::...                                                                            
       .:-==========-:.                                                                        
     :=================-:                                                                      
   :=====================-.                                                                    
  -========================:                                               :-:    ...          
 :===::..        ..::-======.      .-====--.                         --:   ===. :====:         
.====...:::::::::..    .:====     .==-:::-=:  ..  ...       ....    .==-.. ... .==-...      .. 
-=========-----======-:..-===:    :==:.      -==-=====:   :======:.:======.-==.========.   :==.
======.           .:-========:     -====--:  -==-. .-==: ===:...===..==-.. -== .==-..==-  .==: 
======---=======--:.  .-=====:       .::-===.-==     -==:==.    .==: ==:   -==  ==-  .==: -=-  
:======--:::::::--===-:======.    .:.    .==:-==.   .==-.==-    :==..==:   -==  ==-   :==-==.  
 =====-.:::::::::. .:-======-     -===---==-.-===---===. :===---==:  ===--.-==  ==-    -===:   
 .=================-:-======.      .::---:.  -==.:--::     :----:.   .:--: :::  :::  . .==-    
  .=======================-.                 -==                                    .====-     
    :====================:                   ...                                     ....      
     .:===============-:                                                                       
        .:--=====--::                                                                          
                                                           
                                        
        """)

    """ Muestra el menú principal y maneja la selección de opciones """
    def menu_principal(self):
        while True:
            print("\n--- Inicio ---\n")
            print("1. Registrarse")
            print("2. Iniciar Sesión")
            print("3. Tu biblioteca")
            print("4. Lista de reproducción")
            print("5. Salir")

            opciones = input("\nSeleccione una opción: ")

            if opciones == "1":
                self.registro_usuario()
            elif opciones == "2":
                self.iniciar_sesion()
            elif opciones == "3":
            	self.mostrar_biblioteca()
            elif opciones == "4":
                self.menu_lista_reproduccion()
            elif opciones == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")


    """ Metodos de funcionalidad manejan las respectivas funcionalidades del menú. """
    def registro_usuario(self):
        usuario_id = input("Ingrese ID de usuario: ")
        nombre = input("Ingrese nombre: ")
        email = input("Ingrese email: ")
        contraseña = input("Ingrese contraseña: ")
        resultado = self.autenticacion_usuario.registro_usuario(usuario_id, nombre, email, contraseña)
        print(resultado)

    def iniciar_sesion(self):
        email = input("Ingrese email: ")
        contraseña = input("Ingrese contraseña: ")
        resultado = self.autenticacion_usuario.login_usuario(email, contraseña)
        print(resultado)
        if "Bienvenido" in resultado:
            self.current_user = self.autenticacion_usuario.usuarios[email]
            self.biblioteca = Biblioteca(self.current_user)

    def mostrar_biblioteca(self):
        if self.current_user:
            while True:
                resultado = self.biblioteca.get_biblioteca_info()
                artistas_guardados = [str(artista) for artista in resultado['Artistas guardados']]
                print("\n--- Tu biblioteca ---\n")
                print(f"Artistas guardados: {', '.join(artistas_guardados)}")
                print("1. Agregar artista")
                print("2. Volver al inicio")

                opciones = input("Seleccione una opción: ")

                if opciones == "1":
                    self.agregar_artista_biblioteca()
                    # Actualizar la lista de artistas guardados después de agregar un nuevo artista
                    resultado = self.biblioteca.get_biblioteca_info()
                    artistas_guardados = [str(artista) for artista in resultado['Artistas guardados']]
                elif opciones == "2":
                    break
        else:
            print("Por favor, inicie sesión primero.")

    def agregar_artista_biblioteca(self):
        # Lista de instancias de artistas desde JSON
        artista_manager = ArtistaManager('artistas.json')
        artistas = artista_manager.get_artistas()

        print("Elige más artistas que te gusten.")
        while artistas:  # Continuar mientras haya artistas disponibles
            print("\nSeleccione un artista de la lista:")
            for i, artista in enumerate(artistas, 1):
                print(f"{i}. {artista.nombre}")
            
            # Validar la selección del usuario
            while True:
                try:
                    seleccion = int(input("\nIngrese el número del artista: "))
                    if 1 <= seleccion <= len(artistas):
                        artista = artistas.pop(seleccion - 1)  # Eliminar el artista de la lista
                        print(f"Artista seleccionado: {artista.nombre}")
                        break  # Salir del bucle de selección
                    else:
                        print("\nSelección inválida. Intente de nuevo.")
                except ValueError:
                    print("\nEntrada inválida. Por favor, ingrese un número.")
            
            print(f"Artista '{artista.nombre}' agregado a tu biblioteca.")
            self.biblioteca.guardar_artista(artista)

            if not artistas:
                print("No hay más artistas disponibles para agregar.")
                break


    def menu_lista_reproduccion(self):
        if self.current_user:
            while True:
                print("\n--- Lista de reproducción ---\n")
                print("1. Crear Lista de Reproducción")
                print("2. Agregar Canción a Lista de Reproducción")
                print("3. Reproducir Canción")
                print("4. Pausar Reproducción")
                print("5. Reanudar Canción")
                print("6. Detener Reproducción")
                print("7. Volver al inicio")

                opciones = input("\nSeleccione una opción: ")

                if opciones == "1":
                    self.crear_playlist()
                elif opciones == "2":
                    self.añadir_cancion_playlist()
                elif opciones == "3":
                    self.reproducir_cancion()
                elif opciones == "4":
                    self.reproduccion.pause()
                    print("Reproducción pausada.")
                elif opciones == "5":
                    self.reproduccion.resume()
                    print("Reproducción reanudada.")
                elif opciones == "6":
                    self.reproduccion.stop()
                    print("Reproducción detenida.")
                elif opciones == "7":
                    break
                else:
                    print("\nOpción no válida. Intente de nuevo.")
        else:
            print("\nPor favor, inicie sesión primero.")                

    def crear_playlist(self):
        if self.current_user:
            nombre = input("Ingrese nombre de la lista de reproducción: ")
            playlist = self.current_user.crear_playlist(nombre)
            print(f"'\nLista de reproducción '{playlist.nombre}' creada.")
        else:
            print("Por favor, inicie sesión primero.")

    def seleccionar_artista(self):
        # Lista de instancias de artistas predefinidos
        artista_manager = ArtistaManager('artistas.json')
        artistas = artista_manager.get_artistas()

        print("\nSeleccione un artista de la lista:")
        for i, artista in enumerate(artistas, 1):
            print(f"{i}. {artista.nombre}")
                
        # Validar la selección del usuario
        while True:
            try:
                seleccion = int(input("\nIngrese el número del artista: "))
                if 1 <= seleccion <= len(artistas):
                    artista = artistas[seleccion - 1]
                    print(f"Artista seleccionado: {artista.nombre}")
                    return artista
                    break
                else:
                    print("\nSelección inválida. Intente de nuevo.")
            except ValueError:
                print("\nEntrada inválida. Por favor, ingrese un número.")    

    def añadir_cancion_playlist(self):
        if self.current_user:
            playlist_nombre = input("Ingrese nombre de la lista de reproducción: ")
            playlist = next((pl for pl in self.current_user.playlists if pl.nombre == playlist_nombre), None)
            if playlist:
                artista = self.seleccionar_artista()

                # Mostrar álbumes del artista seleccionado
                print("\nSeleccione un álbum de la lista:")
                for i, album in enumerate(artista.albums, 1):
                    print(f"{i}. {album.titulo} - {album.fecha_lanzamiento}")
                try:
                    album_seleccionado = artista.albums[int(input("\nIngrese el número del álbum: ")) - 1]
                except (IndexError, ValueError):
                    print("Número de álbum inválido. Por favor, intente de nuevo.")
                    return

                # Mostrar canciones del álbum seleccionado
                print("\nSeleccione una canción de la lista:")
                for i, cancion in enumerate(album_seleccionado.canciones, 1):
                    print(f"{i}. {cancion.titulo}")
                try:
                    cancion_seleccionada = album_seleccionado.canciones[int(input("\nIngrese el número de la canción: ")) - 1]
                except (IndexError, ValueError):
                    print("Número de canción inválido. Por favor, intente de nuevo.")
                    return

                ruta = cancion_seleccionada.ruta 
                cancion = Cancion(cancion_seleccionada.titulo, artista.nombre, album_seleccionado.titulo, ruta, cancion_seleccionada.duracion)
                playlist.añadir_cancion(cancion)
                duracion_total = Playlist.calcular_duracion_total(playlist.canciones)
                total_canciones = Playlist.contar_canciones(playlist.canciones)

                print(f"\nCanción '{cancion_seleccionada.titulo}' agregada a la lista de reproducción '{playlist.nombre}'.")
                print(f"Tienes un total de {total_canciones} canciones en tu lista.")
                print(f"La duración total de la lista de reproducción es de: {duracion_total} segundos.")
            else:   
                print("\nLista de reproducción no encontrada.")
        else:
            print("\nPor favor, inicie sesión primero.")


    def reproducir_cancion(self):
        if self.current_user:
            playlist_nombre = input("Ingrese nombre de la lista de reproducción: ")
            playlist = next((pl for pl in self.current_user.playlists if pl.nombre == playlist_nombre), None)
            if playlist:
                cancion_titulo = input("Ingrese título de la canción: ")
                cancion = next((tr for tr in playlist.canciones if tr.titulo == cancion_titulo), None)
                if cancion:
                    cancion.play()
                    self.reproduccion.play(cancion)
                else:
                    print("\nCanción no encontrada en la lista de reproducción.")
            else:
                print("\nLista de reproducción no encontrada.")
        else:
            print("\nPor favor, inicie sesión primero.")