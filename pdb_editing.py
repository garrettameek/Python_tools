# This file contains functions related to PPI.py
import pandas as pd

# This function writes coordinates in PDB format
def write_pdb(coordinates,file_name):
 file = open(file_name,'w')
 line_df = pd.DataFrame(data=[list(coordinates[0])])
 last_chain = line_df.iloc[0,21]
 for line in coordinates:
  file.write(line)
  line_df = pd.DataFrame(data=[list(line)])
  chain = line_df.iloc[0,21]
  if chain != last_chain:
   file.write('TER'+'\n')
  last_chain = chain
 file.write('TER'+'\n')
 file.write('END'+'\n')
 file.close()
 return

# This function gets atomic coordinates for chains of interest
def get_atomic_coords(file,chain_list,text):
 coordinates = []
 aa_file = file.replace('.pdb','_aa.pdb')
 for line in text:
  for chain in chain_list:
   string_list = [str(" "+chain+" "),"ATOM"]
   if all(string in line for string in string_list):
    coordinates.append(line)
 write_pdb(coordinates,aa_file)
 return(coordinates)

# This function gets calpha coordinates for chains of interest
def get_calpha_coords(file,chain_list,text):
 coordinates = []
 ca_file = file.replace('.pdb','_ca.pdb')
 for line in text:
  for chain in chain_list:
   string_list = [str(" "+chain+" "),"ATOM"," CA "]
   if all(string in line for string in string_list):
    coordinates.append(line)
 write_pdb(coordinates,ca_file)
 return(coordinates)

# This function renumbers residues
def renumber(chain_list,text):
 coordinates = []
 atom = 1
 residue = 1
 old_number = ""
 for line in text:
  for chain in chain_list:
   required_strings = [str(" "+chain+" "),"ATOM"]
   if all(string in line for string in required_strings):
# Renumber atoms
    line_df = pd.DataFrame(data=[list(line)])
    replace_df = pd.DataFrame(data=[list(format(atom,'5d'))])
    atom_column=6
    for i in replace_df.columns:
     line_df.iloc[0,atom_column] = replace_df.iloc[0,i]
     atom_column=atom_column+1
    new_line=""
    line_list=list()
    for i in line_df.columns:
     line_list.append(line_df.iloc[0,i])
    new_line=new_line.join(line_list)
    line = new_line
    new_line=""
# Renumber residues
    line_df = pd.DataFrame(data=[list(line)])
    line_list=list()
# Iterate over columns with residue ID
    for i in line_df.iloc[0,23:26]:
     line_list.append(i)
    residue_id = "".join(line_list)
    if old_number == "":
     old_number = residue_id
    else:
     if residue_id != old_number:
      residue = residue + 1
      old_number = residue_id
    replace_df = pd.DataFrame(data=[list(format(residue,'3d'))])
    res_column=23
    for i in replace_df.iloc[0,:]:
     line_df.iloc[0,res_column] = i
     res_column = res_column + 1
    line_list=list()
    for i in line_df.iloc[0,:]:
     line_list.append(i)
    new_line=new_line.join(line_list)
    atom = atom + 1
    coordinates.append(new_line)
 return(coordinates)