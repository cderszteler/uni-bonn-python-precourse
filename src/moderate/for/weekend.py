# Wochenende am See (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/for-loops/002/)
import pprint
from collections import Counter

if __name__ == '__main__':
  alice = ['Bananen ', 'Brot', 'Schokolade ', 'Rotwein ']
  bob = ['Bier', 'Bier', 'Chips ']
  eve = ['Brot', 'Schokolade ', 'Chips ', 'Bier', 'Wasser ']
  combined = alice + bob + eve
  pprint.pprint(Counter(combined))