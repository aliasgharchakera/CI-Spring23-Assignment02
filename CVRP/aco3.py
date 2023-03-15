class Ant:
    def __init__(self, num_customers, capacity):
        self.visited = np.zeros(num_customers, dtype=np.bool)
        self.solution = []
        self.cost = np.inf
        self.remaining_capacity = capacity
        self.current_node = 0
        
    def visit(self, node):
        self.visited[node-1] = True
        self.solution.append(node)
        self.remaining_capacity -= self.demand[node-1]
        self.current_node = node
        
    def full(self):
        return self.remaining_capacity < 0

    def calculate_cost(self, solution):
        cost = 0
        for i in range(len(solution)-1):
            cost += self.dist_matrix[solution[i], solution[i+1]]
        return cost
        
    def update_pheromone(self, pheromone_matrix, q):
        for i in range(len(self.solution)-1):
            pheromone_matrix[self.solution[i], self.solution[i+1]] += q/self.cost
 
import numpy as np

class CVRP_ACO:
    def __init__(self, dist_matrix, demand, num_ants, evap_rate=0.1, alpha=1, beta=2, q=1, pheromone=1, iterations=100):
        self.dist_matrix = dist_matrix # distance matrix
        self.demand = demand # demand of each customer
        self.num_ants = num_ants # number of ants
        self.evap_rate = evap_rate # evaporation rate of pheromone
        self.alpha = alpha # importance of pheromone in path selection
        self.beta = beta # importance of distance in path selection
        self.q = q # pheromone deposit factor
        self.pheromone = pheromone # initial pheromone amount
        self.iterations = iterations # number of iterations
        self.num_nodes = len(dist_matrix) # number of nodes
        self.nodes = np.arange(1, self.num_nodes) # list of customer nodes
        self.num_customers = len(self.nodes) # number of customers
        self.capacity = np.sum(demand) / 2 # capacity of each vehicle
        self.best_cost = np.inf # best cost found so far
        self.best_solution = None # best solution found so far
        
        # initialize pheromone matrix
        self.pheromone_matrix = np.full((self.num_nodes, self.num_nodes), self.pheromone)
        np.fill_diagonal(self.pheromone_matrix, 0)
        
    def run(self):
        for i in range(self.iterations):
            # create ants
            ants = [self.create_ant() for _ in range(self.num_ants)]
            
            # update pheromone
            self.update_pheromone(ants)
            
            # find best solution
            best_ant = min(ants, key=lambda ant: ant.cost)
            if best_ant.cost < self.best_cost:
                self.best_cost = best_ant.cost
                self.best_solution = best_ant.solution
                
            # evaporation of pheromone
            self.pheromone_matrix *= (1 - self.evap_rate)
        
    def create_ant(self):
        # initialize ant
        ant = Ant(self.num_customers, self.capacity)
        
        # visit depot
        ant.visit(0)
        
        # visit customers
        while not ant.full():
            node = self.select_node(ant)
            ant.visit(node)
        
        # return to depot
        ant.visit(0)
        
        # calculate cost
        ant.cost = self.calculate_cost(ant.solution)
        
        return ant
    
    def select_node(self, ant):
        # calculate probabilities of selecting each node
        unvisited = np.setdiff1d(self.nodes, ant.visited)
        pheromone = self.pheromone_matrix[ant.current_node, unvisited]
        distance = self.dist_matrix[ant.current_node, unvisited]
        demand = self.demand[unvisited]
        mask = ant.remaining_capacity >= demand
        probabilities = np.zeros_like(unvisited, dtype=np.float64)
        probabilities[mask] = pheromone[mask]**self.alpha * (1/distance[mask])**self.beta
        probabilities /= probabilities.sum()
        
        # select node based on probabilities
        selected_node = np.random.choice(unvisited, p=probabilities)
        
        return selected_node
           
def solve_cvrp(dist_matrix, demand, num_ants, evap_rate=0.1, alpha=1, beta=2, q=1, pheromone=1, iterations=100):
    aco = CVRP_ACO(dist_matrix, demand, num_ants, evap_rate, alpha, beta, q, pheromone, iterations)
    aco.run()
    return aco.best_solution, aco.best_cost

num_ants = 10
evap_rate = 0.1
alpha = 1
beta = 2
q = 1
pheromone = 1
iterations = 100

# Define the number of customers, including the depot (which is customer 0)
num_customers = 6

# Define the demand for each customer
demand = np.array([0, 1, 2, 3, 4, 5])

# Define the locations for each customer
locations = np.array([
    [0, 0],  # depot
    [1, 1],  # customer 1
    [2, 2],  # customer 2
    [3, 3],  # customer 3
    [4, 4],  # customer 4
    [5, 5]   # customer 5
])

# Calculate the distance matrix based on Euclidean distance
dist_matrix = np.zeros((num_customers, num_customers))
for i in range(num_customers):
    for j in range(num_customers):
        if i == j:
            dist_matrix[i][j] = 0
        else:
            dist_matrix[i][j] = np.linalg.norm(locations[i] - locations[j])

best_solution, best_cost = solve_cvrp(dist_matrix, demand, num_ants, evap_rate, alpha, beta, q, pheromone, iterations)

print("Best solution:", best_solution)
print("Best cost:", best_cost)

