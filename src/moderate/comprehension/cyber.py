# Cyber-Comprehension-Collection (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/comprehensions/001/)

if __name__ == '__main__':
  print([i for i in range(0, 18)])
  print([i**2 for i in range(0, 18)])
  print([i for i in range(33) if i % 3 == 0])
  print([f'cyber-{items}' for items in ["cool", "toll", "nice", "klasse"]])
  print({i: i**3 for i in range(21, 33)})
  print([[0 for j in range(5)] for i in range(5)])
  print([hex(i) for i in range(7, 22)])
  print([[j for j in range(i * 4 + 1, i * 4 + 5)] for i in range(4)])