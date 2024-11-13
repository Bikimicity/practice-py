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

        self.bells = Bell.create_bells(self.canvas)
        self.bell_positions = Bell.arrange_bells(self.bells)

        # 저장된 벨 위치 정보 출력
        print("벨 위치 정보:", self.bell_positions)
        
        