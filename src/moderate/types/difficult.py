# Mehr Happy Cyber-Chris noises (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/type-hinting/003/)
# Fehlermeldungen für den Nutzer
message_1: str = "Das Passwort ist zu kurz!"
message_2: str = "Das Passwort muss min. 3 Buchstaben enthalten!"
message_3: str = "Das Passwort muss min. 2 Zahlen enthalten!"
message_4: str = "Das Passwort benötigt min. 1 Sonderzeichen!"

# Alle Zahlen, Buchstaben und Sonderzeichen auf der Welt hust hust
numbers: tuple[int, int, int, int] = (3, 9, 4, 2)
characters: dict[str, tuple[str, ...]] = {
  "letters": ('W', 'h', 'e', 'a', 't', 'l', 'e', 'y'),
  "special": ('!', '?', '-', '@')}


# Diese Funktion nimmt ein Passwort, bestehend aus einem String und prüft, ob dieses Passwort sicher ist.
def naive_password_check(password: str) -> bool:
  password_length: int = len(password)
  if password_length < 8:
    print(message_1)
    return False

  if character_counter(password, characters["letters"]) < 3:
    print(message_2)
    return False

  if number_counter(password) < 2:
    print(message_3)
    return False

  if character_counter(password, characters["special"]) < 1:
    print(message_4)
    return False

  return True


# Helferfunktionen
# noinspection PyShadowingNames
def character_counter(password: str, characters: tuple[str, ...]) -> int:
  i: int = 0
  for char in password:
    if char in characters:
      i = i + 1
  return i


def number_counter(password: str) -> int:
  i: int = 0
  for char in password:
    # noinspection PyBroadException
    try:
      if int(char) in numbers:
        i = i + 1
    except:
      continue
  return i


def main() -> int:
  if naive_password_check("Wheatley!42"):
    print("Stein starkes Passwort!")
  return 0


if __name__ == "__main__":
  main()
