import tkinter as tk
from PIL import Image, ImageTk
from objects import *

class Animation:
    def __init__(self, frame3):
        self.frame3 = frame3
        self.canvas = tk.Canvas(self.frame3, width=600, height=600)
        self.canvas.pack()
        
        self.robot = Robot(self.canvas)
        self.tablebutton = Bell(self.canvas, self.robot)