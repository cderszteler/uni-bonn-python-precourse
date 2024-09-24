# Split (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/for-loops/006/)
def split(to_split: list[int], length: int) -> list[list[int]]:
  if length <= 0:
    return [to_split, []]
  elif length >= len(to_split):
    return [[], to_split]
  return [to_split[:length], to_split[length:]]

if __name__ == '__main__':
  print(split([1, 2, 3, 4, 5, 6], 3))
  print(split([1, 2, 3, 4, 5, 6], -2))
  print(split([1, 2, 3, 4, 5, 6], 10))