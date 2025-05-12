import matplotlib.pyplot as plt
import numpy as np
from lorenz import solve_lorenz

def plot_difference():
    state1 = [1.0, 1.0, 1.0]
    state2 = [1.0001, 1.0, 1.0]

    t, sol1 = solve_lorenz(state1)
    _, sol2 = solve_lorenz(state2)
    difference = np.linalg.norm(sol1 - sol2, axis=0)

    plt.figure(figsize=(10, 5))
    plt.plot(t, difference, label="Різниця між траєкторіями")
    plt.yscale("log")
    plt.title("Ефект метелика — різниця через малу похибку")
    plt.xlabel("Час")
    plt.ylabel("Відхилення (log шкала)")
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_attractor():
    state = [1.0, 1.0, 1.0]
    _, sol = solve_lorenz(state)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(sol[0], sol[1], sol[2], lw=0.5)
    ax.set_title("Атрактор Лоренца")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()