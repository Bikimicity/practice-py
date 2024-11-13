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
    def __init__(self, canvas):
        self.canvas = canvas
        self.bells_image = Image.open("bell.png")
        self.bells_image = self.bells_image.resize((60, 60))
        self.bell_image = ImageTk.PhotoImage(self.bells_image)
        self.bell = self.canvas.create_image(50, 50, anchor="center", image=self.bell_image)
        
    def create_bells(self):
        self.bells = [Bell(self.canvas) for _ in range(10)]
        return self.bells
        
    def arrange_bells(self, bells):
        # 벨 객체들의 위치 조정
        for i, bell in enumerate(bells):
            # 위쪽 5개 벨 위치 (y=50)
            if i < 5:
                x = 50 + i * 120  # 간격을 120으로 설정
                y = 50
            # 아래쪽 5개 벨 위치 (y=550)
            else:
                x = 50 + (i - 5) * 120  # 간격을 120으로 설정
                y = 550
            bell.set_position(x, y)  # 위치 설정 메서드 호출
            
    def set_position(self, x, y):
        # 이미지를 지정된 (x, y) 위치로 이동
        self.canvas.coords(self.bell, x, y)