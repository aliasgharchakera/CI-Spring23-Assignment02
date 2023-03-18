import matplotlib.pyplot as plt
import numpy as np
from CVRP import AntColonyOptimization


iterations = 50
numAnts = 30
def main():
    minlst = []
    avglst = []
    aco = AntColonyOptimization(4, 4, iterations, numAnts, 0.5, "A-n60-k9")
    aco.AntColonySimulation(initialize=True)
    aco.tau = aco.computeTau()
    for i in range(iterations):
        aco.AntColonySimulation(initialize=False)
        aco.updateTau()
        minlst.append(aco.minDistance)
        avglst.append(np.average(aco.avgDistances))
    print("Overall Minimum Distance: ", aco.minDistance)
    print("Overall Minimum Route: ", aco.minRoute)
    return minlst, avglst
    
    
minlst, avglst = main()
plt.plot([i for i in range(1, iterations+1)], minlst, label="min")
plt.plot([i for i in range(1, iterations+1)], avglst, label="avg")
# plt.xlabel('generation')
# plt.title('Plot of average fitness against generations')
plt.xlabel('iteration')
plt.title('Plot of average fitness against iterations')
plt.ylabel('fitness')
plt.legend()
plt.show()