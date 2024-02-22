import tkinter as tk
import os
from tkinter import filedialog

class FileDecompressor:

    def __init__(self):
        self.file_path = None
        self.output_path = None     

    def select_file(self):
        archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos .tar.gz", "*.tar.gz")])
        self.file_path.delete(0, tk.END)  
        self.file_path.insert(0, archivo)  

    def show_success_message(self, message=''):
        tk.messagebox.showinfo("Información", message)

    def show_error_message(self, message=''):
        tk.messagebox.showerror("Error", message)

    def decompress_file(self, file_path, output_path=None):
        command = f'tar -xvf {file_path}'
        if output_path:
            command += f' -C {output_path}'
        res = os.system(command)
        if res == 0:
            self.show_success_message("Archivo descomprimido correctamente")
        else:
            self.show_error_message("Error al descomprimir el archivo")

    def select_output_path(self):
        path = filedialog.askdirectory()
        self.output_path.delete(0, tk.END)
        self.output_path.insert(0, path)

    def main(self):
        window = tk.Tk()
        window.title("Selector de archivos")

        tk.Label(window, text="Archivo .tar.gz:").pack()

        self.file_path = tk.Entry(window, width=50)
        self.file_path.pack()

        btn_select_file = tk.Button(window, text="Seleccionar archivo", command=self.select_file)
        btn_select_file.pack()

        tk.Label(window, text="Ruta para guardar el descomprimido:").pack()
        self.output_path = tk.Entry(window, width=50)
        self.output_path.pack()

        btn_output_path = tk.Button(window, text="Seleccionar ruta", command=self.select_output_path)
        btn_output_path.pack()

        btn_decompress = tk.Button(window, text="Descomprimir archivo", command=lambda: self.decompress_file(self.file_path.get(), self.output_path.get()))
        btn_decompress.pack()

        window.mainloop()
