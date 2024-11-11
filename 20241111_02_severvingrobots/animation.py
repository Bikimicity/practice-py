import time

def move_robot(table_number):
    # 단순 이동 애니메이션
    print(f"로봇이 {table_number}번 테이블로 이동 중...")
    time.sleep(1)
    print(f"{table_number}번 테이블에 도착했습니다.")
