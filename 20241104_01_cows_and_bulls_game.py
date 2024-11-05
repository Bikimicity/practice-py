import random

def generate_secret():
  """
  1. list(range(10))로 0~9 까지의 숫자를 digits 라는 변수에 담는다
  2. random.shuffle(digits)로 digits에 차례대로 담긴 0~9까지의 숫자를 랜덤으로 섞는다
  3. return ''.join([str(digit) for digit in digits[:4]])의 구동 원리를 설명한다
    - 리스트 컴프리헨션이라는 기술이 사용된다.
    - 우선 for 반복문은 랜덤으로 섞인 digits 변수 0~3째 인덱스를 반환한다.
    - 리스트 컴프리헨션이기 때문에 str(digits)에 정수였던 숫자를 문자열로 넣는다.
    - ''.join() 이라는 함수는 ''빈 문자열 없이 모두 하나로 연결 시킨다로 해석할 수 있다.
  4. 전체적으로 종합하자면 0~9 까지의 숫자를 리스트로 만들어 변수에 담고
     리스트 안에 숫자를 랜덤으로 섞어서 리스트 컴프리헨션을 이용해 for 반복문을 통해 변수 0~3번째 까지의 인덱스를 문자열로 반환하고 
     모두 하나의 문자열로 잇는다.
    """
  digits = list(range(10))
  random.shuffle(digits)
  return ''.join([str(digit) for digit in digits[:4]])


def calculate_cows_and_bulls(secret, guess):
  """
  1. bulls는 main() 함수의 input 받은 정수 값과 비교하는 표현식이다.
    - 우선 secret은 아까 랜덤으로 셔플 된 숫자를 저장한 변수다.
    - guess는 사용자가 입력한 숫자다.
    - 이번에도 리스트 컴프리헨션 수식으로 for 반복문을 수행한다.
    - 반복문을 0~3 까지 돌면서 secret 과 guess 의 각 자리의 인덱스 값을 비교한다.
    - 동일한 자리에 동일한 숫자가 맞으면 숫자 1을 추가한다. ex) [1,2,3,4], [1,6,3,4] => bulls = 3

  2. cows는 숫자가 포함되어 있으면 1을 추가하는 표현식이다.
    - bulls 와는 달리 자리가 같지 않고 동일한 숫자가 포함만 되어 있어도 1을 추가하는 방식이다
    - ex) guess = [1,3,5,7], secret = [8,5,4,3] => bulls = 0, cows = 2
  
  3. return 을 통해 cows, bulls 를 함수 외부로 반환한다.
  """
  bulls = sum([1 for i in range(4) if guess[i] == secret[i]])
  cows = sum([1 for i in range(4) if guess[i] in secret]) - bulls

  return cows, bulls


def main():
  """
  1. 위에서 설명한 내용은 생략한다.
  2. while 반복문
    - 이 반복문은 참이 될 때까지 무한 반복된다.
    - if len() : 이 조건문은 guess 가 4개인지, 숫자인지, 4개의 숫자로 이루어져 있는지 확인한다.
    - 반환 된 secret, guess 를 cows, bulls 변수에 저장하고 출력한다.
    - if bulls : 조건문은 bulls 의 값이 4가 나올 때 즉, guess = secret 일때 참이고 break를 통해 while 반복문을 끝낸다.
    - else 는 if 조건문이 거짓일 때 준비 된 문자를 출력한다.
  """
  secret = generate_secret()
  print('I have generated a 4-digit number with unique digits. Try to guess it!')

  while True:
    guess = input('Guess: ')
    if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
      cows, bulls = calculate_cows_and_bulls(secret, guess)
      print(f'{cows} cows, {bulls} bulls')

      if bulls == 4:
        print('Congratulations! You guessed the correct number')
        break
    else:
      print('Invalid guess. Please enter a 4-digit number with unique digits.')
      

if __name__ == '__main__':
  main()