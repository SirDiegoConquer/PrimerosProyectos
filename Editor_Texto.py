###- Crea una interfaz gráfica de usuario (GUI)
###- para simular nuestro propio editor de texto. Este 
###- ejemplo también utiliza componentes estándar de GUI,
###- incluyendo etiquetas, botones y campos de entrada. 
###- Puedes añadir la capacidad de abrir y guardar archivos, 
###- al igual que un editor de texto real.
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto Simple")

        # Crear el área de texto con barra de desplazamiento
        self.text_area = ScrolledText(root, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill='both')

        # Crear el menú
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        # Añadir opciones al menú
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=root.quit)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Archivos de texto", "*.txt"),
                                                          ("Todos los archivos", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Archivos de texto", "*.txt"),
                                                            ("Todos los archivos", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()         
## Fin del código del editor de texto