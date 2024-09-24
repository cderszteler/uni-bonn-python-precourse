# Dict-Comprehension 3 (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-500/comprehension/004/)
if __name__ == '__main__':
  words = ['Ball', 'Feather', 'Control']
  count = {word: {char: word.count(char) for char in set([char for char in word])} for word in words}
  print(count)