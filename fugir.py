import tkinter as tk
import random
import webbrowser

class MyApp:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Trocar link")

        # Configurar o tamanho da janela
        self.parent.geometry("1000x900")

        # Centralizar a janela na tela
        self.parent.eval('tk::PlaceWindow . center')

        self.frame = tk.Frame(self.parent, bg="red")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame, bg="red")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.image = tk.PhotoImage(file="")
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)

        self.button1 = tk.Button(self.frame, text="obvio", command=self.open_link, bg="white", fg="black", font=("Helvetica", 20))
        self.button1.pack(side=tk.LEFT, padx=200, pady=200)

        self.button2 = tk.Button(self.frame, text="Não", command=self.change_button_position, bg="white", fg="black", font=("Helvetica", 20))
        self.button2.pack(side=tk.RIGHT, padx=200, pady=200)

        self.label = tk.Label(self.frame, text="O miguel é o melhor?", bg="red", fg="white", font=("Helvetica", 30))
        self.label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def open_link(self):
        self.change_label_text()
        self.button1.config(text="claro!!!", command=self.open_new_link)

    def open_new_link(self):
        webbrowser.open("https://ibb.co/Kssb3Nm")

    def change_button_position(self):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        self.button2.place(x=x, y=y)
        self.button1.place(relx=0.25, rely=0.5, anchor=tk.CENTER)

    def change_label_text(self):
        self.label.config(text="Adoras-me não adoras?")

    def change_button_position_back(self):
        self.button2.place(relx=0.75, rely=0.5, anchor=tk.CENTER)
        self.button1.place(relx=0.25, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
