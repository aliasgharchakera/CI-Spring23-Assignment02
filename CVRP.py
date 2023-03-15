import numpy as np
from input import input
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
            # print("Iteration:", iteration, "Best Cost:", best_cost)
        return best_solution, best_cost

    def construct_solution(self, pheromone):
        solution = []
        visited = set()
        current_customer = 0
        current_capacity = 0
        all_customers = set(range(0, self.num_customers))
        while len(visited) < self.num_customers:
            unvisited_customers = set(range(0, self.num_customers)) - visited
            probabilities = np.zeros(self.num_customers)
            # print(visited)
            # print(list(unvisited_customers))
            # print(probabilities)
            for customer in unvisited_customers:
                # print(customer)
                if self.demands[customer] > self.max_capacity - current_capacity:
                    probabilities[customer] = 0
                else:
                    probabilities[customer] = pheromone[current_customer, customer]**self.alpha * (1/self.distances[current_customer, customer])**self.beta
            
            for v in visited:
                probabilities[v] = 0
            if probabilities.sum() == 0:
                break
            probabilities = probabilities/probabilities.sum()
            # print(list(probabilities))
            next_customer = np.random.choice(list(all_customers), p=list(probabilities))
            visited.add(next_customer)
            solution.append(next_customer)
            current_capacity += self.demands[next_customer]
            current_customer = next_customer
        solution.append(0)
        return solution
    
    def select_next_customer(self, ant, current_customer, unvisited_customers):
        # calculate probabilities for unvisited customers
        filtered_probabilities = []
        for customer in unvisited_customers:
            probability = self.calculate_transition_probability(ant, current_customer, customer)
            filtered_probabilities.append(probability)
            
        # select next customer based on probabilities
        filtered_probabilities = np.array(filtered_probabilities)
        sum_prob = np.sum(filtered_probabilities)
        if sum_prob > 0:
            filtered_probabilities /= sum_prob
            next_customer_index = np.random.choice(len(unvisited_customers), p=filtered_probabilities)
            return unvisited_customers[next_customer_index]
        else:
            return None


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
print(distances)
print(len(demands), num_customers)
print(demands)
distances, demands, k, num_customers, max_capacity = input('A-n32-k05.xml')
# create ACO instance and run algorithm
print(distances)
print(len(demands), num_customers)
print(demands)
aco = AntColonyOptimization(num_ants, num_iterations, alpha, beta, rho, q, max_capacity, num_customers, distances, demands)
# best_solution, best_cost = aco.run()

# print best solution and cost
print("Best Solution:", best_solution)
print("Best Cost:", best_cost)
