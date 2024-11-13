class RobotController:
    def __init__(self, canvas, robot):
        self.canvas = canvas
        self.robot = robot  # robot 객체

    def move_robot_to(self, target_x, target_y, speed=5):
        """로봇을 목표 위치로 이동시키는 메서드"""
        # 로봇의 현재 좌표를 가져오기
        current_x, current_y = self.canvas.coords(self.robot)

        # x, y 방향으로 이동해야 할 거리 계산
        delta_x = target_x - current_x
        delta_y = target_y - current_y

        # 거리가 speed 이하이면 목표 위치 도달
        distance = (delta_x ** 2 + delta_y ** 2) ** 0.5
        if distance < speed:
            self.canvas.coords(self.robot, target_x, target_y)
        else:
            # 이동할 방향 계산
            step_x = speed * (delta_x / distance)
            step_y = speed * (delta_y / distance)
            
            # 로봇 이동
            self.canvas.move(self.robot, step_x, step_y)
            
            # 20밀리초 후에 move_robot_to 호출하여 애니메이션 효과
            self.canvas.after(20, self.move_robot_to, target_x, target_y, speed)
