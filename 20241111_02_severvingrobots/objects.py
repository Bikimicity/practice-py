import tkinter as tk
from PIL import Image, ImageTk
import os

class Robot:
    def __init__(self, canvas):
        self.canvas = canvas
        self.robots_image = Image.open(os.path.join("20241111_02_severvingrobots", "images", "robots.png"))
        self.robots_image = self.robots_image.resize((100, 100))
        self.robot_image = ImageTk.PhotoImage(self.robots_image)
        self.robot = self.canvas.create_image(400, 270, anchor="center", image=self.robot_image)  # self.robot에 저장


class Bell:
    def __init__(self, canvas, bell_id):
        self.canvas = canvas
        self.id = bell_id
        self.bells_image = Image.open(os.path.join("20241111_02_severvingrobots", "images", "bell.png"))
        self.bells_image = self.bells_image.resize((60, 60))
        self.bell_image = ImageTk.PhotoImage(self.bells_image)
        self.bell = self.canvas.create_image(50, 50, anchor="center", image=self.bell_image)
        
    @classmethod
    def create_bells(cls, canvas):
        # 10개의 벨 객체를 생성하고 리스트로 반환
        return [cls(canvas, i+1) for i in range(10)]
        
    @staticmethod
    def arrange_bells(bells):
        bell_positions = {}
        
        for i, bell in enumerate(bells):
            if i < 5:
                x = 50 + i * 170
                y = 50
            else:
                x = 50 + (i - 5) * 170
                y = 550
            
            bell.set_position(x, y)
            bell_positions[bell.id] = {"x": x, "y": y}
        
        return bell_positions
    
    def set_position(self, x, y):
        self.canvas.coords(self.bell, x, y)