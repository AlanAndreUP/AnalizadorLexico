import re
from typing import List, Tuple

class Lexer:
    def __init__(self):
        self.tokens = [
            # Ignorar espacios en blanco y comentarios primero
            ('WHITESPACE', r'\s+'),                        # Espacios en blanco, tabs y saltos de línea
            ('COMMENT', r'//.*?\n'),                       # Comentarios - captura toda la línea hasta el salto
            
            # Literales
            ('STRING', r'"(?:[^"\\]|\\.)*"'),             # Cadenas con soporte para caracteres escapados
            ('NUMBER', r'\d+(\.\d+)?([eE][+-]?\d+)?'),    # Números con soporte para notación científica
            
            # Palabras clave - antes que identificadores para evitar conflictos
            ('IF', r'\bif\b'),                            # Palabra clave 'if' con límites de palabra
            ('THEN', r'\bthen\b'),                        # Palabra clave 'then' con límites de palabra
            ('ELSE', r'\belse\b'),                        # Palabra clave 'else' con límites de palabra
            
            # Operadores - ordenados por longitud para evitar conflictos
            ('LOGICAL_OPERATOR', r'==|!=|<=|>=|<|>'),     # Operadores lógicos expandidos
            ('ASSIGN', r'='),                             # Operador de asignación
            ('OPERATOR', r'[+\-*/]'),                     # Operadores aritméticos
            
            # Delimitadores
            ('LPAREN', r'\('),                            # Paréntesis izquierdo
            ('RPAREN', r'\)'),                            # Paréntesis derecho
            ('LBRACE', r'\{'),                            # Llave izquierda
            ('RBRACE', r'\}'),                            # Llave derecha
            ('SEMICOLON', r';'),                          # Punto y coma
            
            # Identificadores - después de palabras clave
            ('IDENTIFIER', r'[a-zA-Z_]\w*'),              # Identificadores
            
            # Token de error - siempre al final
            ('UNKNOWN', r'.'),                            # Cualquier otro carácter no reconocido
        ]

    def tokenize(self, code: str) -> List[Tuple[str, str]]:
        pos = 0
        tokens_found = []
        regexes = [re.compile(token_regex) for _, token_regex in self.tokens]
        while pos < len(code):
            match = None
            for token_name, regex in zip((token_name for token_name, _ in self.tokens), regexes):
                match = regex.match(code, pos)
                if match:
                    value = match.group(0)
                    # Ignorar espacios en blanco y comentarios
                    if token_name not in ['WHITESPACE', 'COMMENT']:
                        tokens_found.append((token_name, value))
                    pos = match.end()
                    break
            if not match:
                raise SyntaxError(f'Carácter inesperado: {code[pos]}')
        return tokens_found
