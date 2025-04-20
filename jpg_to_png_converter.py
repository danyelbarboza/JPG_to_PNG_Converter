import os
from tkinter import Tk, Label, Button, filedialog, Text, END, Frame
from PIL import Image

class JPGtoPNGConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor JPG para PNG")
        self.input_folder = ""
        self.output_folder = ""
        self.scale_factor = 1
        
        Label(root, text="Pasta de Entrada (JPG):").pack()
        Button(root, text="Selecionar Pasta", command=self.select_input_folder).pack()
        Label(root, text="Pasta de Saída (PNG):").pack()
        Button(root, text="Selecionar Pasta", command=self.select_output_folder).pack()
        
        size_frame = Frame(root)
        size_frame.pack(pady=5)
        self.btn_half = Button(size_frame, text="Reduzir pela metade", command=self.select_half_size)
        self.btn_half.pack(side="left", padx=5)
        self.btn_normal = Button(size_frame, text="Tamanho Normal", command=self.select_normal_size)
        self.btn_normal.pack(side="left", padx=5)
        self.btn_double = Button(size_frame, text="Aumentar 2x", command=self.select_double_size)
        self.btn_double.pack(side="left", padx=5)
        
        Button(root, text="Iniciar Conversão", command=self.convert_images).pack(pady=10)
        Label(root, text="Status:").pack()
        self.status_box = Text(root, height=10, width=60)
        self.status_box.pack()
        self.update_button_styles()

    def select_half_size(self):
        self.scale_factor = 0.5
        self.update_button_styles()

    def select_normal_size(self):
        self.scale_factor = 1
        self.update_button_styles()

    def select_double_size(self):
        self.scale_factor = 2
        self.update_button_styles()

    def update_button_styles(self):
        if self.scale_factor == 1:
            self.btn_normal.config(relief="sunken", bg="#cccccc")
            self.btn_double.config(relief="raised", bg="SystemButtonFace")
            self.btn_half.config(relief="raised", bg="SystemButtonFace")
        elif self.scale_factor == 2:
            self.btn_normal.config(relief="raised", bg="SystemButtonFace")
            self.btn_double.config(relief="sunken", bg="#cccccc")
            self.btn_half.config(relief="raised", bg="SystemButtonFace")
        elif self.scale_factor == 0.5:
            self.btn_half.config(relief="sunken", bg="#cccccc")
            self.btn_normal.config(relief="raised", bg="SystemButtonFace")
            self.btn_double.config(relief="raised", bg="SystemButtonFace")
        else:
            self.btn_normal.config(relief="sunken", bg="#cccccc")
            self.btn_double.config(relief="raised", bg="SystemButtonFace")
            self.btn_half.config(relief="raised", bg="SystemButtonFace")

    def select_input_folder(self):
        self.input_folder = filedialog.askdirectory()
        self.log(f"Pasta de entrada selecionada: {self.input_folder}")

    def select_output_folder(self):
        self.output_folder = filedialog.askdirectory()
        self.log(f"Pasta de saída selecionada: {self.output_folder}")

    def convert_images(self):
        if not self.input_folder or not self.output_folder:
            self.log("Erro: selecione as pastas antes de iniciar.")
            return

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        files = os.listdir(self.input_folder)
        count = 0

        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg')):
                img_path = os.path.join(self.input_folder, filename)
                try:
                    img = Image.open(img_path)
                    if self.scale_factor == 2:
                        new_size = (img.width * 2, img.height * 2)
                        img = img.resize(new_size, Image.Resampling.LANCZOS)
                        size_info = " (2x)"
                    elif self.scale_factor == 0.5:
                        new_size = (int(img.width / 2), int(img.height / 2))
                        img = img.resize(new_size, Image.Resampling.LANCZOS)
                        size_info = " (1/2x)"
                    else:
                        size_info = ""
                    clean_name = os.path.splitext(filename)[0]
                    output_path = os.path.join(self.output_folder, clean_name + '.png')
                    img.save(output_path, 'PNG')
                    self.log(f"Convertido{size_info}: {filename}")
                    count += 1
                except Exception as e:
                    self.log(f"Erro ao converter {filename}: {e}")
                finally:
                    img.close()
        
        self.log(f"Conversão concluída! {count} imagem(ns) convertida(s).")

    def log(self, message):
        self.status_box.insert(END, message + "\n")
        self.status_box.see(END)

if __name__ == "__main__":
    root = Tk()
    app = JPGtoPNGConverter(root)
    root.mainloop()