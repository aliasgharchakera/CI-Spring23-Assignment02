import random
import numpy as np

class Ant:
    def __init__(self, alpha, beta, num_cities, pheromone, distances):
        self.alpha = alpha
        self.beta = beta
        self.num_cities = num_cities
        self.pheromone = pheromone
        self.distances = distances
        self.tour = []
        self.visited = np.zeros(num_cities, dtype=bool)
        self.total_distance = 0
        
    def choose_next_city(self, current_city):
        unvisited_cities = np.where(~self.visited)[0]
        if len(unvisited_cities) == 0:
            return None
        
        pheromone = np.power(self.pheromone[current_city, unvisited_cities], self.alpha)
        attractiveness = np.power(1 / self.distances[current_city, unvisited_cities], self.beta)
        
        prob = pheromone * attractiveness / np.sum(pheromone * attractiveness)
        next_city = np.random.choice(unvisited_cities, p=prob)
        return next_city
        
    def update_pheromone(self, evaporation_rate, Q):
        for i in range(self.num_cities):
            for j in range(i+1, self.num_cities):
                self.pheromone[i,j] *= (1 - evaporation_rate)
                self.pheromone[j,i] = self.pheromone[i,j]
        
        for i in range(len(self.tour)-1):
            city1 = self.tour[i]
            city2 = self.tour[i+1]
            self.pheromone[city1, city2] += Q / self.total_distance
            self.pheromone[city2, city1] = self.pheromone[city1, city2]
        
    def tour_length(self):
        self.total_distance = 0
        for i in range(len(self.tour)-1):
            city1 = self.tour[i]
            city2 = self.tour[i+1]
            self.total_distance += self.distances[city1, city2]
        
    def run(self, start_city):
        self.visited[start_city] = True
        self.tour.append(start_city)
        current_city = start_city
        
        while True:
            next_city = self.choose_next_city(current_city)
            if next_city is None:
                break
            self.visited[next_city] = True
            self.tour.append(next_city)
            self.total_distance += self.distances[current_city, next_city]
            current_city = next_city
        
        self.tour_length()
        
        
class ACO:
    def __init__(self, num_ants, num_iterations, alpha, beta, rho, Q, distances):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.num_cities = distances.shape[0]
        self.distances = distances
        self.pheromone = np.ones((self.num_cities, self.num_cities))
        self.ants = [Ant(alpha, beta, self.num_cities, self.pheromone, self.distances) for _ in range(num_ants)]
        self.best_tour = None
        self.best_tour_length = float('inf')
        
    def update_pheromone(self):
        for ant in self.ants:
            ant.update_pheromone(self.rho, self.Q)
        
    def run(self, start_city):
        for i in range(self.num_iterations):
            for ant in self.ants:
                ant.run(start_city)
                
                if ant.total_distance < self.best_tour_length:
                    self.best_tour = ant.tour
                    self.best_tour_length = ant.total_distance
            
            self.update_pheromone()
            
        return self.best_tour, self.best_tour_length
