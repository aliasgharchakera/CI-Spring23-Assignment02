# ACO Algorithm for CVRP and Car Exhaust Smoke Visualization

This repository contains the implementation of an Ant Colony Optimization (ACO) algorithm for solving the Capacitated Vehicle Routing Problem (CVRP) and a particle system for visualizing car exhaust smoke. The ACO algorithm is a metaheuristic inspired by the foraging behavior of ants, and it is applied to find efficient routes for vehicle routing problems. The particle system provides a visual representation of car exhaust smoke for simulation and analysis purposes.

## Table of Contents
- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [ACO Algorithm Overview](#aco-algorithm-overview)
- [CVRP Problem Description](#cvrp-problem-description)
- [Particle System for Car Exhaust Smoke Visualization](#particle-system-for-car-exhaust-smoke-visualization)
- [Results](#results)
- [Contributors](#contributors)

## Introduction
In this assignment, I have implemented an ACO algorithm to solve the CVRP and a particle system to visualize car exhaust smoke. The ACO algorithm is a population-based optimization technique that mimics the behavior of ants searching for food. It is used to find optimal or near-optimal routes for vehicle routing problems with capacity constraints. The particle system, on the other hand, provides a realistic simulation of car exhaust smoke, allowing for visual analysis and understanding of the emission patterns.

The main goal of this assignment is to demonstrate the implementation and application of the ACO algorithm for the CVRP and the particle system for car exhaust smoke visualization. The provided code serves as a starting point for further experimentation and research in the fields of optimization and visualization.

## Dependencies
The following dependencies are required to run the code:
- Python 
- NumPy
- Matplotlib (for visualization)
- Processing.py (for particle system visualization)

## ACO Algorithm Overview
The implemented ACO algorithm follows these main steps:

1. **Initialization**: Initialize a population of ants and the pheromone matrix.
2. **Ant Construction**: Each ant constructs a solution by probabilistically selecting edges based on pheromone values and heuristic information.
3. **Local Update**: Update the pheromone values on the edges of the constructed solutions.
4. **Global Update**: Update the pheromone values globally based on the best solution found so far.
5. Repeat steps 2-4 for a specified number of iterations or until a stopping criterion is met.

The ACO algorithm exploits the positive feedback mechanism of pheromone trails to guide the search towards promising areas of the solution space.

## CVRP Problem Description
The Capacitated Vehicle Routing Problem (CVRP) is a well-known optimization problem in logistics. It involves finding optimal routes for a fleet of vehicles to deliver goods from a central depot to a set of customers, while respecting capacity constraints of the vehicles. The ACO algorithm is applied to find the most efficient set of routes that minimize the total distance traveled.

## Particle System for Car Exhaust Smoke Visualization
The particle system provides a visual representation of car exhaust smoke, which can be useful for simulating and analyzing emission patterns. The system simulates the movement of individual particles representing smoke particles emitted from car exhausts, taking into account factors such as wind speed and direction, particle dispersion, and lifetime.

## Results
The repository includes example results obtained by running the ACO algorithm on CVRP instances and visualizing car exhaust smoke using the particle system.

## Contributors
This was a group assignment completed in collaboration with [Muhammad Murtaza]( https://github.com/mm06369/ ).

<a href="https://github.com/aliasgharchakera/CI-Spring23-Assignment01/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=aliasgharchakera/CI-Spring23-Assignment01" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
