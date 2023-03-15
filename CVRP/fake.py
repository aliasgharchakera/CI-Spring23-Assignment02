import random
import numpy as np
from input import readFile
import math

class Ant:
    def __init__(self, routes, distance) -> None:
        self.routes = routes
        self.distance = distance

class AntColonyOptimization:
    def __init__(self, alpha, beta, iteration, numAnts, rho, path) -> None:
        self.alpha = alpha
        self.beta = beta
        self.iteration = iteration
        self.numAnts = numAnts
        self.evapRate = 1 - rho
        self.Q = 1

        # Reading the Distance Matrix file with help of ACO File Read
        fileInst = readFile(path)
        self.capacity = fileInst["capacity"]
        self.depot = fileInst["depot"][0]
        self.n = fileInst["dimension"]
        self.demand = fileInst["demand"]
        self.distances = fileInst["edge_weight"]

        self.eta = np.reciprocal(self.distances, out=np.zeros_like(self.distances), where=self.distances!=0)
       
        self.tau = np.zeros((self.n, self.n))
        self.minDistance = np.inf
        self.minRoute = None
        self.avgDistances = list()


    def AntColonySimulation(self, initialize=False):
        # If initialize is True, we randomly select a path, else we use the pheromones to select the path
        self.ants = list()
        for i in range(self.numAnts):
            ant = self.simulateAnt(initialize)
            self.ants.append(ant)

       
    def computeTau(self):
        deltaTau = [[0 for i in range(self.n)] for j in range(self.n)]
        for ant in self.ants:
            for route in ant.routes:
                for path in range(0,len(route)-1):
                    deltaTau[route[path]][route[path + 1]] += np.reciprocal(ant.distance)
                    deltaTau[route[path + 1]][route[path]] += np.reciprocal(ant.distance)
        return deltaTau
    

    def calculateProbabilities(self, currentCity, potentialCities):

        probabilities = list()
        for i in potentialCities:
            p = math.pow(self.tau[currentCity][i], self.alpha) + math.pow(self.eta[currentCity][i], self.beta)
            probabilities.append(p)

        probabilities = np.array(probabilities)/np.sum(probabilities)

        # Now making the ranges of Probabilities
        proportionalProbabilities = list()
        start = 0
        for i in range(len(probabilities)):
            proportionalProbabilities.append([start , start + probabilities[i]])
            start += probabilities[i]
        
        return proportionalProbabilities

    def getNextCity(self, currentCity, unvisited, truckCapacity):
        potentialCities = list()
        for i in unvisited:
            if self.demand[i] <= truckCapacity and i!= currentCity:
                potentialCities.append(i)
        
        proportionalProbabilities = self.calculateProbabilities(currentCity, potentialCities)

        # Choosing the Random number
        p = random.random()
        for i in range(len(proportionalProbabilities)):
            if p >= proportionalProbabilities[i][0] and p < proportionalProbabilities[i][1]:
                selectedCity = i
                break
        
        return potentialCities[selectedCity]

    def simulateAnt(self, initialize=False):
        # Initializing/Resetting the route
        
        route = list()
        unvisited = [i for i in range(self.n)]
        lim = 1
        if initialize:
            unvisited = unvisited[1:]
            lim = 0
        currentCity, truckCapacity = self.depot, self.capacity
        totalDistance = 0
        path = [currentCity]

        while len(unvisited) > lim:
            # Choosing random city from unvisited cities
            if initialize:
                # Choosing random city from unvisited cities
                i = random.randint(0, len(unvisited) - 1)
                nextCity = unvisited[i]
                if self.demand[nextCity] > truckCapacity:
                    totalDistance += self.distances[currentCity][self.depot]
                    currentCity = self.depot
                    route.append(path)
                    # Changing the capacity of vehicles
                    truckCapacity = self.capacity
                    path = [self.depot]
            else:
                # Choosing the city with the help of probabilities
                nextCity = self.getNextCity(currentCity, unvisited, truckCapacity)
            truckCapacity -= self.demand[nextCity]
            totalDistance += self.distances[currentCity][nextCity]

            currentCity = nextCity
            path.append(currentCity)
            if initialize:
                unvisited.pop(i)
            else:
                if currentCity == self.depot:
                    truckCapacity = self.capacity
                    route.append(path)
                    path = [self.depot]
                else:
                    unvisited.remove(currentCity)

        # Now the path will again go to Depot to make a full route
        path.append(self.depot)
        totalDistance += self.distances[currentCity][self.depot]

        route.append(path)
        if totalDistance < self.minDistance:
            self.minDistance = totalDistance
            self.minRoute = route
        self.avgDistances.append(totalDistance)
        return Ant(route, totalDistance)



    def updateTau(self):
        deltaTau = self.computeTau()
        for i in range(len(self.tau)):
            for j in range(len(self.tau)):
                self.tau[i][j] = (self.tau[i][j] * self.evapRate) + deltaTau[i][j]
            

    def run(self):
        self.AntColonySimulation(initialize=True)

        # Updating the Tau Matrix
        self.tau = self.computeTau()

        for i in range(self.iteration):
            self.AntColonySimulation(initialize=False)
            # Updating Tau Matrix
            self.updateTau()

        # Checking the minimum distance after the entire process
        minDist = float('inf')
        for ant in self.ants:
            if ant.distance < minDist:
                minDist = ant.distance
                minRoute = ant.routes
        
        print(minDist)
        print(minRoute)
        print("Overall Minimum Distance: ", self.minDistance)
        print("Overall Minimum Route: ", self.minRoute)

        

# aco = AntColonyOptimization(4, 4, 50, 30, 0.5, "A-n32-k5")
# aco.run()
