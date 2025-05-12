import unittest
import numpy as np
from lorenz import solve_lorenz

class TestLorenz(unittest.TestCase):
    def test_sensitivity(self):
        _, sol1 = solve_lorenz([1.0, 1.0, 1.0])
        _, sol2 = solve_lorenz([1.000001, 1.0, 1.0])
        diff = np.linalg.norm(sol1 - sol2, axis=0)
        self.assertGreater(diff[-1], 1.0)

if __name__ == "__main__":
    unittest.main()