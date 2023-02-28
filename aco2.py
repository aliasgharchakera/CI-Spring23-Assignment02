import numpy as np

class AntColony:
    def __init__(self, num_ants, num_iterations, evaporation_rate, alpha, beta):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.evaporation_rate = evaporation_rate
        self.alpha = alpha
        self.beta = beta
        self.graph = None
        self.pheromone = None
        self.best_path = None
        self.best_path_length = np.inf
        
    def run(self, graph):
        self.graph = graph
        self.pheromone = np.ones_like(graph) / len(graph)
        for i in range(self.num_iterations):
            for ant in range(self.num_ants):
                path = self.generate_path()
                path_length = self.calculate_path_length(path)
                self.update_pheromone(path, path_length)
                if path_length < self.best_path_length:
                    self.best_path = path
                    self.best_path_length = path_length
        return self.best_path, self.best_path_length
    
    def generate_path(self):
        path = []
        visited = np.zeros(len(self.graph))
        start_node = np.random.randint(len(self.graph))
        visited[start_node] = 1
        path.append(start_node)
        for i in range(len(self.graph) - 1):
            current_node = path[-1]
            probabilities = self.calculate_probabilities(current_node, visited)
            next_node = self.choose_next_node(probabilities)
            visited[next_node] = 1
            path.append(next_node)
        return path
    
    def calculate_probabilities(self, current_node, visited):
        pheromone = self.pheromone[current_node]
        heuristic = 1 / (self.graph[current_node] + 1e-10)
        probabilities = np.power(pheromone, self.alpha) * np.power(heuristic, self.beta)
        probabilities *= 1 - visited
        probabilities /= np.sum(probabilities)
        return probabilities
    
    def choose_next_node(self, probabilities):
        return np.random.choice(len(probabilities), p=probabilities)
    
    def calculate_path_length(self, path):
        length = 0
        for i in range(len(path) - 1):
            length += self.graph[path[i], path[i+1]]
        return length
    
    def update_pheromone(self, path, path_length):
        delta_pheromone = np.zeros_like(self.pheromone)
        for i in range(len(path) - 1):
            delta_pheromone[path[i], path[i+1]] = 1 / path_length
            delta_pheromone[path[i+1], path[i]] = 1 / path_length
        self.pheromone = (1 - self.evaporation_rate) * self.pheromone + self.evaporation_rate * delta_pheromone

# Define the graph
graph = np.array([[0, 1, 2, 3],
                  [1, 0, 4, 5],
                  [2, 4, 0, 6],
                  [3, 5, 6, 0]])

# Create an instance of the AntColony class
ant_colony = AntColony(num_ants=10, num_iterations=100, evaporation_rate=0.5, alpha=1, beta=5)

# Run the algorithm and get the best path and length
best_path, best_path_length = ant_colony.run(graph)

# Print the results
print("Best path:", best_path)  
print("Best path length:", best_path_length)
