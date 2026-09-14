import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

np.random.seed(1)


X = []
y = []

for _ in range(100):
    x1 = np.random.uniform(-5, 5)
    x2 = np.random.uniform(-5, 5)

    r_squared = x1**2 + x2**2   

    # Inside circle of radius 2 -> 1, outside -> 0
    if r_squared <= 4:
        target = 1
    else:
        target = 0

    X.append([x1, x2])
    y.append(target)

X = np.array(X)
y = np.array(y)

# ---------------- Plotting ----------------
fig, ax = plt.subplots(figsize=(7, 7))

inside  = y == 1
outside = y == 0

ax.scatter(X[inside, 0],  X[inside, 1],  c='blue', s=40,
           edgecolor='k', label='inside (class 1)')
ax.scatter(X[outside, 0], X[outside, 1], c='red',  s=40,
           edgecolor='k', label='outside (class 0)')


true_circle = Circle((0, 0), radius=2, fill=False,
                     edgecolor='green', linewidth=2,
                     label='boundary (r = 2)')
ax.add_patch(true_circle)

# Axes setup
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')      
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('Points classified by distance from origin')
ax.legend(loc='upper right')
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()