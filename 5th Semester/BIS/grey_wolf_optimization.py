
import numpy as np

def fitness(x):
    return np.sum(x ** 2)

N = 20
dim = 3
Max_iter = 100
lower = -10
upper = 10

wolves = np.random.uniform(lower, upper, (N, dim))

alpha = np.zeros(dim)
beta = np.zeros(dim)
delta = np.zeros(dim)

alpha_score = float('inf')
beta_score = float('inf')
delta_score = float('inf')

for t in range(Max_iter):

    for i in range(N):
        score = fitness(wolves[i])

        if score < alpha_score:
            delta_score = beta_score
            delta = beta.copy()

            beta_score = alpha_score
            beta = alpha.copy()

            alpha_score = score
            alpha = wolves[i].copy()

        elif score < beta_score:
            delta_score = beta_score
            delta = beta.copy()

            beta_score = score
            beta = wolves[i].copy()

        elif score < delta_score:
            delta_score = score
            delta = wolves[i].copy()

    a = 2 - (2 * t / Max_iter)

    for i in range(N):

        r1, r2 = np.random.rand(), np.random.rand()
        A1 = 2 * a * r1 - a
        C1 = 2 * r2
        D_alpha = abs(C1 * alpha - wolves[i])
        X1 = alpha - A1 * D_alpha

        r1, r2 = np.random.rand(), np.random.rand()
        A2 = 2 * a * r1 - a
        C2 = 2 * r2
        D_beta = abs(C2 * beta - wolves[i])
        X2 = beta - A2 * D_beta

        r1, r2 = np.random.rand(), np.random.rand()
        A3 = 2 * a * r1 - a
        C3 = 2 * r2
        D_delta = abs(C3 * delta - wolves[i])
        X3 = delta - A3 * D_delta

        wolves[i] = (X1 + X2 + X3) / 3

        wolves[i] = np.clip(wolves[i], lower, upper)

print("Best Wolf (Alpha):", alpha)
print("Best Fitness:", alpha_score)

# Output
# Best Wolf (Alpha): [ 1.05029413e-07  2.61486941e-08 -1.07584902e-07]
# Best Fitness: 2.328944279999018e-14
