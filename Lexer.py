import re
from typing import List, Tuple

class Lexer:
    def __init__(self):
        self.tokens = [
            ('COMMENT', r'//[^\n]*'),              # Comentarios (línea que inicia con //)
            ('NUMBER', r'\d+(\.\d*)?'),           # Enteros y números reales
            ('STRING', r'"[^"]*"'),                # Cadenas de caracteres
            ('IDENTIFIER', r'[a-zA-Z_]\w*'),        # Identificadores (nombres de variables)
            ('OPERATOR', r'[+\-*/]'),              # Operadores aritméticos
            ('LOGICAL_OPERATOR', r'==|!=|<|>'),     # Operadores lógicos
            ('ASSIGN', r'='),                      # Operador de asignación
            ('IF', r'if'),                         # Palabra clave 'if'
            ('THEN', r'then'),                     # Palabra clave 'then'
            ('ELSE', r'else'),                     # Palabra clave 'else'
            ('LPAREN', r'\('),                     # Paréntesis izquierdo
            ('RPAREN', r'\)'),                     # Paréntesis derecho
            ('LBRACE', r'\{'),                     # Llave izquierda
            ('RBRACE', r'\}'),                     # Llave derecha
            ('SEMICOLON', r';'),                   # Punto y coma
            ('WHITESPACE', r'\s+'),                # Espacios en blanco
            ('UNKNOWN', r'.'),                     # Cualquier otro carácter no reconocido
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
