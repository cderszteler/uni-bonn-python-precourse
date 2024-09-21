# Was passiert hier? (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/kommentare/001/)

def eine_funktion(zahl):
  """
  Diese Funktion quadriert die gegebene Zahl und gibt diese zurück.
  :param zahl: Die zu quadrierende Zahl
  :return: Die quadrierte Zahl
  """
  neue_zahl = zahl * zahl
  return neue_zahl

def eine_weitere_funktion(zahl):
  """
  Diese Methode berechnet eine neue Zahl anhand des Eingabeparameters,
  indem diese Zahl mit 1 addiert und danach mit 2 multipliziert wird.
  Aus 3 wird so bspw. 8
  :param zahl: Die zu berechnende Zahl
  :return: Die berechnete Zahl
  """
  zahl += 1
  neue_zahl = zahl * 2
  return neue_zahl

def eine_weiterere_funktion(zahl):
  """
  Diese Methode berechnet die 3. Potenz der angegebenen Zahl und gibt diese zurück.
  :param zahl: Die Zahl, von der die 3. Potenz berechnet werden soll
  :return: Die 3. Potenz der angegebenen Zahl
  """
  i = 3
  neue_zahl = 1
  while i > 0:
    neue_zahl = neue_zahl * zahl
    i = i - 1
  return neue_zahl

def noch_eine_funktion(natuerliche_zahl):
  """
  Diese Methode berechnet die n.-Fakultät der angegebenen, natürlichen Zahl.
  :param natuerliche_zahl: Das n, von der die n.-Fakultät berechnet werden soll
  :return: Die berechnete n.-Fakultät
  """
  neue_zahl = 1
  i = natuerliche_zahl
  while i > 0:
    neue_zahl = neue_zahl * i
    i = i - 1
  return neue_zahl

def noch_eine_weitere_funktion(zahl):
  """
  Diese Methode berechnet den absoluten Wert der angegebenen Zahl
  :param zahl: Die Zahl, von der der absolute Wert berechnet werden soll.
  :return: Der absolute Wert des angegebenen Parameters.
  """
  if zahl < 0:
    neue_zahl = zahl * (-1)
  else:
    neue_zahl = zahl
  return neue_zahl
