#GA template
import random

class MyGA:
    
    def __init__(self, popsize, generations, data):
        self.popsize = popsize # Could be needed for random population generation
        self.generations = generations # Amount of generations to go / a stopping criterion in this case.
        self.data = data # Original data and current generation are intialized
        self.currGeneration = data
        self.bestIndividual = None # TBD as a result of GA execution
        
    def crossover(self, parent_1, parent_2):
        # Define crossover "masks" - it is problem specific, depends on the string length.
        # For example, for 5 bits-long string, for "after 3rd bit" crossover position the masks will be 11100 (28 decimal) and 00011 (3 decimal)
        
        #Define random position for crossover bit
        bit_pos = random.randrange(1,5) #0-4?
        
        mask_head = 28
        mask_tail = 3
        
        # Making the crossover
        child_1 = (parent_1 & mask_head) + (parent_2 & mask_tail) # head of parent 1, tail of parent 2
        child_2 = (parent_2 & mask_head) + (parent_1 & mask_tail) # head of parent 2, tail of parent 1
        return child_1, child_2
        
        
    def fitness(self, individual, currGeneration):
        # Calculate fitness score of the individual w.r.t. the current generation
        # Problem specific - x*x.
        # Sum up all the functions
        sum = 0
        for x in currGeneration:
            sum += x*x
        return individual*individual/sum
    
    def selection(self, currGeneration, fitnessResults):
    
        #Ekstremt dårlig kode. Det hadde vært bedre å bare sortere listen med høyeste først og så hente elementene
        #ut iterativt.

        # Problem specific. In this case - 2 pairs, the fittest - in both pairs and then the two next best ones - for one time.
        # Get position of the fittest
        theFittest = max(fitnessResults)
        posFittest = fitnessResults.index(theFittest)
        
        sel_1 = currGeneration[posFittest]
        # Setting best individual based on the current generation
        self.bestIndividual = sel_1
        #Remove the fittest from the current generation
        currGeneration.remove(sel_1)
        fitnessResults.remove(theFittest)
        
        #Find the second fittest
        theFittest = max(fitnessResults)
        posFittest = fitnessResults.index(theFittest)
        
        sel_2 = currGeneration[posFittest]
        #Remove the second fittest from the current generation
        currGeneration.remove(sel_2)
        fitnessResults.remove(theFittest)
        
        #Find the third fittest
        theFittest = max(fitnessResults)
        posFittest = fitnessResults.index(theFittest)
        
        sel_3 = currGeneration[posFittest]
        #Remove the third fittest from the current generation - optional, as we have found everything what we were looking for
        currGeneration.remove(sel_3)
        fitnessResults.remove(theFittest)
        
        return [(sel_1,sel_2),(sel_1,sel_3)] # An array of pairs for crossover
    
    
    def run(self):
        # Execute the algorithm 
        nextGeneration = self.data # To populate as the next generation, in the beginning is set to data
        fitnessResults = [] #An empty array to store fitness results.
        #Iterating via the # of generations defined.
        for i in range(1, self.generations):
            currGeneration = nextGeneration.copy()
            nextGeneration.clear()
            # Fitness evaluation for the current generation
            for individual in currGeneration:
                fitnessResults.append(self.fitness(individual, currGeneration))
            
            # Select the fittest parents for crossover
            selection = self.selection(currGeneration, fitnessResults)
            
            # Make the crossover
            for pair in selection:
                child1, child2 = self.crossover(pair[0],pair[1]) # Taking two selected parents to generate two children (just one of the ways to do it).
                nextGeneration.append(child1) # Appending children to the next generation variable.
                nextGeneration.append(child1)
            
            # Mutation - TBD
            
            # Clearing fitnessResults
            fitnessResults.clear()
        
        # By this time, after the loop execution, the best individual was set via the selection function inside the loops.
        return
    
    
# Test the class
data = [13, 24, 8, 19] 
myga = MyGA(4, 5, data)
print("Fitness test", myga.fitness(13, data)) 
print("Crossover test", myga.crossover(13, 24)[0]) 

# Some useful operations
print("Random selection test", random.choice(data))
print("Max test", max(data))
print("Index of the element", data.index(19))

myga.run()
print("Best individual:", myga.bestIndividual)
