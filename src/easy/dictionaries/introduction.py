# Warm werden mit Dictionaries (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/dictionaries/001/)
if __name__ == '__main__':
  # noinspection PyDictCreation
  adjectives = {'a': 'awesome', 'c': 'cyber'}
  adjectives['b'] = 'bombastic'

  print(adjectives['a'])
  print(f'Ich bin {adjectives['a']}, du bist {adjectives['b']}, zusammen sind wir {adjectives['c']}!')

  print("a" in adjectives) # Tests whether key exists in dict.

  x = adjectives.get("a") # Returns value for key in dict or 'None' if not found
  print(x)

  y = adjectives.get("z", 42) # Returns value for key in dict or 42 as fallback if not found
  print(y)

  keys = list(adjectives.keys()) # Lists keys in dict.
  print(keys)

  vals = list(adjectives.values()) # Lists values in dict.
  print(vals)

  items = list(adjectives.items()) # Lists (key,value) pairs in dict.
  print(items)

  print(max(adjectives)) # Returns "max" key in dict (here: c, because a < b < c in sorting)

  del adjectives["a"] # Deletes entry with key 'a' in dict.
  print(adjectives)