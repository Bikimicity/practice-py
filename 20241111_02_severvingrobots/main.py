from ui import *  # ui 폴더의 mainUI.py에서 UI 클래스 가져오기
from robot_controller import RobotController

if __name__ == "__main__":
    ui_instance = windows()  # ui와 변수명이 겹치지 않도록 변경
    robot_controller = RobotController(ui_instance)
    ui_instance.run()
