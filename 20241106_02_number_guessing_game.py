# 컴퓨터와 숫자 맞추기 게임 같네요!

import random 

number_to_guess = random.randint(1, 100)

while True:
  """
  1. 프로그램이 실행되면 1~100 사이의 랜덤 정수를 생성하고 변수에 저장합니다.
  2. 사용자로부터 숫자를 입력 받습니다. 공백으로 입력하면 valueError를 띄웁니다.
  3. 높거나 낮으면 Too low, Too high 를 띄워 힌트를 줍니다.
  4. 정답을 맞추면 축하 메세지와 함께 break문이 실행되면서 가장 가까운 반복문이 종료됩니다.
  """
  try:
    guess = int(input('Guess the number between 1 and 100: '))

    if guess < number_to_guess:
      print('Too low!')
    elif guess > number_to_guess:
      print('Too high!')
    else:
      print('Congratulations! You guessed the number.')
      break
  except ValueError:
    print('Please enter a valid number')
