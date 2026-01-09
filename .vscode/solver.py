import numpy as np

class RungeKuttaSolver:
    def __init__(self, butcher_table="3.1"):
        self.table = butcher_table

    def solve(self, f, t0, y0, t_end, dt=0.05):
        n = int((t_end - t0) / dt) + 1
        t_vals = np.linspace(t0, t_end, n)
        y_vals = np.zeros((n, len(y0)))
        y_vals[0] = y0

        for i in range(1, n):
            t = t_vals[i - 1]
            y = y_vals[i - 1]
            h = dt

            k1 = f(t, y)
            k2 = f(t + h / 2, y + h / 2 * k1)
            k3 = f(t + h, y - h * k1 + 2 * h * k2)

            y_new = y + h * (k1 / 6 + 2 * k2 / 3 + k3 / 6)
            y_vals[i] = y_new

        return t_vals, y_vals