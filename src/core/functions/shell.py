import os
import shutil
import glob

def take(path):
  if not os.path.exists(f"{path}"):
    os.makedirs(f"{path}")
  os.chdir(f"{path}")

# <---------------------------->

def mkdir(path):
  if not os.path.exists(f"{path}"):
    os.makedirs(f"{path}")

# <---------------------------->
  
def touch(path):
  if not os.path.exists(f"{path}"):
    with open(f"{path}", "w") as file:
      pass

# <---------------------------->

def cd(path):
  if os.path.exists(f"{path}"):
    os.chdir(f"{path}")

# <---------------------------->