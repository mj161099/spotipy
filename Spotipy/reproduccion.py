import threading
import pygame
from cancion import Cancion

class Reproduccion:
    def __init__(self):
        pygame.mixer.init()
        self.pista_actual = None
        self.reproduciendo = False
        self.hilo_reproduccion = None

    def play(self, cancion):
        self.pista_actual = cancion
        self.reproduciendo = True

        def reproducir():
            pygame.mixer.music.load(cancion.ruta)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                if not self.reproduciendo:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            self.reproduciendo = False

        # Crear y empezar un hilo para la reproducción de la canción
        self.hilo_reproduccion = threading.Thread(target=reproducir)
        self.hilo_reproduccion.start()

    def pause(self):
        self.reproduciendo = False
        pygame.mixer.music.pause()

    def resume(self):
        if self.pista_actual and not self.reproduciendo:
            self.reproduciendo = True
            pygame.mixer.music.unpause()

    def stop(self):
        self.pista_actual = None
        self.reproduciendo = False
        pygame.mixer.music.stop()
