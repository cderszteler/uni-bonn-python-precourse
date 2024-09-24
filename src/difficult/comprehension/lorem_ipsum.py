# Dict-Comprehension (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-500/comprehension/002/)
import collections

lorem = (
  "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
  "sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,"
  " sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum."
  " Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
)
if __name__ == '__main__':
  lorem = lorem.replace(' ', '')
  print({char: lorem.count(char) for char in set([char for char in lorem])})
  # pythonic way:
  print(collections.Counter(lorem))