import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from objects import *

class Animation:
    def __init__(self, frame3):
        self.frame3 = frame3
        self.canvas = Canvas(self.frame3, width=800, height=600, bg="white")
        self.canvas.pack(pady=20)
        
        self.robot = Robot(self.canvas)
        self.bell = Bell(self.canvas)

        self.bells = self.bell.create_bells()
        self.bell.arrange_bells(self.bells)