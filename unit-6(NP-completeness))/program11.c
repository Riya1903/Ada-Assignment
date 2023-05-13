# Implement a brute force algorithm for the Traveling Salesman Problem (TSP)
import itertools

def brute_force_tsp(dist_matrix):
    n = len(dist_matrix)
    cities = range(n)
    shortest_path = None
    shortest_distance = float("inf")

    for path in itertools.permutations(cities):
        distance = 0
        for i in range(n - 1):
            distance += dist_matrix[path[i]][path[i + 1]]
        distance += dist_matrix[path[-1]][path[0]]

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path

    return shortest_path, shortest_distance

# Analyze its time complexity using Big-O notation.
"""
To analyze the time complexity more formally, we can consider the number of computations required for the algorithm. 
Each permutation requires n-1 additions, and there are n! permutations, so the total number of computations is (n-1) * n!.
Thus, the time complexity of the algorithm is O(n * n!), which is clearly impractical for large values of n.

"""