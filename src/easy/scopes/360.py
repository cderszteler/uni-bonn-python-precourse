# 360 no-scope? (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/scopes/001/)
fakt = "Portal ist ein super Spiel"

def coole_funktion():
  print(fakt)

def doofe_funktion():
  fakt = "Portal ist ein blödes Spiel!!!"
  print(fakt)

def komische_funktion():
  print(fakt)

def witzige_funktion():
  fakt2 = "Portal 3 wann?"


# noinspection NonAsciiCharacters,PyUnresolvedReferences
def verdächtige_funktion():
  print(fakt2)

def main():
  doofe_funktion()
  coole_funktion()
  komische_funktion()
  witzige_funktion()
  try:
    verdächtige_funktion()
  except:
    print("Das ist nicht erlaubt!")

if __name__ == "__main__":
  main()

# Order:
# Portal ist ein blödes Spiel!!!
# Portal ist ein super Spiel
# Portal ist ein super Spiel
# Das ist nicht erlaubt!