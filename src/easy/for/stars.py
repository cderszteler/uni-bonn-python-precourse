# Sterne (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/for-loops/001/)
if __name__ == '__main__':
  count = 5
  for index in range(0, count*2):
    print("* " * (index if index <= count else (count*2 - index)))