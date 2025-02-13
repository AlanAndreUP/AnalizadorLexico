class FileHandler:
    @staticmethod
    def read_file(file_path: str) -> str:
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo {file_path} no existe.")
        except IOError as e:
            raise IOError(f"Error al leer el archivo: {e}")