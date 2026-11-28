
import random

def fitness(x):
    return sum(i * i for i in x)

N = 20
dim = 3
Pa = 0.25
Max_iter = 100
alpha = 0.01
lower = -10
upper = 10

nests = [
    [random.uniform(lower, upper) for _ in range(dim)]
    for _ in range(N)
]

best = min(nests, key=fitness)

for t in range(Max_iter):

    for i in range(N):
        step = [
            random.gauss(0, 1) /
            (abs(random.gauss(0, 1)) ** (1 / 1.5) + 0.0001)
            for _ in range(dim)
        ]

        new_nest = [
            nests[i][d] + alpha * step[d]
            for d in range(dim)
        ]

        new_nest = [
            max(lower, min(upper, x))
            for x in new_nest
        ]

        j = random.randint(0, N - 1)

        if fitness(new_nest) < fitness(nests[j]):
            nests[j] = new_nest

    for i in range(N):
        if random.random() < Pa:
            nests[i] = [
                random.uniform(lower, upper)
                for _ in range(dim)
            ]

    current_best = min(nests, key=fitness)

    if fitness(current_best) < fitness(best):
        best = current_best[:]

print("\n========== CUCKOO SEARCH RESULTS ==========")
print("Algorithm       : Cuckoo Search")
print("Population Size :", N)
print("Iterations      :", Max_iter)
print("-------------------------------------------")

print("Best Solution   :")
for i, value in enumerate(best):
    print("  x" + str(i + 1) + " =", round(value, 6))

print("-------------------------------------------")
print("Minimum Fitness :", round(fitness(best), 8))
print("===========================================")


# Ouput
# ========== CUCKOO SEARCH RESULTS ==========
# Algorithm       : Cuckoo Search
# Population Size : 20
# Iterations      : 100
# -------------------------------------------
# Best Solution   :
#   x1 = -0.016247
#   x2 = -0.002936
#   x3 = -0.056093
# -------------------------------------------
# Minimum Fitness : 0.00341901
# ===========================================
