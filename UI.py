import tkinter as tk
from tkinter import filedialog, messagebox, font
from tkinter import ttk
from typing import List, Tuple
from Lexer import Lexer
from FileHandler import FileHandler

class UI:
    def __init__(self, root: tk.Tk, lexer: Lexer, file_handler: FileHandler):
        self.lexer = lexer
        self.file_handler = file_handler
        
        root.title("Lexer Analyzer")
        root.geometry("800x500")
        root.configure(bg="#f0f0f0")
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", 
                        background="#e1e1e1",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#e1e1e1",
                        font=("Helvetica", 10))
        style.configure("Treeview.Heading",
                        background="#4a4a4a",
                        foreground="white",
                        font=("Helvetica", 11, "bold"))
        style.map("Treeview", background=[('selected', '#347083')])
        
        header_font = font.Font(family="Helvetica", size=14, weight="bold")
        btn_font = font.Font(family="Helvetica", size=10)
        
        self.label = tk.Label(root, text="Seleccione un archivo .txt para analizar", 
                              bg="#f0f0f0", fg="#333333", font=header_font)
        self.label.pack(pady=15)
        
        self.select_file_btn = tk.Button(root, text="Seleccionar archivo", 
                                         command=self.select_file,
                                         bg="#4a90e2", fg="white",
                                         font=btn_font, relief="flat", padx=10, pady=5,
                                         activebackground="#357ab8", activeforeground="white")
        self.select_file_btn.pack(pady=10)
        
        self.table_frame = tk.Frame(root, bg="#f0f0f0")
        self.table_frame.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)
        
        self.token_table = ttk.Treeview(self.table_frame, columns=("Tipo", "Valor"), show="headings")
        self.token_table.heading("Tipo", text="Tipo de Token")
        self.token_table.heading("Valor", text="Valor del Token")
        self.token_table.column("Tipo", anchor=tk.CENTER, width=150)
        self.token_table.column("Valor", anchor=tk.W, width=600)
        self.token_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar = ttk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=self.token_table.yview)
        self.token_table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return
        try:
            code = self.file_handler.read_file(file_path)
            tokens = self.lexer.tokenize(code)
            self.display_tokens(tokens)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_tokens(self, tokens: List[Tuple[str, str]]):        
        for row in self.token_table.get_children():
            self.token_table.delete(row)

        if not tokens:
            messagebox.showinfo("Información", "No se encontraron tokens.")
            return
        
        for token_type, token_value in tokens:
            self.token_table.insert("", tk.END, values=(token_type, token_value))