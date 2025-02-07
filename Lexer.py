import re
from typing import List, Tuple

class Lexer:
    def __init__(self):
        self.tokens = [
            ('WHITESPACE', r'\s+'),  # Espacios en blanco
            ('COMMENT', r'//.*?\n'),  # Comentarios
            
            ('STRING', r'"(?:[^"\\]|\\.)*"'),  # Cadenas
            ('NUMBER', r'\d+(\.\d+)?([eE][+-]?\d+)?'),  # Números
            ('BOOLEAN', r'\btrue\b|\bfalse\b'),  # Booleanos
            
            ('IF', r'\bif\b'),  # Palabra clave 'if'
            ('THEN', r'\bthen\b'),  # Palabra clave 'then'
            ('ELSE', r'\belse\b'),  # Palabra clave 'else'
            
            ('LOGICAL_OPERATOR', r'==|!=|<=|>=|<|>'),  # Operadores lógicos
            ('ASSIGN', r'='),  # Operador de asignación
            ('OPERATOR', r'[+\-*/]'),  # Operadores aritméticos
            
            ('LPAREN', r'\('),  # Paréntesis izquierdo
            ('RPAREN', r'\)'),  # Paréntesis derecho
            ('LBRACE', r'\{'),  # Llave izquierda
            ('RBRACE', r'\}'),  # Llave derecha
            ('SEMICOLON', r';'),  # Punto y coma
            
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_#$]*'),  # Identificadores
            ('UNKNOWN', r'.'),  # Cualquier otro carácter no reconocido
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
                    print(value)  # Muestra el valor completo antes de procesarlo

                    # Verificamos si es un identificador y contiene un '#'
                    if token_name == "IDENTIFIER" and '#' in value:
                        tokens_found.append(("UNKNOWN", value))  # Marcamos como error
                        pos += len(value)
                        break

                    # Verificamos si el número contiene un alfabeto inmediatamente después
                    if token_name == "NUMBER" and pos + len(value) < len(code) and code[pos + len(value)].isalpha():
                        error_match = re.match(r'\d+[a-zA-Z_]\w*', code[pos:])
                        if error_match:
                            value = error_match.group(0)
                        tokens_found.append(("UNKNOWN", value))
                        pos += len(value)
                        break

                    # Ignoramos espacios en blanco y comentarios
                    if token_name not in ['WHITESPACE', 'COMMENT']:
                        tokens_found.append((token_name, value))

                    pos = match.end()
                    break

            if not match:
                raise SyntaxError(f'Carácter inesperado: {code[pos]}')

        return tokens_found
