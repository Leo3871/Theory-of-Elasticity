import numpy as np
from material_point import MaterialPoint

class Body:
    def __init__(self):
        self.points = []
        self.side_length = 3.0
        self.quarter = 2
        self.corner_points = []

    def create_square(self, side=3.0, quarter=2):
        self.side_length = side
        self.quarter = quarter

        print(f"Создание квадрата {side}x{side} в {quarter}-й четверти")

        x1_vals = np.linspace(-side, -0.1, 7)
        x2_vals = np.linspace(0.1, side, 7)

        for i, x1 in enumerate(x1_vals):
            for j, x2 in enumerate(x2_vals):
                point_id = f"p_{i}_{j}"
                self.points.append(MaterialPoint(x1, x2, point_id))

        # Угловые точки для контура
        self.corner_points = [
            MaterialPoint(-side, 0.1, "bottom_left"),
            MaterialPoint(-0.1, 0.1, "bottom_right"),
            MaterialPoint(-0.1, side, "top_right"),
            MaterialPoint(-side, side, "top_left"),
            MaterialPoint(-side, 0.1, "bottom_left_close")
        ]

        print(f"Создано точек: {len(self.points)} + 5 угловых")