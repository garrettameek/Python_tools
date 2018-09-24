####
###
### BASIC GENETIC ALGORITHM (GA) FOR PARAMETER SET MINIMIZATION
###
####
import math, random, copy, sys # IMPORT MODULES FOR GA
from fitness import calc_fitness # IMPORT FITNESS FUNCTION FOR THIS EXAMPLE

####
###
### KEY VARIABLES
###
####
example_genome = [10.0,5.3,7] # List used for initial population
best_genome = [12,9,6] # Contains "fittest" genome
pop_size=10 # Size of the population
convergence=0.001 # The genetic algorithm stops when the fitness changes by less than 0.1% in a generation
total_genes=20 # Number of properties (variables) to optimize
crossover_events=1 # Number of "crossover" events for "fittest" parents per generation
mutations=1 # Number of mutations in offspring
mutation_bound=0.5 # Bound on change in genes during mutation
maximum_iterations=1000

####
###
### DEFINE INITIAL GENOME AND POPULATION
###
####
print "Initializing a population..."
## Read initial genome provided by the user
example_genome = open(example_genome_file, "r") #
sample_pop=[[0 for i in range(total_genes)],[0 for i in range(total_genes)]]
names_pop=[]
init_pop=[[0 for i in range(total_genes)],[0 for i in range(total_genes)]]
for i in example_genome:
 names_pop.append( i[0:3] )
 sample_pop[i]=float(i[4:8])
print "sample_pop=",sample_pop
#random.seed()

## Make "pop_size" copies of initial genome
for i in range( pop_size ):
 temp_pop = copy.copy( sample_pop )
## Randomly shuffle some genes for variety among members
 random.shuffle( temp_pop )
 init_pop.append( temp_pop )

###
##
## BEGIN GENETIC ALGORITHM (RUN UNTIL WE REACH CONVERGENCE)
##
###
print "Begin genetic algorithm..."

current_pop=init_pop
last_fitness=0.1
change=1.0 # Change in fitness from the last generation
iteration=1
if change >= convergence or iteration <= maximum_iterations:
 print "Iteration #",iteration

# print "current_pop=",current_pop

###
##
## STEP 1: EVALUATE FITNESS OF THE POPULATION
##
###
 print "Calculating the fitness of the current population"
 fitness = []
 i=0
 for i in range(pop_size):
# Temporarily use a random number for fitness function
  fitness.append( random.uniform(0.0,1.0 ) )
#  fitness.append( calc_fitness( current_pop[i] ) )
  i=i+1
###
##
## STEP 2: SELECTION (CHOOSE "FITTEST" MEMBERS OF PREVIOUS POPULATION)
##
###
 print "Choosing the fittest members of the population"

# fittest[] contains the integer values of the fittest population members
# best_fitness[] contains the fitness values for the two fittest members
 fittest_member = [-1,-1]
 best_fitness = [0.0,0.0]
 fittest_genome = [[0 for i in range(total_genes)],[0 for i in range(total_genes)]]
 i=0
 for i in range(pop_size):
  if i != any(fittest_member):
   if fitness[i] > best_fitness[0]:
    best_fitness[0]=fitness[i]
    fittest_member[0] = i
    fittest_genome[0] = current_pop[i][:]
   if (fitness[i] > best_fitness[1] and fitness[i] != best_fitness[0] ):
    best_fitness[1]=fitness[i]
    fittest_member[1] = i
    fittest_genome[1] = current_pop[i][:]
  i=i+1

###
##
## STEP 3: CROSSOVER (RANDOMLY EXCHANGE GENE(S) AMONG FITTEST PARENTS)
##
###
 print "Performing gene crossover for the fittest members"

# print "Parent #1 before crossover=",fittest_genome[0]
# print "Parent #2 before crossover=",fittest_genome[1]

 i=1
# crossover_list=[]
 while i <= crossover_events:
  crossover_gene=range(random.randint(0,total_genes-1),total_genes)
  print "crossover gene =",crossover_gene
  for j in crossover_gene:
   fittest_genome[0][j], fittest_genome[1][j] = fittest_genome[1][j], fittest_genome[0][j]
#  crossover_list.append(crossover_gene)
  i=i+1

#  print "Parent #1 after crossover=",fittest_genome[0]
#  print "Parent #2 after crossover=",fittest_genome[1]


###
##
## STEP 4: MUTATION (RANDOMLY MUTATE GENES OF NEW GENERATION)
##
###
 print "Performing mutation of offspring"
# Create the new generation
 new_pop=[[0 for i in range(total_genes)] for j in range(pop_size)]
 half_pop=int(round(pop_size/2))
 for i in range(0,half_pop):
  new_pop[i]=fittest_genome[0]
 for i in range(half_pop,pop_size):
  new_pop[i]=fittest_genome[1]
 j=1
 while j <= mutations:
  for i in range(0,pop_size):
   mutation_gene=random.randint(0,total_genes-1)
   print "member=",i
   print "mutated gene index=",mutation_gene
# Mutation is chosen from a Gaussian distribution of pure gene values
# with a standard devation of "mutation_bound"
   pure_gene=float(new_pop[i][mutation_gene])
   print "pure gene value=",new_pop[i][mutation_gene]
   mutation=round(random.gauss(pure_gene,mutation_bound),2)
   print "mutated gene value=",mutation
   new_pop[i][mutation_gene] , mutation = mutation, new_pop[i][mutation_gene]
  j=j+1
 for i in range(pop_size):
  print "member",i,"=",new_pop[i]
##
#
# Calculate fitness change of fittest member
#
##
 current_fitness=fitness[0]
 change=abs((current_fitness-last_fitness)/last_fitness)
 last_fitness=current_fitness
 iteration=iteration+1
else:

###
##
## ITERATE AGAIN OVER STEPS 1-4
##
###

 best_genome_file=open(best_genome_file, "w")

 for i in range( total_genes ):
  best_genome_file.write('%s %s\n' % (names_pop[i],current_pop[0][i]))
  break
###
##
## END OF GENETIC ALGORITHM
##
###

sys.exit()
