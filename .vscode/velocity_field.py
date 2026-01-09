import numpy as np

class VelocityField:
    def __init__(self, A_str="-sin(t)", B_str="t"):
        self.A_str = A_str
        self.B_str = B_str

        if A_str == "-sin(t)":
            self.A_func = lambda t: -np.sin(t)
        else:
            self.A_func = lambda t: eval(A_str.replace('t', str(t)))

        if B_str == "t":
            self.B_func = lambda t: t
        else:
            self.B_func = lambda t: eval(B_str.replace('t', str(t)))

    def get_velocity_at_position(self, t, x1, x2):
        v1 = -self.A_func(t) * x1
        v2 = self.B_func(t) * x2
        return v1, v2

    def get_velocity_field(self, t, x1_grid, x2_grid):
        X1, X2 = np.meshgrid(x1_grid, x2_grid)
        V1 = -self.A_func(t) * X1
        V2 = self.B_func(t) * X2
        return V1, V2