# Das Geheimnis des Caesars (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/strings/001/)
a_char = 97
z_char = 123

def encrypt(raw: str, places: int) -> str:
  if not 0 < places < 26:
    raise ValueError(f'`places` must be between 0 (a) and 26 (z)')
  characters = [ord(character) for character in raw]
  for index in range(len(characters)):
    character = characters[index]
    offset = places if character + places <= z_char else places - 26
    characters[index] = characters[index] + offset
  return ''.join([chr(character) for character in characters]).upper()

def decrypt(encrypted: str, places: int) -> str:
  if not 0 < places < 26:
    raise ValueError(f'`places` must be between 0 (a) and 26 (z)')
  characters = [ord(character) for character in encrypted.lower()]
  for index in range(len(characters)):
    character = characters[index]
    offset = places if character - places >= a_char else places - 26
    characters[index] = character - offset
  return ''.join([chr(character) for character in characters])

def main():
  test = "zoufa"
  encrypted = encrypt(test, 3)
  print(test)
  print(encrypted)
  assert decrypt(encrypted, 3) == test

if __name__ == '__main__':
  main()