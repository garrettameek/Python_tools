def calc_fitness( genes ):
###
##
## Calculates fitness of "genes", passed from genetic algorithm in "ga.py"
##
###

 fitness=0.9999
#fitness=exp(-(1.0/calc_zscore(genes))

 return fitness

def calc_zscore():
###
##
## This subroutine calculates the Z-score of a structural ensemble, as follows:
##
## V(native,eps) = Free energy of the native ensemble 
##   with the current value of epsilon (eps)
##
## <V(non-native,eps)> = Mean free energy of the non-native ensemble
##
## Z = ( V(native,eps) - <V(non-native,eps)> ) / ( SQRT( <V(non-native,eps)^2> - <V(non-native,eps)>^2 ) )
##
## A low Z-score suggests we can use this parameter set
## to distinguish native and non-native poses in molecular
## simulations.
##
###

##
#
# Ensemble variables
#
##
 nonnative_ens_size=100
 native_pdb = "/home/gameek/ensembles/test/GO.pdb"

##
#
# Load the native structure and non-native ensemble coordinates
#
##
 native=[]
 native = readPDB(native_pdb)

 nonnative=[]
 i=1
 while (i <= nonnative_ens_size):
  coor = ()
  unbound.append( coor.readPDB(i) )
  i=i+1
  break

##
#
# Calculate the energies and standard deviation (denominator of Z-score)
#
##

#  V_native=
