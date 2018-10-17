import os
import shutil
import glob
import yaml

class Reader(object):
  """
  Description:
  
    Instance of this class looks inside
    data folder and fetches various kinds
    of data.
    
  """
  def __init__(self):
    super(Reader, self).__init__()
    self.root = os.path.abspath(os.getcwd())
    self.look = os.path.join(os.getcwd(), "data")
  
  def read(self, extension = "", src = ".", file = ""):
    """  
    -------------------------------------
  
      Read files that end with a particular 
      extension. A particular tree can
      be specified for search. By default it
      reads yaml files and walks recursively
      inside data folder at root of the
      project.
  
    -------------------------------------
  
      args => None
      kwargs => extension and src.
      
    -------------------------------------  
    """
    output = []

    if os.path.exists(self.root):
      os.chdir(self.root)

    if os.path.exists(self.look):
      os.chdir(self.look)
      for path, folders, files in os.walk(self.look):
        for f in files:
          """ 
            ======================================
              Read all YAML files in specified 
              source directory (else in data folder)
            ======================================
          """
          if (f == file and f.endswith(f".yaml")) or (extension != "" and f.endswith(f"{extension}")):
            content = self.readyaml(os.path.join(path, f))
            output.append({f"{f[:-5]}" : content})

    if os.path.exists(self.root):
      os.chdir(self.root)
    return output
  
  def readyaml(self, path):
    with open(f"{path}", "r") as file:
      content = yaml.load(file)
      return content