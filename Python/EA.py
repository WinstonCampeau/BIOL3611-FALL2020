#! /usr/bin/python

#EVOLUTIONARY ALGORITHM EXAMPLE#
#Winston Campeau, v1.0_2020#

import random
import math
import numpy
import sys
import locale
from itertools import izip
locale.setlocale(locale.LC_ALL, '') 


#Makes a random population of N (pop_size), K length (gen_length) binary genomes.

def population_generator(pop_size, gen_length):
	
	population = []
	
	for i in range(pop_size):
		
		temp = []
		
		for j in range(gen_length):		
			
			temp.append(random.randint(0,1))
		
		population.append(temp)
		
	return population

# Computed Hamming Distance of two strings

def hamming(list0, list1):
    return sum(c1 != c2 for c1, c2 in izip(list0, list1))


# "Selection". Input your target genome, a threshold of how similar genomes are to target (how many genome positions), 'population' is jsut the list of all genomes

def selection(target_genome, hamming_threshold, population):
	
	to_del = []
	
	for genome in population:
		
		if hamming(target_genome, genome) > hamming_threshold:
			
			to_del.append(genome)
	
	for genome in to_del:
		
		population.remove(genome)
		
# sexual recombination of genomes -- do this after selection. 
# offspring are a random 50/50 mix of each parent. Becomes the new population. 
# offspring can also be mutated in one random position, randomly.
		
def mating(population, gen_length):
	
	num_matings = int(math.ceil(len(population)/2.))
	
	for i in range(num_matings):
		
		offspring = []
		gen_a = population[random.randint(0, len(population)-1)]
		gen_b = population[random.randint(0, len(population)-1)]
		
		while len(offspring) < gen_length:
			
			for j in range(gen_length):
			
				tmp_num = random.randint(0,9)

				if tmp_num%2==0:
					offspring.append(gen_a[j])
				if tmp_num%2==1:
					offspring.append(gen_b[j])
				
				if len(offspring)==gen_length and tmp_num >=5: # this is the mutation section
					
					tmp_num = random.randint(0, gen_length-1)
					offspring[tmp_num] = 1-offspring[tmp_num]
				
		population.append(offspring)
		
# checks if there is at least one genome equivalent to the target
		
def check(population, target_genome):
	
	exit = None
	
	for genome in population:
		
		if hamming(genome, target_genome) == 0:
			
			exit = True
		
		else:
			
			exit = False
			
	return exit

# makes sure the population doesn't explode to some huge number, "limit" set that limit.
# deletions are completely random. 

def carrying_capacity(population, limit):
	
	if len(population) > limit:
		
		to_del = random.sample(numpy.arange(len(population)), len(population)-limit)
		
		for index in sorted(to_del, reverse=True):
			del population[index]
					
													
population_size = 10 # set your population
genome_length = 16 # length of genomes
target_genome = [1]*genome_length # set your target genome, the genome of all ones by default

hamming_threshold = 10 # should never exceed genome length -- but you can. In which case, mating is random and selection is pointless, i.e. all by genetic drift. 0 is also boring...
					   # the meaning of the number is, "You can be different in X number of places, but still produce viable offspring

generation = 1 # initiates the generation counter
cc = 100 # maximum population size
generation_time = 75 # how many years is a generation? I picked a human lifespan. 

test = population_generator(population_size, genome_length)

print "Starting population\n", test, "\n"

print "Starting simulation, press anything to begin..."

wait = raw_input()

while check(test, target_genome)==False:
	
	selection(target_genome, hamming_threshold, test)
	mating(test, genome_length)
	carrying_capacity(test, cc)
	output_string = str('{:n}'.format(generation)) + " generations"
	sys.stdout.write('%s\r' % output_string)
	sys.stdout.flush()
	generation += 1
	
	if generation == 1000000:
		print "Target genome not acheivable after 1 million generations,"
		break

if len(test) == 0:
	
	print "All organisms are extinct!"
		
if check(test, target_genome)==True:
	
	print "Target genome acheived after " + str('{:n}'.format(generation)) + " generations or " + str('{:n}'.format(generation*generation_time)) + " years."

	






