# 2개의 주사위를 굴리는 프로그램

import random 

while True:
  """
  1. 사용자에게 주사위를 굴릴지 말지 물어본다.
  2. y / n 둘중 하나를 입력해야 하고 .lower() 함수로 인해 대문자로 작성해도 소문자로 변환된다.
  3. 조건문에서 만약 y 라면 2개의 주사위를 굴려 랜덤한 숫자 조합 2개를 만든다. 프로그램은 끝나지 않는다.
  4. 만약 n 을 선택한다면 정해진 출력문을 띄우고 break문으로 인해 가장 가까운 반복문이 종료된다.
  5. y / n 을 입력하지 않고 다른 것을 입력하면 else 문의 출력문을 출력한다. 프로그램은 끝나지 않는다.
  """
  choice = input('Roll the dice? (y/n): ').lower()
  if choice == 'y':
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(f'({die1}, {die2})')
  elif choice == 'n':
      print('Thanks for playing!')
      break
  else:
      print('Invalid choice!')