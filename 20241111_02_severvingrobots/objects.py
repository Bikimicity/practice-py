import tkinter as tk
from PIL import Image, ImageTk

class Robot:
    def __init__(self, canvas):
        self.canvas = canvas
        self.robots_image = Image.open("robots.png")
        self.robots_image = self.robots_image.resize((100, 100))
        self.robot_image = ImageTk.PhotoImage(self.robots_image)
        self.canvas.create_image(400, 270, anchor="center", image=self.robot_image)

class Bell:
    def __init__(self, canvas, robot):
        pass