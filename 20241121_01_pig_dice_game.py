import random 

def roll_die():
  return random.randint(1, 6)

def play_turn(player_name):
  turn_score = 0

  print(f"\n{player_name}'s turn")

  while True:
    roll = roll_die()
    print(f'You rolled a {roll}')

    if roll == 1:
      return 0
    
    turn_score += roll
    choice = input('Roll again? (y/n): ').lower()
    if choice != 'y':
      return turn_score


def main():
  scores = [0, 0]
  current_player = 0 

  while True:
    player_name = f'Player {current_player + 1}'
    turn_score = play_turn(player_name)
    scores[current_player] += turn_score

    print(f'\nYou scored {turn_score} points this turn.')
    print(f'Current scores: Player 1: {scores[0]}, Player 2: {scores[1]}')

    if scores[current_player] >= 100:
      print(f'{player_name} wins!')
      break

    current_player = 1 if current_player == 0 else 0

if __name__ == '__main__':
  main()
  

# 이 프로그램은 2명의 플레이어가 주사위를 굴려 나온 점수를 더해 100점이 먼저 나오면 이기는 게임 같습니다.
# 주사위는 계속 굴릴 수 있지만 1점이 나오면 그 턴의 점수는 모두 잃게 됩니다.
# current_player = 1 if current_player == 0 else 0 >> 이 프로그램에서 배울만한 코드다. 삼항연산자라고한다. 자세히 알아보자
#  - 이 코드는 이 프로그램에서 플레이어를 전환하는 역할을 한다.
#  - current_player 가 1이면 0이 되고 0이 되면 1이 되면서 1,2 번 플레이어가 바뀐다.