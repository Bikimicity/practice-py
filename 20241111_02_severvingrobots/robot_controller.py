from animation import move_robot
import time

class RobotController:
    def __init__(self, ui):
        self.ui = ui
        self.call_queue = []

    def add_call(self, table_number):
        self.call_queue.append(table_number)
        if len(self.call_queue) == 1:
            self.start_serving()

    def start_serving(self):
        while self.call_queue:
            table_number = self.call_queue.pop(0)
            self.go_to_table(table_number)
        self.return_to_home()

    def go_to_table(self, table_number):
        print(f"{table_number}번 호출 출발합니다.")
        move_robot(table_number)
        time.sleep(2)  # 서빙 대기 시간

    def return_to_home(self):
        print("모든 서빙 완료, 로봇이 홈으로 돌아옵니다.")
