class Generator(object):
  """
  Description:
  
  Instance of this class will generate
  various stuff depending on the requirements,
  as of right now, it can generate : 

  - Directory Structure (with empty files)
    
  """
  def __init__(self):
    super(Generator, self).__init__()

  def generate(self, what = "structure", src = "", name = ""):
    """  
    -------------------------------------
  
      Interface for various generating
      functions described here or maybe in
      other files.
  
    -------------------------------------
  
      args => None
      kwargs => what, src
      
    -------------------------------------  
    """
    if (src != "") and (name != "") and (what == "structure"):
      self.structure(src)

  # <---------------------------->
  
  def structure(self, yaml):
    """  
    -------------------------------------
  
      Generates directory structure with
      emptry files depending on the YAML
      based directory structure that it 
      gets. 

      All keys in yaml are directories
      and all array elements are files.
  
    -------------------------------------
  
      args => yaml
      kwargs => None
      
    -------------------------------------  
    """
    pass