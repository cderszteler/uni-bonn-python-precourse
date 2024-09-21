# Die Idee kam mir definitiv nicht beim Einkaufen (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/funktionen/002/)
types = {
  'Glas': 10,
  'Plastik': 15,
  'Dose': 25
}

if __name__ == '__main__':
  command = ""
  deposit = 0
  while command != 'exit':
    command = input("> ")
    if command == 'exit':
      print(f'Sie kriegen {round(deposit) / 100}€ Pfand ausgezahlt!')
      break
    if command.capitalize() in types:
      deposit += types[command.capitalize()]
      print(command.capitalize())
    else:
      print(None)


