from imaginaze.imageFunction import Imagine

from PIL import Image
import tkinter as tk


class Application(tk.Tk): # класс наследует tkinter 
    def __init__(self):
        super().__init__()
        self.title('Работа с фото') # титульник дял программы
        first_label = tk.Label(self, text="Работа с фото", font=10) #   лейбл для программы
        first_label.pack(pady=2, padx=2) # размещение лейбла в окне
        self.image_handler = Imagine(master=self) # создание обьекта класса
        self.image_handler.pack(pady=5, padx=5) # расмещение окна обьекта в главном  окне программы

        

app = Application() # создание обькта класса
app.mainloop() # вывод главного окна


