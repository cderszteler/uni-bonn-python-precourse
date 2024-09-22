# Und Sie dachten Sie seien fertig (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/klassen/004/)
from enum import Enum


class BestePokemon(Enum):
  PIKACHU = 1
  GLUMANDA = 2
  SHIGGY = 3
  BISASAM = 4

def task_one() -> None:
  print(BestePokemon(1)) # BestePokemon.PIKACHU
  print(BestePokemon.BISASAM.name) # BISASAM
  print(BestePokemon.BISASAM.value) # 4

  print(BestePokemon.PIKACHU.value == 1) # True

  shiggy = BestePokemon.SHIGGY
  print(shiggy == BestePokemon.SHIGGY) # True


class Position(Enum):
  Left = 0
  Middle = 1
  Right = 2

# Task 3 is skipped, because of the same reasons that some tasks in `improve.py`
# were skipped. See README.md for more information.

if __name__ == '__main__':
  task_one()