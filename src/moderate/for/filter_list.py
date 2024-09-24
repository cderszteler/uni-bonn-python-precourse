# Rausschmeißer (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/for-loops/004/)
def filter(target: list[int], value: int, remove_only_first = False) -> list[int]:
  copy = target.copy()
  for item in target:
    if item == value:
      copy.remove(item)
      if remove_only_first:
        break
  return copy


if __name__ == '__main__':
  print(filter([2, 4, 4, 6, 7], 4))
  print(filter([2, 4, 4, 6, 7], 4, remove_only_first = True))