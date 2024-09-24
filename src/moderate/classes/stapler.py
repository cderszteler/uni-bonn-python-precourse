# Catch the Python (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/classes/002/)
class Stapler:
  def __init__(self, initial_papers):
    self.papers = initial_papers

  def staple_in(self, paper):
    """Adds a paper to the papers list."""
    self.papers.append(paper)

  def staple_out(self):
    """Removes the last paper from the papers list."""
    return self.papers.pop()

  def list_papers(self):
    """Lists all papers in the paper list."""
    for paper in self.papers:
      print(paper)

def main():
  papers = ["Blatt 1", "Blatt 2"]
  stapler = Stapler(papers)
  stapler.staple_out()
  stapler.staple_in("Neues Blatt")
  stapler.list_papers()

if __name__ == "__main__":
  main()