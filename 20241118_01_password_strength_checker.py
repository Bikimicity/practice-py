import re

def check_password_strength(password):
  strength = 0 

  if len(password) >= 8:
    strength += 1
  if re.search('[a-z]', password):
    strength += 1
  if re.search('[A-Z]', password):
    strength += 1
  if re.search('[0-9]', password):
    strength += 1
  if re.search('[@#$%+=!]', password):
    strength += 1

  return strength
  

def main():
  password = input('Enter a password: ')
  strength = check_password_strength(password)

  if strength == 5:
    print('Password strength: Very Strong')
  elif strength == 4:
    print('Password strength: Strong')
  elif strength == 3:
    print('Password strength: Medium')
  elif strength == 2:
    print('Password strength: Weak')
  else:
    print('Password strength: Very Weak')


if __name__ == '__main__':
  main()
  
# 이 프로그램은 사용자의 비밀번호가 안전한지 확인하는 프로그램인 것 같다.
# 프로그램은 사용자에게 패스워드를 입력받고
# 길이가 8자 이상, 소문자, 대문자, 숫자, 특수문자가 포함 될 수록 1점씩 추가해서 최종 5점을 받으면 매우 훌륭한 비밀번호라는 것을 알려준다.