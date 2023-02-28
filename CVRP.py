import numpy as np
import random
import copy

class AntColonyOptimization:

    def __init__(self, num_ants, num_iterations, alpha, beta, rho, q, max_capacity, num_customers, distances, demands):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.q = q
        self.max_capacity = max_capacity
        self.num_customers = num_customers
        self.distances = distances
        self.demands = demands

    def run(self):
        pheromone = np.ones((self.num_customers+1, self.num_customers+1))
        best_cost = np.inf
        best_solution = []
        for iteration in range(self.num_iterations):
            solutions = []
            for ant in range(self.num_ants):
                solution = self.construct_solution(pheromone)
                solutions.append(solution)
            pheromone = self.update_pheromone(pheromone, solutions)
            cost, solution = self.get_best_solution(solutions)
            if cost < best_cost:
                best_cost = cost
                best_solution = solution
            print("Iteration:", iteration, "Best Cost:", best_cost)
        return best_solution, best_cost

    def construct_solution(self, pheromone):
        solution = []
        visited = set()
        current_customer = 0
        current_capacity = 0
        while len(visited) < self.num_customers:
            unvisited_customers = set(range(1, self.num_customers+1)) - visited
            probabilities = np.zeros(self.num_customers+1)
            for customer in unvisited_customers:
                if self.demands[customer] > self.max_capacity - current_capacity:
                    probabilities[customer] = 0
                else:
                    probabilities[customer] = pheromone[current_customer, customer]**self.alpha * (1/self.distances[current_customer, customer])**self.beta
            probabilities = probabilities/probabilities.sum()
            next_customer = np.random.choice(list(unvisited_customers), p=probabilities)
            visited.add(next_customer)
            solution.append(next_customer)
            current_capacity += self.demands[next_customer]
            current_customer = next_customer
        solution.append(0)
        return solution

    def update_pheromone(self, pheromone, solutions):
        pheromone *= (1-self.rho)
        for solution in solutions:
            cost = self.get_solution_cost(solution)
            for i in range(len(solution)-1):
                from_customer = solution[i]
                to_customer = solution[i+1]
                pheromone[from_customer, to_customer] += self.q/cost
        return pheromone

    def get_best_solution(self, solutions):
        best_cost = np.inf
        best_solution = []
        for solution in solutions:
            cost = self.get_solution_cost(solution)
            if cost < best_cost:
                best_cost = cost
                best_solution = solution
        return best_cost, best_solution

    def get_solution_cost(self, solution):
        cost = 0
        current_capacity = 0
        for i in range(len(solution)-1):
            from_customer = solution[i]
            to_customer = solution[i+1]
            cost += self.distances[from_customer, to_customer]
            current_capacity += self.demands[to_customer]
        return cost

# define problem parameters
num_ants = 10
num_iterations = 100
alpha = 1
beta = 3
rho = 0.5
q = 100
max_capacity = 200
num_customers = 10
distances = np.random.rand(num_customers+1, num_customers+1)
demands = np.random.randint(1, 50, num_customers+1)

# create ACO instance and run algorithm
aco = AntColonyOptimization(num_ants, num_iterations, alpha, beta, rho, q, max_capacity, num_customers, distances, demands)
best_solution, best_cost = aco.run()

# print best solution and cost
print("Best Solution:", best_solution)
print("Best Cost:", best_cost)
