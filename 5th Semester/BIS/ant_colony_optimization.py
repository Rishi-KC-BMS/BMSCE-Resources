
import random

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = 4
ants = 10
iterations = 100
alpha = 1
beta = 2
rho = 0.5
Q = 100

pheromone = [[1 for j in range(n)] for i in range(n)]

best_path = []
best_distance = float('inf')

for t in range(iterations):

    all_paths = []
    all_distances = []

    for ant in range(ants):

        path = [random.randint(0, n - 1)]

        while len(path) < n:

            current = path[-1]
            unvisited = [i for i in range(n) if i not in path]

            probabilities = []

            for city in unvisited:
                p = (pheromone[current][city] ** alpha) * \
                    ((1 / dist[current][city]) ** beta)
                probabilities.append(p)

            total = sum(probabilities)
            probabilities = [p / total for p in probabilities]

            next_city = random.choices(
                unvisited, weights=probabilities
            )[0]

            path.append(next_city)

        distance = 0

        for i in range(n - 1):
            distance += dist[path[i]][path[i + 1]]

        distance += dist[path[-1]][path[0]]

        all_paths.append(path)
        all_distances.append(distance)

        if distance < best_distance:
            best_distance = distance
            best_path = path[:]

    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= (1 - rho)

    for k in range(ants):
        path = all_paths[k]
        distance = all_distances[k]

        deposit = Q / distance

        for i in range(n - 1):
            a = path[i]
            b = path[i + 1]
            pheromone[a][b] += deposit
            pheromone[b][a] += deposit

        a = path[-1]
        b = path[0]
        pheromone[a][b] += deposit
        pheromone[b][a] += deposit

# Display result
print("\n====== ANT COLONY OPTIMIZATION ======")

print("Number of Cities :", n)
print("Number of Ants   :", ants)
print("Iterations      :", iterations)

print("-------------------------------------")

print("Best Tour:")
print(" -> ".join(str(city + 1) for city in best_path),
      "->", best_path[0] + 1)

print("-------------------------------------")

print("Shortest Distance:", best_distance)

print("=====================================")


#Output
# ====== ANT COLONY OPTIMIZATION ======
# Number of Cities : 4
# Number of Ants   : 10
# Iterations      : 100
# -------------------------------------
# Best Tour:
# 3 -> 1 -> 2 -> 4 -> 3
# -------------------------------------
# Shortest Distance: 80
# =====================================
