import numpy as np

X = np.array([
    [1, 1],
    [2, 1],
    [3, 1],
    [1, 4],
    [0, 1]
])

y = np.array([1, 0, 0, 0, 1])

eta = 0.01
iterations = 20

w1 = 0.1
w2 = 0.2
b = 1


def step_function(z):
    if z >= 0:
        return 1
    else:
        return 0


for iteration in range(1, iterations + 1):
    print(f"\n============= Iteration {iteration} ==============")

    for i in range(len(X)):

        x1 = X[i][0]
        x2 = X[i][1]
        target = y[i]

        z = (w1 * x1) + (w2 * x2) + b

        prediction = step_function(z)

        error = target - prediction

        delta_w1 = eta * error * x1
        delta_w2 = eta * error * x2
        delta_b = eta * error

        w1 = w1 + delta_w1
        w2 = w2 + delta_w2
        b = b + delta_b

        print(
            f"x1={x1}, x2={x2}, "
            f"target={target}, "
            f"prediction={prediction}, "
            f"error={error}, "
            f"w1={w1:.2f}, "
            f"w2={w2:.2f}, "
            f"b={b:.2f}"
        )
