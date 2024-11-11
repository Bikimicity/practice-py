import tkinter as tk

class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("서빙로봇 시뮬레이터")
        self.create_table_button()
        
    def create_table_button(self):
        for i in range(1, 11):
            # 각 버튼을 grid()로 배치
            table = tk.Button(self.root, text=f"{i}번 테이블", command=lambda i=i: self.on_table_call(i))
            row = (i - 1) // 5
            column = (i - 1) % 5
            table.grid(row=row, column=column, padx=5, pady=5)

    def on_table_call(self, table):
        print(f"{table}번 테이블 호출됨")  # 버튼 클릭 시 메시지 출력
    
    def run(self):
        self.root.mainloop()
