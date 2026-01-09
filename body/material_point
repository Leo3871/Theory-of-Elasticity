import numpy as np

class MaterialPoint:

    def __init__(self, x1, x2, point_id=None):
        self.x1 = x1
        self.x2 = x2
        self.id = point_id
        self.initial_position = (x1, x2)
        self.trajectory = []
        self.times = []

    def add_position(self, t, x1, x2):
        self.times.append(t)
        self.trajectory.append([float(x1), float(x2)])

    def get_position_at_time(self, t):
        if not self.trajectory:
            return self.initial_position

        if t <= self.times[0]:
            return self.trajectory[0]
        if t >= self.times[-1]:
            return self.trajectory[-1]

        for i in range(len(self.times) - 1):
            if self.times[i] <= t <= self.times[i + 1]:
                alpha = (t - self.times[i]) / (self.times[i + 1] - self.times[i])
                x1 = self.trajectory[i][0] + alpha * (self.trajectory[i + 1][0] - self.trajectory[i][0])
                x2 = self.trajectory[i][1] + alpha * (self.trajectory[i + 1][1] - self.trajectory[i][1])
                return [x1, x2]

        return self.trajectory[-1]