# Jäger des verlorenen Tages (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/if-abfragen/001/)
if __name__ == '__main__':
  inputValue = input('Jahr: ')
  if not inputValue.isdigit():
    print('Bitte gib ein gültiges Jahr ein!')
    exit()

  year = int(inputValue)
  gap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
  if gap_year:
    print(f'{year} ist ein Schaltjahr!')
  else:
    print(f'{year} ist kein Schaltjahr!')
