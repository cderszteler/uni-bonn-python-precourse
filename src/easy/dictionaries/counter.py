# 1+1+1+1...+1+1 (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/dictionaries/004/)
from collections import Counter
from functools import reduce

a = [
  'For-Schleifen', 'For-Schleifen', 'Print', 'Klassen', 'For-Schleifen',
  'For-Schleifen', 'Strings', 'Print', 'Remove', 'Print', 'Print',
  'For-Schleifen', 'Print', 'Print', 'Klassen', 'Print', 'Klassen', 'Print',
  'Strings', 'For-Schleifen', 'For-Schleifen', 'Print', 'For-Schleifen',
  'Print', 'For-Schleifen', 'Strings', 'Print', 'For-Schleifen',
  'For-Schleifen', 'Klassen', 'For-Schleifen', 'Print', 'Klassen',
  'For-Schleifen', 'Print', 'Print', 'Klassen', 'Strings', 'Klassen', 'Strings',
  'Print', 'Print', 'Strings', 'Strings', 'Print', 'Print', 'Print', 'Print',
  'Print', 'Klassen', 'Klassen', 'Klassen', 'For-Schleifen', 'For-Schleifen',
  'Strings', 'Klassen', 'For-Schleifen', 'Print', 'For-Schleifen', 'Print',
  'Strings', 'Print', 'For-Schleifen', 'Print', 'Print', 'Print', 'Klassen',
  'Print', 'For-Schleifen'
]

b = [
  'Print', 'For-Schleifen', 'Strings', 'Klassen', 'Strings', 'For-Schleifen',
  'Strings', 'For-Schleifen', 'Strings', 'Print', 'Strings', 'For-Schleifen',
  'Print', 'For-Schleifen', 'Strings', 'Klassen', 'For-Schleifen', 'Strings',
  'Klassen', 'Print', 'Print', 'Remove', 'Strings', 'For-Schleifen',
  'Strings', 'Strings', 'Strings'
]

if __name__ == '__main__':
  counter = Counter(a)
  print(counter)
  print(max(set(a), key=a.count))
  print(reduce(lambda one, two: one + two, counter.values()))
  print(counter - Counter(b))
