# Malen in Python (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/for-loops/006/)
import math

if __name__ == '__main__':
  length = 10
  for line in range(length):
    print(str(line) + ": " +
      "O " * min(line, length - (line + 1))
      + "X "
      + "O " * max(0, length - 2 * (min(line + 1, length - line)))
      + "X " * (0 if line == math.floor(length / 2) and length % 2 != 0 else 1)
      + "O " * min(line, length - (line + 1))
    )
