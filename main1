import numpy as np
from body import Body
from velocity_field import VelocityField
from solver import RungeKuttaSolver
from plotter import Plotter
from trajectory import Trajectory

def load_config():
    try:
        config = {}
        with open('geometry_config.txt', 'r') as f:
            for line in f:
                if ':' in line and not line.startswith('#'):
                    key, value = line.split(':', 1)
                    config[key.strip()] = value.strip()
    except:
        config = {
            'side_length': '3',
            'quarter': '2',
            'A_function': '-sin(t)',
            'B_function': 't',
            'butcher_table': '3.1',
            't0': '0.1',
            't_end': '3.0',
            'dt': '0.05'
        }

    return config

def main():

    # Конфигурация
    print("\n1. ЗАГРУЗКА КОНФИГУРАЦИИ")
    config = load_config()
    for key, value in config.items():
        print(f"  {key}: {value}")

    # Объекты
    print("\n2. СОЗДАНИЕ ОБЪЕКТОВ")

    body = Body()
    body.create_square(
        side=float(config.get('side_length', 3)),
        quarter=int(config.get('quarter', 2))
    )

    vf = VelocityField(
        config.get('A_function', '-sin(t)'),
        config.get('B_function', 't')
    )
    print(f"  Поле скоростей: v1 = sin(t)*x1, v2 = t*x2")

    solver = RungeKuttaSolver(config.get('butcher_table', '3.1'))
    print(f"  Метод: Рунге-Кутта 3-го порядка")

    # Определение системы ОДУ
    def system(t, y):
        x1, x2 = y
        v1, v2 = vf.get_velocity_at_position(t, x1, x2)
        return np.array([v1, v2])

    # Параметры времени
    t0 = float(config.get('t0', 0.1))
    t_end = float(config.get('t_end', 3.0))
    dt = float(config.get('dt', 0.05))

    print(f"  Время: от {t0} до {t_end}, шаг {dt}")

    # Расчет траекторий для всех точек


    trajectories = []


    for i, point in enumerate(body.points):
        # Интегрируем траектории
        t_vals, y_vals = solver.solve(system, t0, [point.x1, point.x2], t_end, dt)

        # Создаем объект траектории
        traj = Trajectory(point_id=i)

        # Сохраняем все точки траектории
        for t, pos in zip(t_vals, y_vals):
            traj.add_point(t, pos[0], pos[1])
            point.add_position(t, pos[0], pos[1])

        trajectories.append(traj)

        # Прогресс
        if i < 3:
            init = traj.get_initial_position()
            final = traj.get_final_position()


    # Также интегрируем угловые точки
    for corner in body.corner_points:
        t_vals, y_vals = solver.solve(system, t0, [corner.x1, corner.x2], t_end, dt)
        for t, pos in zip(t_vals, y_vals):
            corner.add_position(t, pos[0], pos[1])



    # Визуализация


    plotter = Plotter()

    # График 1: Квадрат и траектории

    plotter.plot_square_trajectories_large(body, trajectories, max_scale=10)

    # График 2: Линии тока
    plotter.plot_streamlines_simple(vf, times=[0.5, 1.0, 2.0, 3.0])

    # График 3: Деформированные квадраты
    plotter.plot_deformed_squares_simple(body, times=[0.5, 1.0, 2.0, 3.0])

    # График 4: Векторные поля
    plotter.plot_velocity_fields_simple(vf, times=[0.5, 1.0, 2.0, 3.0])

    print("ПРОГРАММА ВЫПОЛНЕНА УСПЕШНО!")
    print("Созданы файлы:")
    print("  1. square_trajectories_large.png - Квадрат и траектории")
    print("  2. streamlines_simple.png - Линии тока при t=0.5,1,2,3")
    print("  3. deformed_squares_simple.png - Деформация квадрата во времени")
    print("  4. velocity_fields_simple.png - Векторные поля скоростей")

if __name__ == "__main__":
    main()