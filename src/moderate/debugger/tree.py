# Ist doch alles richtig, oder? (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/debugger/002/)
# Apples: 1, Blossoms: 3 (total: 4)
baum = {
  "wurzel": {
    "zweig1": {"bluete": "*"},
    "zweig2": {
      "zweig1": {"bluete": "*"},
      "zweig2": {"apfel": "o"}
    },
    "zweig3": {},
    "zweig4": {"bluete": "*"}
  }
}

def count_apples_and_blossoms(tree):
  count = 0
  for key, value in tree.items():
    if key == "bluete" or key == "apfel":
      count += 1
    elif key == "wurzel" or key.startswith("zweig"):
      count += count_apples_and_blossoms(value)
  return count


def main():
  print(count_apples_and_blossoms(baum))

if __name__ == "__main__":
  main()
