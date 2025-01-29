from Lexer import Lexer
from FileHandler import FileHandler
from UI import UI

def main():
    lexer = Lexer()
    file_handler = FileHandler()
    ui = UI(lexer, file_handler)
    ui.run()

if __name__ == "__main__":
    main()