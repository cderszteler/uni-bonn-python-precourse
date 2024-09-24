# Sarcastic Text Generator (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/strings/003/)
import random

def generate(raw: str, factor=50) -> str:
  if not 0 <= factor <= 100:
    print('factor must be between 0 and 100')
  sarcasm = []
  for character in raw:
    generated = random.randint(0, 100)
    sarcasm.append(character.lower() if factor <= generated else character.upper())
  return ''.join(sarcasm)

def main():
  example = 'Das ist in der Tat ein sehr merkwürdiger Satz, nicht wahr?'
  print(generate(example))
  print(generate(example, factor=0))
  print(generate(example, factor=100))

if __name__ == '__main__':
  main()