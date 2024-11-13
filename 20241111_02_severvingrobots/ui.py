import tkinter as tk
from animation import Animation

class Windows:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("서빙로봇 시뮬레이터")
        self.root.geometry("1200x800")
        
        # 전체 프레임
        self.frame = Frame(self.root)
        self.frame.create_frame()
        
        # 엔트리 상자
        self.entrybox = EntryBox(self.frame.frame2)
        self.entrybox.create_entry_box()
        
        # 애니메이션 추가
        self.animation = Animation(self.frame.frame3)
        
        # 테이블 버튼 생성
        self.tablebtn = TableBtn(self.frame.frame1, self.entrybox, self.animation)
        self.tablebtn.create_table_button()
        
    def run(self):
        self.root.mainloop()
    
class Frame:
    def __init__(self, root):
        self.root = root
        self.frame1 = None
        self.frame2 = None
        self.frame3 = None

    def create_frame(self):
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()
    
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()
    
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack()

class TableBtn:
    def __init__(self, frame1, entrybox, animation):
        self.frame1 = frame1
        self.entrybox = entrybox
        self.animation = animation
        
    def create_table_button(self):
        for i in range(1, 11):
            # 각 버튼을 grid()로 배치하고 고유 테이블 번호를 전달
            table = tk.Button(self.frame1, text=f"{i}번 테이블", command=lambda table_id=i: self.on_table_call(table_id))
            row = (i - 1) // 5
            column = (i - 1) % 5
            table.grid(row=row, column=column, padx=5, pady=5)
            
    def on_table_call(self, table_id):
        # EntryBox에 호출된 테이블 번호 출력
        self.entrybox.update_entry(f"{table_id}번 호출 됨")
        
        # 해당 테이블 ID에 맞는 호출벨 위치로 로봇 이동
        if table_id in self.animation.bell_positions:
            bell_position = self.animation.bell_positions[table_id]
            target_x, target_y = bell_position["x"], bell_position["y"]
            self.animation.move_robot_to(target_x, target_y)
        else:
            print(f"테이블 ID {table_id}에 대한 호출벨 위치를 찾을 수 없습니다.")

class EntryBox:
    def __init__(self, frame2):
        self.frame2 = frame2
    
    def create_entry_box(self):
        self.entry = tk.Entry(self.frame2)
        self.entry.pack()

    def update_entry(self, text):
        # Entry 위젯에 텍스트를 출력
        self.entry.delete(0, tk.END)  # 기존 텍스트를 지운 후
        self.entry.insert(0, text)    # 새로운 텍스트 삽입