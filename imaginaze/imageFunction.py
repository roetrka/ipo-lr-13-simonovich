import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter import filedialog as fd
from tkinter import simpledialog
from PIL import Image, ImageTk
from .imageHandler import ImageHandler


class Imagine(tk.Frame,ImageHandler):
    def __init__(self, master=None):
        super().__init__(master)
        self.initUI()

    def initUI(self):
        self.pack()
        
        # Визуал кнопок для взаимодействия с обьектами  fill.x растягивание кнопки 
        ttk.Button(self, text='Файл', command=self.load_image_gui).pack(fill=tk.X)
        ttk.Button(self, text='Размер', command=self.re_size_gui).pack(fill=tk.X)
        ttk.Button(self, text='Сохранить', command=self.save_to_file_gui).pack(fill=tk.X)
        ttk.Button(self, text='JPG', command=self.remake_format_gui).pack(fill=tk.X)
        ttk.Button(self, text='Поворот на 45', command=self.turn_gui).pack(fill=tk.X)
        ttk.Button(self, text='Резкость', command=self.sharpen_load_gui).pack(fill=tk.X)
        ttk.Button(self, text='Рамка 15ph', command=self.border_load_gui).pack(fill=tk.X)


    
        # Лейбл для вывода изображения при изменении/загрузке
        self.label_photo = ttk.Label(self)
        self.label_photo.pack(pady=10)
    

    def load_image_gui(self):
        self.file_path = fd.askopenfilename(title="Выберите нужный вам формат", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*")])  #окно переход в проводник для выбора нужного файла вручную
        try:
            self.load_image(self.file_path)
            self.update_label(self.img)  # вывод на лейбл изображения
        except:
            showerror("Ошибка", "Файл не удалось открыть") # вывод при ошибок


    #метод обновления лейбла
    def update_label(self, img):
        self.img_tk = ImageTk.PhotoImage(img)  # метод ткинтера
        self.label_photo.config(image=self.img_tk)  # обновление лейбла


    def re_size_gui(self):
        width = simpledialog.askinteger("Ширина", "Введите ширину") #Ввод через диалоговое окно ширины
        height = simpledialog.askinteger("Высота", "Введите высоту") #Ввод через диалоговое окно высоты
        if width and height:
            try:  
                self.re_size(width,height)
                self.update_label(self.img)  # изменение лейбла
            except:
                showerror("Ошибка", "Не удалось изменить изображение") # вывод при ошибке


    def save_to_file_gui(self):
        try:
            self.save_to_file(self.file_path)
        except:
             showerror("Ошибка", "Не удалось Сохранить изображение") # вывод при ошибке


    def remake_format_gui(self):
        try:
            self.remake_format(self.file_path)
        except:
            showerror("Ошибка", "Не удалось изменить формат изображения") # вывод при ошибке


    def turn_gui(self):
        try:
            self.turn(self.img)
            self.update_label(self.img)  # сохранение на лейбл
        except:
            showerror("Ошибка", "Не удалось изменить ориентацию изображения") # вывод при ошибке


    # метод повышения резкости изображения
    def sharpen_load_gui(self):
            try:
                self.sharpen_load(self.img)
                self.update_label(self.img)  # меняем лейбл
            except:
                showerror("Ошибка", "Не удалось  применить фильтр резкости") # вывод при ошибке


    def border_load_gui(self):
        try:
            self.border_load(self.img)
            self.update_label(self.img) # меняем лейбл
        except:
            showerror("Ошибка", "Не удалось создать рамку изображению") # вывод при ошибке
