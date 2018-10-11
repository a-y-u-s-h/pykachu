# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| #
# |~~~~~~\|/~~~~~~\|/~~~~~~\|/~~~~~~\|/~~~~~~\|/~~~~~~\|/~~~~~~\|/~~~~~~~| #
# |                                                                      | #
# |                                                                      | #
# |                     Author  : Ayush Sharma                           | #
# |                     Github  : a-y-u-s-h                              | #
# |                     Website : ayushsharma.net                        | #
# |                     Twitter : @taggosaurus                           | #
# |                                                                      | #
# |                                                                      | #
# |~~~~~~/|\~~~~~~/|\~~~~~~/|\~~~~~~/|\~~~~~~/|\~~~~~~/|\~~~~~~/|\~~~~~~~| #
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| #

import sys

from src.automation.cleaners.remove import remove
from src.core.scripts.structure import structure

""" 
  ========================================================
    
    Command Line Interface to handle various aspects 
    for this project depending on data stored in 'data'.
    Some features that are implemented till now are : 

    - Cleaning up unnecessary folders like __pycache__
    - Creating directory structure

  ========================================================
"""


def main():
  if "--remove" in sys.argv:
    remove()
  
  elif ("use" in sys.argv) and (len(sys.argv) > sys.argv.index("use") + 1):
    project = sys.argv[sys.argv.index("use") + 1]
    structure(project)

if __name__ == '__main__':
  main()