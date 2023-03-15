import random
import numpy as np
from input import readFile
import math

class Ant:
    def __init__(self, routes, distance) -> None:
        self.routes = routes
        self.distance = distance

class AntColonyOptimization:
    def __init__(self, alpha, beta, iteration, numAnts, evapRate, path) -> None:
        self.alpha = alpha
        self.beta = beta
        self.iteration = iteration
        self.numAnts = numAnts
        self.evapRate = evapRate
        self.Q = 1

        # Reading the Distance Matrix file with help of ACO File Read
        fileInst = readFile(path)
        # fileInst = temp.instanceTaker()
        # print(fileInst)
        self.capacity = fileInst["capacity"]
        self.depot = fileInst["depot"][0]
        self.n = fileInst["dimension"]
        self.demand = fileInst["demand"]
        self.distances = fileInst["edge_weight"]

        self.eta = np.reciprocal(self.distances, out=np.zeros_like(self.distances), where=self.distances!=0)
       
        # self.eta = [[1/i if i != 0 else 0 for i in row] for row in self.distances]



    def createAnt(self):
        route = list()
        unvisited = [i for i in range(1, self.n)]
        currentCity = self.depot
        truckCapacity = self.capacity
        totalDistance = 0
        path = list()
        path.append(self.depot)
        while len(unvisited) > 0:
            # Choosing random city from unvisited cities
            i = random.randint(0, len(unvisited) - 1)
            nextCity = unvisited[i]
            if self.demand[nextCity] <= truckCapacity:
                truckCapacity -= self.demand[nextCity]
                totalDistance += self.distances[currentCity][nextCity]
                path.append(nextCity)
                currentCity = nextCity
                # Now its time to pop the city from unvisited
                unvisited.pop(i)
            else:
                # This means that the truck is full and we need to go back to depot and line 70 will simply add the distance of depot to current city or vice versa

                totalDistance += self.distances[currentCity][self.depot]
                route.append(path)
                # Changing the capacity of vehicles
                truckCapacity = self.capacity
                path = list()
                path.append(self.depot)
                currentCity = self.depot
                truckCapacity -= self.demand[nextCity]
                totalDistance += self.distances[currentCity][nextCity]
                path.append(nextCity)
                currentCity = nextCity
                unvisited.pop(i)
        # Now I have to go back to depot to complete the route
        path.append(self.depot)
        totalDistance += self.distances[currentCity][self.depot]

        route.append(path)

        ant = Ant(route, totalDistance)
        return ant


    def AntColonyInitialization(self):
        # Initalizing Pheromones with 1
        self.pheromones = [[0 for i in range(self.n)] for j in range(self.n)]

        self.ants = [0 for i in range(self.numAnts)]

        # Making Artificial Ants by calculating Routes
        self.ants = []
        for i in range(self.numAnts):
            ant = self.createAnt()
            self.ants.append(ant)
       
    

    def computeTau(self):
        deltaT = [[0 for i in range(self.n)] for j in range(self.n)]
        for ant in self.ants:
            for route in ant.routes:
                for path in range(0,len(route)-1):
                    deltaT[route[path]][route[path+1]] += np.reciprocal(ant.distance)
                    deltaT[route[path+1]][route[path]] += np.reciprocal(ant.distance)
        return deltaT
    
    # def computingInverseDistance(self, i, j):
    #     InverseDistance = [[0 for i in range(self.n)] for j in range(self.n)]

    #     return 1/self.distances[i][j]
    

    def calculateProbabilities(self, currentCity, potentialCities):

        probabilities = []
        for i in potentialCities:
            p = math.pow(self.Tau[currentCity][i], self.alpha) + math.pow(self.eta[currentCity][i], self.beta)
            probabilities.append(p)

        sumProb = sum(probabilities)
        finalProb = [i/sumProb for i in probabilities]

        # Now making the ranges of Probabilities
        probRange = {}
        startRange = 0
        for i in range(len(finalProb)):
            probRange[i] = [startRange , startRange + finalProb[i]]
            startRange += finalProb[i]
        
        return probRange



    def simulateAnt(self):
        # Copying the code from AntMaking as now I have to decide the city with the help of probabilities
        
        fullRoute = []
        unvisited = [i for i in range(self.n)]
        currentCity = self.depot
        truckCapacity = self.capacity
        totalDistance = 0
        tempRoute = []
        tempRoute.append(self.depot)

        while len(unvisited) >1:
            # Choosing random city from unvisited cities
            potentialCities = []
            for i in unvisited:
                if self.demand[i] <= truckCapacity and i!= currentCity:
                    potentialCities.append(i)
            
            probRange = self.calculateProbabilities(currentCity, potentialCities)

            # Choosing the Random number
            randNum = random.random()
            for i in probRange:
                if randNum >= probRange[i][0] and randNum <= probRange[i][1]:
                    selectedCity = i
                    break
            
            nextCity = potentialCities[selectedCity]
            truckCapacity -= self.demand[nextCity]
            totalDistance += self.distances[currentCity][nextCity]

            currentCity = nextCity
            tempRoute.append(currentCity)

            if currentCity == self.depot:
                truckCapacity = self.capacity
                fullRoute.append(tempRoute)
                tempRoute = [self.depot]
            else:
                for i in unvisited:
                    if i == nextCity:
                        unvisited.remove(i)
                        break

        # Now the path will again go to Depot to make a full route
        tempRoute.append(self.depot)
        totalDistance += self.distances[currentCity][self.depot]

        fullRoute.append(tempRoute)

        return Ant(fullRoute, totalDistance)



    def updatePhermone(self):
        deltaTau = self.computeTau()
        for i in range(len(self.Tau)):
            for j in range(len(self.Tau)):
                self.Tau[i][j] = (self.Tau[i][j] * self.evapRate) + deltaTau[i][j]
            

    def ACO_main(self):
        self.AntColonyInitialization()

        # Updating the Tau Matrix
        self.Tau = self.computeTau()

        for i in range(self.iteration):
            tempAnt = []
            for j in range(self.numAnts):
                tempAnt.append(self.simulateAnt())
            
            self.ants = tempAnt
            # Now we have to update the Tow and get the new Tau
            self.updatePhermone()
        

        # Checking the minimum distance after the entire process
        minDist = float('inf')
        for ant in self.ants:
            if ant.distance < minDist:
                minDist = ant.distance
                minRoute = ant.routes
        
        print(minDist)






        

temp = AntColonyOptimization(2, 2, 50, 30, 0.6, "A-n32-k5")
temp.ACO_main()
# print(temp.distaneMatrix)
# print(temp.inverseDM)
# alpha, beta, iteration, numAnts, evapRate, path
