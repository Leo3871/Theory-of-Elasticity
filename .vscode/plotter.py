import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Polygon

class Plotter:

    def __init__(self):
        self.colors = plt.cm.tab10(np.linspace(0, 1, 10))
        plt.style.use('seaborn-v0_8-darkgrid')

    def plot_square_trajectories_large(self, body, trajectories, max_scale=10):

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

        side = body.side_length

        # Начальный квадрат и все траектории
        rect = Rectangle((-side, 0), side, side,
                         linewidth=3, edgecolor='red',
                         facecolor='none', linestyle='-',
                         label='Начальный квадрат', alpha=0.8)
        ax1.add_patch(rect)

        # Все траектории
        for traj in trajectories:
            if hasattr(traj, 'positions'):
                positions = np.array(traj.positions)
                if len(positions) > 0:
                    ax1.plot(positions[:, 0], positions[:, 1],
                             'b-', alpha=0.15, linewidth=0.8)

        # Начальные точки
        for point in body.points:
            ax1.scatter(point.x1, point.x2, c='red', s=15, alpha=0.7)

        ax1.set_title('Квадрат и траектории движения\n(масштаб увеличен до 10)',
                      fontsize=14, fontweight='bold')
        ax1.set_xlabel('$x_1$', fontsize=12)
        ax1.set_ylabel('$x_2$', fontsize=12)
        ax1.axhline(0, color='black', linewidth=1)
        ax1.axvline(0, color='black', linewidth=1)
        ax1.grid(True, alpha=0.3)
        ax1.legend(fontsize=11)
        ax1.set_aspect('equal', adjustable='box')
        ax1.set_xlim([-max_scale, max_scale])
        ax1.set_ylim([-max_scale, max_scale])

        # Выделенные траектории с метками
        selected_indices = [0, len(body.points) // 4, len(body.points) // 2,
                            3 * len(body.points) // 4, len(body.points) - 1]
        labels = ['A (левый нижний)', 'B (левый центр)', 'C (центр)',
                  'D (правый центр)', 'E (правый верхний)']

        for idx, label, color in zip(selected_indices, labels, self.colors):
            if idx < len(trajectories) and idx < len(body.points):
                point = body.points[idx]
                traj = trajectories[idx]

                if hasattr(traj, 'positions') and len(traj.positions) > 0:
                    positions = np.array(traj.positions)

                    # Траектория
                    ax2.plot(positions[:, 0], positions[:, 1],
                             color=color, linewidth=2.5,
                             label=f'{label}\n({point.x1:.1f}, {point.x2:.1f})')

                    # Начальная точка
                    ax2.scatter(point.x1, point.x2, color=color,
                                s=120, marker='o', edgecolor='black', linewidth=1.5)

                    # Конечная точка
                    if hasattr(traj, 'get_final_position'):
                        final_pos = traj.get_final_position()
                        ax2.scatter(final_pos[0], final_pos[1], color=color,
                                    s=120, marker='s', edgecolor='black', linewidth=1.5)

        # Начальный квадрат
        rect2 = Rectangle((-side, 0), side, side,
                          linewidth=2, edgecolor='black',
                          facecolor='none', linestyle='--', alpha=0.5)
        ax2.add_patch(rect2)

        ax2.set_title('Траектории характерных точек', fontsize=14, fontweight='bold')
        ax2.set_xlabel('$x_1$', fontsize=12)
        ax2.set_ylabel('$x_2$', fontsize=12)
        ax2.axhline(0, color='black', linewidth=1)
        ax2.axvline(0, color='black', linewidth=1)
        ax2.grid(True, alpha=0.3)
        ax2.legend(loc='upper right', fontsize=10)
        ax2.set_aspect('equal', adjustable='box')
        ax2.set_xlim([-max_scale, max_scale])
        ax2.set_ylim([-max_scale, max_scale])

        plt.tight_layout()
        plt.savefig('square_trajectories_large.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("График 'Квадрат и траектории' сохранен")

    def plot_streamlines_simple(self, velocity_field, times=[0.5, 1.0, 2.0, 3.0]):
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        axes = axes.flatten()

        # Область построения
        x1_min, x1_max = -5, 2
        x2_min, x2_max = -1, 5

        for idx, t in enumerate(times):
            if idx >= 4:
                break

            ax = axes[idx]

            # Сетка для линий тока
            x1_grid = np.linspace(x1_min, x1_max, 25)
            x2_grid = np.linspace(x2_min, x2_max, 25)
            X1, X2 = np.meshgrid(x1_grid, x2_grid)

            # Вычисляем поле скоростей
            V1, V2 = velocity_field.get_velocity_field(t, x1_grid, x2_grid)

            # Линии тока
            ax.streamplot(X1, X2, V1, V2,
                          color='blue', density=2.0,
                          linewidth=1.2, arrowsize=1.2)

            ax.set_xlabel('$x_1$', fontsize=11)
            ax.set_ylabel('$x_2$', fontsize=11)
            ax.set_title(f'Линии тока при t = {t:.1f}\n'
                         f'$v_1 = sin({t:.1f}) x_1$, $v_2 = {t:.1f} x_2$',
                         fontsize=12, fontweight='bold')
            ax.axhline(0, color='black', linewidth=1)
            ax.axvline(0, color='black', linewidth=1)
            ax.grid(True, alpha=0.3)
            # Ограничиваем область данных
            ax.set_xbound(x1_min, x1_max)
            ax.set_ybound(x2_min, x2_max)

        plt.tight_layout()
        plt.savefig('streamlines_simple.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("График 'Линии тока' сохранен")

    def plot_deformed_squares_simple(self, body, times=[0.5, 1.0, 2.0, 3.0]):

        fig, ax = plt.subplots(figsize=(10, 8))

        # Начальный квадрат
        side = body.side_length
        initial_square = Rectangle((-side, 0), side, side,
                                   linewidth=3, edgecolor='black',
                                   facecolor='none', linestyle='-',
                                   label='Начальный квадрат (t=0)', alpha=1.0)
        ax.add_patch(initial_square)

        # Для деформированных квадратов
        colors = ['red', 'green', 'blue', 'purple']
        labels = ['t=0.5', 't=1.0', 't=2.0', 't=3.0']

        # Деформированные квадраты
        for t, color, label in zip(times, colors, labels):
            # Получаем позиции углов в момент времени t
            corners = []
            for point in body.corner_points:
                pos = point.get_position_at_time(t)
                corners.append([pos[0], pos[1]])

            # Деформированный квадрат
            polygon = Polygon(corners, closed=True,
                              linewidth=2.5, edgecolor=color,
                              facecolor='none', linestyle='--',
                              label=label, alpha=0.8)
            ax.add_patch(polygon)

            # Отмечаем угловые точки
            for corner_pos in corners:
                ax.scatter(corner_pos[0], corner_pos[1],
                           color=color, s=80, alpha=0.7, zorder=5)

        # Внутренние точки в разные моменты времени
        marker_styles = ['o', 's', '^', 'D']
        for t, marker in zip(times, marker_styles):
            for i, point in enumerate(body.points):
                if i % 7 == 0:  # Каждую 7-ю точку
                    pos = point.get_position_at_time(t)
                    ax.scatter(pos[0], pos[1],
                               color='gray', s=15, marker=marker, alpha=0.3)

        ax.set_title('Деформация квадрата во времени', fontsize=16, fontweight='bold')
        ax.set_xlabel('$x_1$', fontsize=14)
        ax.set_ylabel('$x_2$', fontsize=14)
        ax.axhline(0, color='black', linewidth=1.5)
        ax.axvline(0, color='black', linewidth=1.5)
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.legend(fontsize=12, loc='upper right')
        ax.set_aspect('equal', adjustable='datalim')
        ax.set_xbound(-10, 5)
        ax.set_ybound(-5, 15)

        plt.tight_layout()
        plt.savefig('deformed_squares_simple.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("График 'Деформация квадрата' сохранен")

    def plot_velocity_fields_simple(self, velocity_field, times=[0.5, 1.0, 2.0, 3.0]):
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        axes = axes.flatten()

        # Область построения
        x1_range = (-5, 2)
        x2_range = (-1, 5)

        for idx, t in enumerate(times):
            if idx >= 4:
                break

            ax = axes[idx]

            # Сетка для векторного поля
            x1 = np.linspace(x1_range[0], x1_range[1], 15)
            x2 = np.linspace(x2_range[0], x2_range[1], 15)
            X1, X2 = np.meshgrid(x1, x2)

            # Векторное поле
            V1 = np.sin(t) * X1  # v1 = sin(t)*x1
            V2 = t * X2  # v2 = t*x2

            # Простое векторное поле
            ax.quiver(X1, X2, V1, V2,
                      color='blue', scale=100,
                      width=0.005, alpha=0.8)

            ax.set_xlabel('$x_1$', fontsize=11)
            ax.set_ylabel('$x_2$', fontsize=11)
            ax.set_title(f'Поле скоростей при t = {t:.1f}\n'
                         f'$v_1 = sin({t:.1f}) x_1$, $v_2 = {t:.1f} x_2$',
                         fontsize=12, fontweight='bold')
            ax.axhline(0, color='black', linewidth=1)
            ax.axvline(0, color='black', linewidth=1)
            ax.grid(True, alpha=0.3)
            ax.set_xbound(x1_range[0], x1_range[1])
            ax.set_ybound(x2_range[0], x2_range[1])

        plt.tight_layout()
        plt.savefig('velocity_fields_simple.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("График 'Векторные поля скоростей' сохранен")