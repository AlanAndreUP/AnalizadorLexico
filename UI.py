from Lexer import Lexer
from FileHandler import FileHandler
from typing import List, Tuple
class UI:
    def __init__(self, lexer: Lexer, file_handler: FileHandler):
        self.lexer = lexer
        self.file_handler = file_handler

    def run(self):
        file_path = input("Ingrese la ruta del archivo .txt a analizar: ")
        try:
            code = self.file_handler.read_file(file_path)
            tokens = self.lexer.tokenize(code)
            self.display_tokens(tokens)
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def display_tokens(tokens: List[Tuple[str, str]]):
        print("\nTokens encontrados:")
        for token in tokens:
            print(f"Tipo: {token[0]}, Valor: {token[1]}")