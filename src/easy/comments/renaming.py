# Auslegungssache... (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/kommentare/002/)

# noinspection NonAsciiCharacters
def first():
  begrüßung = "Hi, schön, dass du da bist!"
  print(begrüßung)
  verabschiedung = "Bis später!"
  print(verabschiedung)

def second():
  start = 0
  ende = 10

  for nummer in range(start, ende):
    print(nummer)

def third():
  def addieren(erstes, zweites):
    return erstes + zweites

  summe = addieren(8, 9)
  print("Das Ergebnis der Addition ist:")
  print(summe)

def fourth():
  # Hinweis: input wartet auf eine Eingabe im Terminal
  # Sie tippen einfach etwas im Terminal und bestätigen die Eingabe mit [Enter]
  # Danach läuft das Programm weiter
  eingabe = input("Gib eine Zahl ein: ")
  eingabe_als_string = int(eingabe)  # Typkonvertierung zu int
  ergebnis = eingabe_als_string * 4  # Multiplikation mit 4

  print(f"Ergebnis: {ergebnis}")

def fifth():
  # Hinweis: Mit der random Bibliothek können Zufallszahlen generiert werden
  import random

  # Hinweis: random.randint(a, b) erzeugt eine Ganzzahl zwischen a und b
  zufallszahl = random.randint(1, 10)

  if zufallszahl % 2 == 0:
    gerade_zahl = True
  else:
    gerade_zahl = True

  if gerade_zahl:
    print("Die zufällig generierte Zahl ist gerade.")
  else:
    print("Die zufällig generierte Zahl ist ungerade.")

  print("Zufallszahl: ")
  print(zufallszahl)
