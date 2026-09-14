import numpy as np

np.random.seed(1)

X = []
y = []

# Generate points
for _ in range(100):

    x1 = np.random.uniform(-5, 5)
    x2 = np.random.uniform(-5, 5)

    # Distance from origin
    distance = x1**2 + x2**2

    # Inside circle -> 1
    # Outside circle -> 0
    if distance <= 4:
        target = 1
    else:
        target = 0

    X.append([x1, x2])
    y.append(target)

X = np.array(X)
y = np.array(y)


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

    total_errors = 0

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

        if error != 0:
            total_errors += 1

        print(
            f"x1={x1:.2f}, "
            f"x2={x2:.2f}, "
            f"target={target}, "
            f"prediction={prediction}, "
            f"error={error}, "
            f"w1={w1:.2f}, "
            f"w2={w2:.2f}, "
            f"b={b:.2f}"
        )

    print(f"Total errors in iteration: {total_errors}")
