# Gotta Catch'em all! (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/dictionaries/003/)
if __name__ == '__main__':
  pokemon = {"feuer": "Glumanda", "wasser": "Shiggy", "pflanze": "Bisasam"}
  for key in pokemon.keys():
    print(key)
  for value in pokemon.values():
    print(value)
  for key, value in pokemon.items():
    print(f'{key}, {value}')

  mehr_pokemon = {"elektro": "Pikachu", "geist": "Gengar", "stein": "Kleinstein"}
  for key, value in mehr_pokemon.items():
    pokemon[key] = value

  for key, value in pokemon.items():
    pokemon[key] = [value]

  mehr_pokemon = {'elektro': 'Joel', 'stein': 'Leander', 'pflanze': 'Chriss'}
  for key, value in mehr_pokemon.items():
    pokemon[key] = pokemon[key] + [value]

  print(pokemon)