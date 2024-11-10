# 이 프로그램은 랜덤 비밀번호를 생성하는 프로그램입니다.

import string 
import random

def generate_password(length, include_uppercase, include_numbers, include_special):
    if length < (include_uppercase + include_numbers + include_special):
        raise ValueError('Password length is too short for the specified criteria.')

    password = ''   
    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_numbers:
        password += random.choice(string.digits)
    if include_special:
        password += random.choice(string.punctuation) 
        
    # Fill the remaining length with any allowed characters
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    for _ in range(length - len(password)):
        password += random.choice(characters) 
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)


def main():
    length = int(input('Enter password length: '))
    include_uppercase = input('Include uppercase letters? (y/n): ').lower() == 'y'
    include_numbers = input('Include numbers? (y/n): ').lower() == 'y'
    include_special = input('Include special characters? (y/n): ').lower() == 'y'
    try:
        password = generate_password(length, include_uppercase, include_numbers, include_special)
        print(password)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    """
    1. 사용자에게 설정할 비밀번호 자릿 수를 숫자로 입력 받습니다.
    2. 사용자에게 대문자, 숫자, 특수문자를 넣을 건지 y / n로 물어봅니다.
    3. if = True 를 만족하는 조건문을 실행시켜 password 변수에 담습니다.
    4. 변수에는 한 자리씩 담기므로 나머지 비밀번호를 채워야합니다.
    5. characters 에 소문자 전체를 담습니다.
    6. 마찬가지로 사용자에게 입력받은 y / n정보로 characters 변수에 대문자, 숫자, 특수문자들을 전부 담습니다.
    6-1. 사용자가 전부 y를 선택했다면 characters = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 최종적으로 이렇게 됩니다.
    7. 반복문의 동작원리는 처음 설정한 비밀번호 자릿 수에서 password에 담긴 문자 길이만큼 빼서 반복문을 돌립니다.
    8. 반복해서 나온 문자를 password 변수 뒤에 차례차례 입력시키고 랜덤으로 섞고 join() 함수를 통해 문자를 합쳐 최종적으로 원하는 길이 만큼 결과가 나옵니다. 
    """
    main()