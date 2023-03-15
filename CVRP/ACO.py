class ACO:
    """
    This class outlines the structure of an optimization problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def calculateFitness(self):
        """
        Calculates the fitness of the population
        """
        pass

    def generatePopulation(self):
        """
        Generates a random initial population.
        """

        pass
    
    def chooseParents(self):
        """
        Implements a parent selection criteria
        
        Returns the selected pair
        """
        pass
    
    def getOffspring(self, parents: list):
        """Implement Crossover and Mutation

        Args:
            parents (list): list of parents
        """
        pass
    
    def crossOver(self, parents: list):
        """
        Produces offspring through crossover of parents
        
        Returns the offsprings
        """
        pass
    
    def mutation(self):
        """
        Mutates the offspring
        
        Returns the mutated individual
        """
        pass       

class Problem:
    def __init__(self) -> None:
        pass
    def getFitness(self):
        pass
    def getPopulation(self):
        pass
    def chooseParent(self):
        pass
    