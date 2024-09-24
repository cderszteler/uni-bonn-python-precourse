# List-Comprehension (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-500/comprehension/001/)
if __name__ == '__main__':
  print([[(1 if (number == 2 or line == 2) else 0) for number in range(5)] for line in range(5)])