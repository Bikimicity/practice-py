# 이 프로그램은 간단한 환율 변환 프로그램으로 보입니다.

def get_amount():
  """
  1. 이 함수는 무한 반복문 내에서 코드 실행 시도와 예외 처리를 합니다.
  2. 사용자에게 정보를 입력 받아 숫자가 아닌경우, 0 이거나 0 보다 작은 숫자면 오류 메세지를 띄웁니다.
  3. 정상적인 값을 받을 때까지 반복문을 실행하고 함수 밖으로 값을 반환합니다.
  """
  while True:
    try:
      amount = float(input('Enter the amount: '))
      if amount <= 0:
        raise ValueError()
      return amount
    except ValueError:
      print('Invalid amount')

def get_currency(label):
  """
  1. 이 함수는 'USD', 'EUR', 'CAD' 중에 하나를 입력 받습니다.
  2. label 인자를 받습니다. 아마 화면에 출력되겠죠
  3. 위 세개의 값을 벗어나면 오류 메세지를 띄웁니다.
  4. .upper() 메소드를 통해 소문자로 작성해도 대문자로 받아 들여지기 때문에 소문자로 입력해도 됩니다.
  5. 정상적인 값을 받을 때까지 반복문을 실행하고 함수 밖으로 값을 반환합니다.
  """
  currencies = ('USD', 'EUR', 'CAD')
  while True:
    currency = input(f'{label} currency (USD/EUR/CAD): ').upper()
    if currency not in currencies:
      print('Invalid currency')
    else:
      return currency


def convert(amount, source_currency, target_currency):
  """
  1. 환율 변환을 담당하는 함수 입니다.
  2. 이중 딕셔너리 구조를 가지고 있습니다. 통화간의 환율 비율로 보입니다.
  3. 조건문의 경우 소스와 타켓 값이 같을 시 값을 그대로 다시 반환합니다.
  4. 마지막 반환문의 [][] 이 모양은 exchange_rates 변수가 이중딕셔너리기 때문에 키에 두번 접근합니다. [첫번째 키][두번째 키]
  """
  exchange_rates = {
    'USD': { 'EUR': 0.85, 'CAD': 1.25 },
    'EUR': { 'USD': 1.18, 'CAD': 1.47 },
    'CAD': { 'USD': 0.80, 'EUR': 0.68 },
  }

  if source_currency == target_currency:
    return amount
  
  return amount * exchange_rates[source_currency][target_currency]

def main():
  """
  1. 이 프로그램의 실행을 담당합니다.
  2. get_amount() 를 실행해 반환된 그 값을 amount에 저장합니다.
  3. get_currency('Source'), get_currency('Target') 마찬가지로 각각 변수에 반환된 값을 저장합니다.
  4. convert() 함수에 위 변수들을 위치 인자로 전달하여 환율을 변환합니다.
  """
  amount = get_amount()
  source_currency = get_currency('Source')
  target_currency = get_currency('Target')
  converted_amount = convert(amount, source_currency, target_currency)
  print(f'{amount} {source_currency} is equal to {converted_amount:.2f}')


if __name__ == "__main__":
  main()