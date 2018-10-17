""" 
  ======================================
    Structure : 

    Debugging at the moment.
  ======================================
"""

import os

from src.core.classes.Reader import Reader
from src.core.classes.Generator import Generator
from pprint import pprint

def structure(name = "app", lang = "python"):
  reader = Reader()
  generator = Generator()
  
  app = reader.read(file = f"{lang}.yaml")
  pprint(app)
  for x in app:
    if f"{lang}" in x:
      generator.generate(what = f"structure", name = f"{name}", src = x[f"{lang}"]["structure"])

if __name__ == '__main__':
  structure(name = "app", lang = "python")