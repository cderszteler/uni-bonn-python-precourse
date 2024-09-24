# Fliesenleger des Königs (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/for-loops/001/)
def int_input_or_abort(prompt: str) -> int:
  unsafe = input(prompt)
  try:
    return int(unsafe)
  except ValueError:
    exit()

if __name__ == '__main__':
  length = int_input_or_abort('Gib die Länge des Schachbretts ein: ')
  width = int_input_or_abort('Gib die Breite des Schachbretts ein: ')
  for line in range(length):
    even_line = line % 2 == 0
    # Alternating change range between range(width) and range(1, width) to offset
    # odd/even indexes
    for index in range(0 if even_line else 1, length if even_line else length + 1):
      print('#' if (index % 2 == 0) else 'O', end='')
    print('')