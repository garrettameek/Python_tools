# This script was produced by Garrett A. Meek
# on September 24th, 2018, and is a basic 
# CHARMM CG simulation python-wrapper.

def __init__(self):
      self.user_name = os.getlogin()
      self.host_name = socket.gethostname()
      if socket.gethostname() == 'Louie':
       if sys.platform == 'win32': self.host_base = str("D:/")
       if sys.platform == 'linux': self.host_base = str("/mnt/d/")
       self.charmm_exe=str('D:/software/R-3.4.4/bin/Rscript.exe')
#       sys.path.insert(0,str(host_base+"NTM/src"))
#       self.processors=4
      if socket.gethostname() == 'elbel':
       self.host_base = str("/mnt/g/software/")
       self.charmm_exe=str(host_base+"charmm/exec/gnu/charmm")

import os, re, csv, scipy, itertools
import math, numpy as np, pandas as pd
from scipy.spatial import distance
from itertools import combinations
from pdb_editing import *

def prep_for_charmm:
 return

def run_charmm(charmm_exe,charmm_script):

