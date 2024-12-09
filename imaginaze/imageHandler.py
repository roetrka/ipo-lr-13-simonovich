import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter import filedialog as fd
from tkinter import simpledialog
from PIL import Image, ImageTk



class ImageHandler():
    def __init__(self):
        self.img = None  
        self.file_path = None  


    def load_image(self,file_path):
        self.img = Image.open(self.file_path)
        


    # изменение размера изображения
    def re_size(self,width ,height):
        self.img = self.img.resize((width, height))  # Изменение размера



    # метод сохранения в файл
    def save_to_file(self,file_path):
        self.img.save(self.file_path)  # обновление старого файла на новый



    # изменение формата на jpg
    def remake_format(self,file_path):
        jpg_path = f"{self.file_path.split('.', 1)[0]}.jpg" # разделяем файл на 2 части получается список из 2 элементов где 1 это пусть файла 2 это .png и добавляем к 1 элементу jpg второй убираем
        self.img.save(jpg_path)



        
    #метод поворота на 45 градусов
    def turn(self,img):
        self.img  = self.img.rotate(45) # повторот и присвоение обьекту




                      
