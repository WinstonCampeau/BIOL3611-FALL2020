#! /usr/bin/python3

import random
import numpy
import matplotlib.pyplot as plt

def	start_pop(population_size, random_check):
	
	output	= []
	
	if random_check == True:
		
		for i in range(population_size):
			temp = []
			for j	in range(5):
				temp.append(random.randrange(0, 2))
			output.append(temp)
			
	else:
		
		tmp_zeros = [0]*5
		
		for i in range(population_size):
			
			output.append(tmp_zeros)
			
	return	output
	
def	org_val(org):
	
	val = 0
	
	for i in range(1,5):
		if org[i]	== 1:
			val += 2**(i-1)
	
	if	org[0] == 1:
		val *= -1	
	
	return	val
	
def	asex_new(population, env_state):
	
	temp_pop =	population
	del_list =	[]
	
	for i in range(len(population)):
		
		mutation_check = random.randrange(0,32)
		
		if mutation_check ==	15:
			random_pos = random.randrange(0,5)
			mut_org	= temp_pop[i]
			mut_org[random_pos]	= 1-mut_org[random_pos]
			temp_pop.append(mut_org)
		else:
			temp_pop.append(temp_pop[i])

	
	for i in range(len(temp_pop)):
		
		org_phe = org_val(temp_pop[i])
		
		if org_phe <= env_state-7.5 or org_phe >= env_state+7.5:
			del_list.append(i)
	
	for i in reversed(del_list):
		
		del temp_pop[i]
		  
	return	temp_pop

def sex_new(population, env_state):
	
	temp_pop =	population
	new_pop = []
	del_list =	[]
	mating_list = []
	sample_me = list(numpy.arange(len(temp_pop)))
	
	num_matings = int(len(population)/2.0)
	
	for i in range(num_matings):
		
		tmp = random.sample(sample_me, 2)
		mating_list.append(tmp)
		
	for mating in mating_list:
		
		recomb_org = []
		m1 = temp_pop[mating[0]]
		m2 = temp_pop[mating[1]]
		
		for i in range(1,6):
			
			tmp = random.randrange(1,10)
			mutation_check = random.randrange(0,32)
			
			if tmp%2 == 0:
				
				gene = m1[i-1]
				
				if mutation_check == 15:
					gene = (gene+1)%2
				
				recomb_org.append(gene)
				
			else:
				
				gene = m2[i-1]
				
				if mutation_check == 15:
					gene = (gene+1)%2
					
				recomb_org.append(m2[i-1])
			
		temp_pop.append(recomb_org)
		
	for i in range(len(temp_pop)):
		
		org_phe = org_val(temp_pop[i])
		
		if org_phe <= env_state-7.5 or org_phe >= env_state+7.5:
			del_list.append(i)
	
	for i in reversed(del_list):
		
		del temp_pop[i]						
	
	return temp_pop
   
	
def	env_var(length):
	
	output	= []
	
	for i in range(length):
		temp = numpy.random.normal(0,4.5,1)[0]
		output.append(temp)
		
	return	output

def cc(population, max_pop):
	
	tmp_p = population
	
	if len(population) > max_pop:
		
		num_to_rem = len(population) - max_pop
		ind_to_rem = random.sample(list(numpy.arange(len(population))), num_to_rem)
		
		for i in reversed(sorted(ind_to_rem)):
			
			del tmp_p[i]
			
	return tmp_p

def get_var(population):
	
	tmp_phenos = []
	
	for i in range(len(population)):
		
		tmp_pheno = org_val(population[i])
		tmp_phenos.append(tmp_pheno)
	
	output = numpy.var(tmp_phenos)
	
	return output
			
		
		


carrying_cap = 10000
test_popa = start_pop(1000, False)
test_pops = test_popa
test_env = env_var(500)

apop_card = []
spop_card = []
apop_card.append(len(test_popa))
spop_card.append(len(test_popa))
counter = 0

apop_var = [get_var(test_popa)]
spop_var = [get_var(test_pops)]

for env in test_env:
	
	if len(test_popa) == 0 and len(test_pops) == 0:
		test_popa.append(0)
		test_pops.append(0)
		print("Everything is dead!")
		break
	
	if len(test_popa) != 0:
	
		test_popa = cc(test_popa, carrying_cap)	
		test_popa = asex_new(test_popa, env)
		test_popa = cc(test_popa, carrying_cap)
		apop_card.append(apop_card[-1] + len(test_popa))
		apop_var.append(get_var(test_popa) + apop_var[-1])
	
	if len(test_pops) != 0:
		
		test_pops = cc(test_pops, carrying_cap)	
		test_pops = sex_new(test_pops, env)
		test_pops = cc(test_pops, carrying_cap)
		spop_card.append(spop_card[-1] + len(test_pops))
		spop_var.append(get_var(test_pops) + spop_var[-1])
		
		
	counter += 1

	print("Environmental state " + str(counter) + " out of " + str(len(test_env)) + " completed.")
	

x_asex = numpy.arange(len(apop_card))
x_ssex = numpy.arange(len(spop_card))

fig = plt.figure()

plt.subplot(1,3,1)
plt.plot(x_asex, apop_card, label='Asexual Population')
plt.plot(x_ssex, spop_card, label='Sexual Population')
plt.xlabel('Generation')
plt.ylabel('Cumulative Population Size')
plt.xlim([0, len(test_env)])
plt.legend()

plt.subplot(1,3,2)
plt.plot(x_asex, apop_var, label='Asexual Population')
plt.plot(x_ssex, spop_var, label='Sexual Population')
plt.xlabel('Generation')
plt.ylabel('Cumulative Population Variance')
plt.xlim([0, len(test_env)])
plt.legend()

plt.subplot(1,3,3)
plt.plot(list(numpy.arange(len(test_env))), test_env, c='r')
plt.xlabel('Time')
plt.ylabel('Environmental State')
plt.show()

print("Simulation Complete")




