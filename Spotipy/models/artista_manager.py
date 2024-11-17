import os
import json
from .artista import Artista

class ArtistaManager:
    def __init__(self, json_file):
        base_dir = os.path.dirname(__file__)  # Directorio actual del script
        project_dir = os.path.abspath(os.path.join(base_dir, os.pardir,os.pardir))  # Subir un nivel desde spotipy
        file_path = os.path.join(project_dir, 'data', json_file)  # Construir la ruta a la carpeta data
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"No such file or directory: '{file_path}'")
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.artistas = self._create_artistas(data['artistas'])

    def _create_artistas(self, artistas_data):
        return [Artista.from_json(artista_data) for artista_data in artistas_data]

    def get_artistas(self):
        return self.artistas
