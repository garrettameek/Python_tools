def calc_fitness( trial_genome ):
 import numpy, random
###
##
## Calculate fitness of "genes", passed from genetic algorithm in "ga.py"
##
## Fitness = EXP [ - SUM_i ( target_V - trial_V ) ^ 2 ]
##
## 0 <= i <= len(r_list)
##
###
 scaling_factor=1.0e-8 # used to sensitize fitness function
# define values of "r" for which to calculate "V"
 r_list=[2.0,2.5,3.0,3.5,4.0,4.5,5.0]
 exact_genome=[13.0,-18.0,4.0]
 exp_argument=0.0
 sigma=3.0
 for i in range(len(r_list)):
# define the arguments of the fitness function
  trial_V=0.0
  V = trial_genome[0] * ( sigma / r_list[i] ) ** 12 + trial_genome[1] * ( sigma / r_list[i] ) ** 10 + trial_genome[2] * ( sigma / r_list[i] ) ** 6
  V_temp = trial_V + V
  trial_V = V_temp
  exact_V=0.0
  V = exact_genome[0] * ( sigma / r_list[i] ) ** 12 + exact_genome[1] * ( sigma / r_list[i] ) ** 10 + exact_genome[2] * ( sigma / r_list[i] ) ** 6
  V_temp = exact_V + V
  exact_V = V_temp

# define the argument of the exponential in the fitness function
#  temp_argument = exp_argument + ( exact_V - trial_V ) ** 2.0
#  exp_argument = temp_argument
# print exp_argument

# fitness=numpy.exp( - exp_argument ) 
 fitness=abs((exact_V - trial_V) / exact_V)
# print "fitness=",fitness

 return fitness
