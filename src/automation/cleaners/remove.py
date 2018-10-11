import os
import shutil
import glob

from src.core.classes.Reader import Reader

def remove():
  reader = Reader()
  targets = reader.read(file = "remove.yaml")
  targets = targets[0]["remove"]

  if os.path.exists(f"{os.getcwd()}"):
    for path, folders, files in os.walk(f"{os.getcwd()}"):
      """ 
        ======================================
          Remove files or folders if they exist
          in remove.yaml file : which is supposed
          to be a list of stuff that you want to 
          remove from everywhere, such as : 
          __pycache__ or other garbage that's produced.
        ======================================
      """
      for folder in folders:
        if folder in targets:
          if os.path.exists(f"{os.path.join(path, folder)}"):
              shutil.rmtree(f"{os.path.join(path, folder)}")

      for file in files:
        if file in targets:
          if os.path.exists(f"{os.path.join(path, file)}"):
            os.remove(f"{os.path.join(path, file)}")
          

# <---------------------------->

if __name__ == '__main__':
  remove()