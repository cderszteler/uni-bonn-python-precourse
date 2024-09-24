# Dict-Comprehension 2 (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-500/comprehension/003/)
if __name__ == '__main__':
  print({first: {second: first*second for second in range(1, 11)} for first in range(1, 11)})