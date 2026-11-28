
def fitness(x):
    return x*x - 4*x + 4

size = 10
N = size * size
Max_iter = 100
lower = -10
upper = 10

import random

cells = [
    [random.uniform(lower, upper) for j in range(size)]
    for i in range(size)
]

best = cells[0][0]

for t in range(Max_iter):

    new_cells = [[0 for j in range(size)]
                 for i in range(size)]

    for i in range(size):
        for j in range(size):

            best_neighbor = cells[i][j]

            for di in range(-1, 2):
                for dj in range(-1, 2):

                    ni = (i + di) % size
                    nj = (j + dj) % size

                    if fitness(cells[ni][nj]) < fitness(best_neighbor):
                        best_neighbor = cells[ni][nj]

            x = (cells[i][j] + best_neighbor) / 2

            x = max(lower, min(upper, x))

            new_cells[i][j] = x

    cells = new_cells

    for i in range(size):
        for j in range(size):
            if fitness(cells[i][j]) < fitness(best):
                best = cells[i][j]

print("\n===== PARALLEL CELLULAR ALGORITHM =====")
print("Grid Size       :", size, "x", size)
print("Total Cells     :", N)
print("Iterations      :", Max_iter)

print("---------------------------------------")
print("Best Solution   :", round(best, 6))
print("Minimum Fitness :", round(fitness(best), 8))
print("=======================================")


# Ouput
# ===== PARALLEL CELLULAR ALGORITHM =====
# Grid Size       : 10 x 10
# Total Cells     : 100
# Iterations      : 100
# ---------------------------------------
# Best Solution   : 2.0
# Minimum Fitness : 0.0
# =======================================
