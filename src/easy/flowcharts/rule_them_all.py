# One Flowchart to rule them all (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/flowcharts/006/)
if __name__ == '__main__':
  race = input('Which race? ')
  if race == 'Elves':
    print('Three were given to the Elves')
  elif race == 'Dwarves':
    print('Seven to the Dwarf-Lords')
  elif race == 'Men':
    print('Nine rings were gifted to the race of men')
  else:
    print('Three were given to the Elves, immortal, wisest and fairest of all beings.'
          'Seven to the Dwarf-Lords, great miners and craftsmen of the mountain halls.'
          'And nine, nine rings were gifted to the race of men, who above all else desire power.')
