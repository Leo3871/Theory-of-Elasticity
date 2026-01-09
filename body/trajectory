class Trajectory:
    def __init__(self, point_id=None):
        self.point_id = point_id
        self.times = []
        self.positions = []

    def add_point(self, t, x1, x2):
        self.times.append(t)
        self.positions.append((x1, x2))

    def get_initial_position(self):
        return self.positions[0] if self.positions else None

    def get_final_position(self):
        return self.positions[-1] if self.positions else None