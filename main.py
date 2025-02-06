import tkinter as tk
from Lexer import Lexer
from FileHandler import FileHandler
from UI import UI

def main():
    root = tk.Tk()
    lexer = Lexer()
    file_handler = FileHandler()
    ui = UI(root, lexer, file_handler)    
    root.mainloop()    

if __name__ == "__main__":
    main()