# Kleines Dictionary 1x1 (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/dictionaries/002/)
import random


# noinspection PyShadowingNames
def play_game(table: dict[int, dict[int, int]]):
  first = random.randint(1, 10)
  second = random.randint(1, 10)
  correct = table[first][second]

  result = input(f'Calcualte {first}x{second}: ')
  if not result.isdigit():
    print('Gib eine richtige Zahl ein... Probier\'s noch mal!')
  elif int(result) == correct:
    print('Mathecrack')
    return True
  else:
    print(f'Grundschuldropout (Correct: {correct})')
  return False


if __name__ == '__main__':
  table: dict[int, dict[int, int]] = {}

  for first in range(1, 11):
    values = {}
    for second in range(1, 11):
      values[second] = first * second
    table[first] = values

  score = 0
  streak = True
  while streak:
    streak = play_game(table)
    if streak:
      score += 1
  print(f'Du hast einen Score von {score} erreicht!')
