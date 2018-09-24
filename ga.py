####
###
### BASIC GENETIC ALGORITHM FOR PARAMETER SET MINIMIZATION
###  
### WRITTEN BY GARRETT A. MEEK, COMPLETED ON MAY 10, 2017
###
####
import math, random, copy, sys, numpy # IMPORT MODULES FOR GA
from ga_fitness import calc_fitness # IMPORT FITNESS FUNCTION FOR THIS EXAMPLE

####
###
### VARIABLES
###
####
#example_genome = [random.uniform(-20.0,20.0),random.uniform(-20.0,20.0),random.uniform(-20.0,20.0)] # List used for initial population
# can also read genome in from file
pop=100 # Size of the population (must be integer multiple of 2)
fitness_data='fitness.dat' # Fitness values for each generation written here
fitness_file=open(fitness_data, 'w')
fitness_file.write('Generation Fitness\n')
convergence=1.0e-6 # The genetic algorithm stops when the fitness changes 
# by less than 0.1% in a generation
total_genes=3 #
crossover_events=2 # Number of gene exchanges for selected parents
mutations=1 # Number of mutations (Gaussian-distributed randoms,
# with peak in distribution for the current gene value)
mutation_bound=0.5 # Standard deviation for mutation value distribution
parents_per_generation=10 # must be integer multiple of 2
maximum_generations=10000

####
###
### DEFINE INITIAL GENOME AND POPULATION
###
####

#print "Initializing population..."
## Read initial genome provided by the user
init_pop=[[0 for i in range(total_genes)] for j in range(pop)]
offspring=[[0 for i in range(total_genes)] for j in range(pop)]
pool=[[0 for i in range(total_genes)] for j in range(pop)]
# Make "pop" copies of initial genome
for i in range(pop):
 init_pop[i]=[random.uniform(-20.0,20.0),random.uniform(-20.0,20.0),random.uniform(-20.0,20.0)]
 random.shuffle( init_pop[i] )
#random.seed()

###
##
## BEGIN GENETIC ALGORITHM (RUN UNTIL CONVERGENCE)
##
###

#print "Begin genetic algorithm..."

offspring=init_pop # "offspring" is an array containing
# the genomes of the previous generation
last_fitness=0.001 # Fitness of last generation
change=1.0 # Change in fitness from last generation
generation=1
while change > convergence and generation <= maximum_generations:
 print "Generation ",generation
# pool contains genomes of current generation
 pool=offspring

###
##
## STEP 1: EVALUATE FITNESS
##
###

# print "Calculating fitness"
 fitness = [0.0 for i in range(pop)]
 for i in range(pop):
  fitness[i]=round(calc_fitness( pool[i] ),4)

###
##
## STEP 2: SELECTION (CHOOSE "FITTEST" MEMBERS OF PREVIOUS POPULATION)
##
###

# print "Selecting best members"

# parent_indices[] contains the integer indices of the two selected
# genomes (parents of next generation)
# parent_fitness[] contains the (float) parent fitness values
# parent_genome[] contains the parent gene values (vectors)
 parent_indices = [0 for i in range(parents_per_generation)]
 parent_fitness = [0.0 for i in range(parents_per_generation)]
 parent_genome = [[0.0 for i in range(parents_per_generation)] for i in range(parents_per_generation)]

 for i in range(pop):
  if (i != any(parent_indices)) or (fitness[i] > any(parent_fitness)):
   for j in range(parents_per_generation):
    if fitness[i] > parent_fitness[j]:
     parent_fitness[j]=fitness[i]
     parent_indices[j] = i
     parent_genome[j] = pool[i][:]
 print parent_fitness

###
##
## STEP 3: CROSSOVER (RANDOMLY EXCHANGE GENE(S) AMONG PARENTS)
##
###

# print "Performing gene crossover"

 i=1
 while i <= crossover_events:
  crossover_gene=range(random.randint(0,total_genes-1),total_genes)
#  print "crossover gene =",crossover_gene
  for j in crossover_gene:
   k=0
   while k <= (parents_per_generation-1):
    parent_genome[k][j], parent_genome[k+1][j] = parent_genome[k+1][j], parent_genome[k][j]
    k=k+2
  i=i+1

###
##
## STEP 4: MUTATION (RANDOMLY MUTATE GENES OF NEW GENERATION)
##
###

# print "Mutating offspring sequences"
## Create the new generation
 offspring=[[0.0 for i in range(total_genes)] for j in range(pop)]
 for i in range(0,pop):
  offspring[i]=parent_genome[random.randint(0,parents_per_generation-1)]

# print "Before mutation, member",i
 j=1
 while j <= mutations:
  for i in range(pop):
   mutation_gene=random.randint(0,total_genes-1)
#   print "member=",i
#   print "mutated gene index=",mutation_gene
## Mutation is chosen from a Gaussian distribution of pure gene values
## with a standard devation of "mutation_bound"
   pure_gene=offspring[i][mutation_gene]
#   print "pure gene value=",offspring[i][mutation_gene]
   mutation=round(random.gauss(pure_gene,mutation_bound),4)
#   print "mutated gene value=",mutation
   offspring[i][mutation_gene] , mutation = mutation, offspring[i][mutation_gene]
  j=j+1
 if generation == 1:
  for i in range(pop):
   print "member",i,"=",offspring[i]

# Calculate fitness of current generation
# (There are other sensible ways to do this)
 current_fitness=numpy.mean(parent_fitness)
# Fitness change from last generation
 change=abs((current_fitness-last_fitness)/last_fitness)
# Write fitness to "fitness_file"
 fitness_file.write('%i %f\n' % (generation,current_fitness))

# Bookkeeping
 last_fitness=current_fitness
 generation=generation+1
###
##
## ITERATE
##
###

fitness_file.close()
print "\n"
print "GENETIC ALGORITHM COMPLETE\n"
print "\n"
print "CHANGE IN FITNESS FOR LAST TWO GENERATIONS WAS ",change,"\n"
print "\n"
print "ALGORITHM REQUIRED ",generation," GENERATIONS\n"

# We can write the best genome to a file:
# best_genome_file=open(best_genome_file, "w")
# for i in range( total_genes ):
#  best_genome_file.write('%f\n' % parent_genome[0])

# Or print it here

print "THE BEST GENOME IS SHOWN BELOW:\n"
print "\n"
print parent_genome[0]


###
##
## END OF GENETIC ALGORITHM
##
###

sys.exit()
