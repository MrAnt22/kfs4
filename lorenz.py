import numpy as np
from scipy.integrate import solve_ivp

def lorenz(t, state, sigma=10.0, rho=28.0, beta=8.0 / 3.0):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]

def solve_lorenz(initial_state, t_max=40, num_points=10000):
    t = np.linspace(0, t_max, num_points)
    sol = solve_ivp(lorenz, [0, t_max], initial_state, t_eval=t)
    return sol.t, sol.y