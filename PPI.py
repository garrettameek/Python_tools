import os, re, csv, scipy, itertools
import math, numpy as np, pandas as pd
from scipy.spatial import distance
from itertools import combinations
from pdb_editing import *

# This function returns the amino acid type
def amino_acid_type(amino_acid):
 hydrophobic = ['ALA','ILE','LEU','MET','PHE','VAL','PRO','GLY']
 polar = ['GLN','ASN','HIS','SER','THR','TYR','CYS','TRP']
 charged = ['ARG','LYS','ASP','GLU']
 if amino_acid in hydrophobic: aa_type='hydrophobic'
 if amino_acid in polar: aa_type='polar'
 if amino_acid in charged: aa_type='charged'
 return(aa_type)

# This function returns the distance between two atoms
def dist(coor_a,coor_b):
 r = math.sqrt((coor_a[0]-coor_b[0])**2.0 + (coor_a[1]-coor_b[1])**2.0 + (coor_a[2]-coor_b[2])**2.0)
 return(r)



# This function outputs a list of residue contacts within
# the user-specified 'distance'
def residue_contacts(coordinates,distance,file):
 contact_file_obj = open(file.replace('.pdb','.contacts'),"w") 
 contact_list = pd.DataFrame(columns=['chain_1','atom1_id','chain_2','atom2_id','distance'])
# Iterate over atomic coordinates twice to get the distances between all atoms,
# add new residue IDs to a list of residue-residue contacts if currently missing,
# replace the distance in the current contact list with new data, which has shorter distance,
 for atom_1,atom_2 in combinations(coordinates,2):
# We're turning each line of atomic coordinate info into a pandas dataframe for column-based manipulation,
# since the PDB follows column-based formatting rules.
  atom_1_df = pd.DataFrame(data=[list(atom_1)])
  atom_2_df = pd.DataFrame(data=[list(atom_2)])
  if all(atom_1_df.iloc[0,23:26] != atom_2_df.iloc[0,23:26]):
     atom_1_coord = list([float("".join(atom_1_df.iloc[0,30:38])),float("".join(atom_1_df.iloc[0,39:47])),float("".join(atom_1_df.iloc[0,48:56]))])
     atom_2_coord = list([float("".join(atom_2_df.iloc[0,30:38])),float("".join(atom_2_df.iloc[0,39:47])),float("".join(atom_2_df.iloc[0,48:56]))])
     atom_dist = dist(atom_1_coord,atom_2_coord)
     skip = False
     
#    distance is a user-input variable in the calling function
     if atom_dist <= distance:
# check to see if this (residue-residue) contact is in the list,
      for contact_1 in contact_list['atom1_id']:
       if contact_1 == atom_1_df.iloc[0,23:26]:
#  if 'yes', is the listed distance larger?
#   if 'yes' then replace with this new contact distance
         if all(atom_1_df.iloc[0,21],"".join(atom_1_df.iloc[0,23:26]),atom_2_df.iloc[0,21],"".join(atom_2_df.iloc[0,23:26])) in line:
#        if line[4] > format(res_dist,'.4'):
#         line = [res_1_df.iloc[0,21],"".join(res_1_df.iloc[0,23:26]),res_2_df.iloc[0,21],"".join(res_2_df.iloc[0,23:26]),format(res_dist,'.4')])
#         skip = True
#         break
#      if not skip: 
#       contact_list.append([res_1_df.iloc[0,21],"".join(res_1_df.iloc[0,23:26]),res_2_df.iloc[0,21],"".join(res_2_df.iloc[0,23:26]),format(distance,'.4')])
#       print([res_1_df.iloc[0,21],"".join(res_1_df.iloc[0,23:26]),res_2_df.iloc[0,21],"".join(res_2_df.iloc[0,23:26]),format(distance,'.4')])
 contact_file_obj.close()
 return
# return(contact_list)

#

# Begin main code
for file in os.listdir():
# Get pdb files
 if ".pdb" in file and '_fixed' not in file:
  chain_list = []
  distance = 8.0
  if "1bg8" in file: chain_list = ['A','B']
  read_file_obj = open(file,"r")
  text=read_file_obj.readlines()
  coordinates = renumber(chain_list,text)
  atomic_coords = get_atomic_coords(file,chain_list,coordinates)
#  ca_coords = get_calpha_coords(file,chain_list,atomic_coords)
# finished until here

# testing here
  residue_contacts = residue_contacts(atomic_coords,distance,file)

#  ppi_ca_contacts = ppi_ca_contacts(ca_coords,distance,file)
#  sa_residues = solvent_accessible_residue_list(atomic_coords,distance,file)
#  sa_residue_types = solvent_accessible_analysis(sa_residues,file)
#  ppi_contact_types = ppi_contact_analysis(ppi_ca_contacts,file)
  
#  read_file_obj.close()

    