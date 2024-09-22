# Number on my list (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/listen/001/)
if __name__ == '__main__':
  # noinspection PyListCreation
  a = [2, 4, 6, 8, 10]

  a.append(42)
  print(a[-1])
  print(a[:3])
  print(a[2:4])
  print(a[-4:])

  print ([2, 2, 2, 4].count(2)) # Counts '2' in list
  print("Hallo".count('l')) # Counts 'l' in list
  print(a.index(8)) # Returns index of element '8' in list 'a'
  print(min(a)) # Returns smallest element in 'a'
  print(max(a)) # Returns largest element in 'a'
  del a[2] # Deletes element in 'a' at index 2 (here: 6)
  print(a)
  a.reverse() # Reverses list (internally, i.e. does not return an altered list)
  print(a)