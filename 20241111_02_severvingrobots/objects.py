import tkinter as tk
from PIL import Image, ImageTk

class Robot:
    def __init__(self, canvas, image_path="robots.png", size=(100, 100), position=(300, 300)):
        self.canvas = canvas
        self.image_path = image_path  
        self.image = Image.open(self.image_path)
        self.image = self.image.resize(size, Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(position[0], position[1], image=self.tk_image)

class Bell:
    def __init__(self, canvas, robot ,image_path="bell.png" ,size=(50, 50), position=(300, 300)):
        self.canvas = canvas
        self.image_path = image_path  
        self.image = Image.open(self.image_path)
        self.image = self.image.resize(size, Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.robot = robot
        self.canvas.create_image(position[0], position[1], image=self.tk_image)
