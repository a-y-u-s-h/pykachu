""" 
  ======================================
    Structure : 

    Debugging at the moment.
  ======================================
"""

from src.core.classes.Reader import Reader
from pprint import pprint

def structure(name = "app"):
  reader = Reader()
  app = reader.read(file = "structure.yaml")
  pprint(app)


if __name__ == '__main__':
  structure()