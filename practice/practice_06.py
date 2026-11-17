import numpy as np
import math
import matplotlib.pyplot as plt


def task1():
    print("Задание 1")
    # ── 1. Исходный набор точек ───────────────────────────────
    points_list = []

    for k in range(6):
        x = math.cos(2 * math.pi * k / 6)
        y = math.sin(2 * math.pi * k / 6)
        points_list.append([x, y])

    points_list.append(points_list[0])
    hexagon = np.array(points_list)

    # ── 2. Матрицы преобразований ──────────────────────────────

    # Поворот на 45° против часовой стрелки
    theta = np.deg2rad(45)
    rotate_45 = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    # Отражение относительно прямой y = x
    # Матрица дана в условии (0 1; 1 0)
    reflect_yx = np.array([
        [0.0, 1.0],
        [1.0, 0.0]
    ])

    # ── 3. Применяем преобразования ────────────────────────────
    rotated = hexagon @ rotate_45.T
    reflected = hexagon @ reflect_yx.T

    # ── 4. Визуализация ────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(7, 7))

    ax.plot(hexagon[:, 0], hexagon[:, 1], 'o-', color='gray', 
            label='Исходный', lw=2, markersize=6)
    ax.plot(rotated[:, 0], rotated[:, 1], 'o-', color='steelblue', 
            label='Повёрнутый на 45°', lw=2, markersize=6)
    ax.plot(reflected[:, 0], reflected[:, 1], 'o-', color='crimson', 
            label='Отражённый (y=x)', lw=2, markersize=6)

    ax.axhline(0, color='black', lw=0.5)
    ax.axvline(0, color='black', lw=0.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_title('Поворот и отражение правильного шестиугольника')

    plt.tight_layout()
    plt.show()

    # ── 5. Ответ на вопрос из задания ─────────────────────────
    # Сравним матрицу поворота на 90° и матрицу отражения относительно y=x
    rotate_90 = np.array([
        [0.0, -1.0],
        [1.0,  0.0]
    ])

    print("Матрица поворота на 90° (против часовой):")
    print(rotate_90)
    print("\nМатрица отражения относительно y = x:")
    print(reflect_yx)
    print("\nВывод: Отраженный шестиугольник выглядит повернутым, потому что")
    print("матрица отражения относительно y=x совпадает с матрицей поворота на 90°")
    print("с точностью до знака (одна из строк умножена на -1). Это значит, что")
    print("отражение — это своего рода вывернутый поворот, меняющий ориентацию фигуры.")

def task2():
    print("Задание 2")
    # ── 1. Генерация исходных точек ─────────────────────────────
    rng = np.random.default_rng(42)
    points = rng.uniform(-2, 2, size=(200, 2))

    # добавляем третью координату z=1
    # Размерность станет (200, 3)
    points_h = np.hstack((points, np.ones((200, 1))))

    # ── 2. Прямые преобразования (3x3) ─────────────────────────

    # Масштабирование
    S = np.array([
        [1.5, 0.0, 0.0],
        [0.0, 0.5, 0.0],
        [0.0, 0.0, 1.0]
    ])

    # Поворот на 60° 
    theta = np.deg2rad(60)
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0.0],
        [np.sin(theta),  np.cos(theta), 0.0],
        [0.0,            0.0,           1.0]
    ])

    # Перенос на вектор (1, -1)
    T = np.array([
        [1.0, 0.0, 1.0],
        [0.0, 1.0, -1.0],
        [0.0, 0.0, 1.0]
    ])

    # Матрицы умножаются справа налево: T @ R @ S
    M_forward = T @ R @ S

    transformed_h = points_h @ M_forward.T
    transformed = transformed_h[:, :2] # Отбрасываем z-координату для графика

    # ── 3. Обратные преобразования (в обратном порядке) ────────

    # Обратный перенос: (-1, 1)
    T_inv = np.array([
        [1.0, 0.0, -1.0],
        [0.0, 1.0,  1.0],
        [0.0, 0.0,  1.0]
    ])

    # Обратный поворот: -60°
    theta_inv = np.deg2rad(-60)
    R_inv = np.array([
        [np.cos(theta_inv), -np.sin(theta_inv), 0.0],
        [np.sin(theta_inv),  np.cos(theta_inv), 0.0],
        [0.0,               0.0,                1.0]
    ])

    # Обратный масштаб: sx = 1/1.5, sy = 1/0.5
    S_inv = np.array([
        [1/1.5, 0.0,   0.0],
        [0.0,   1/0.5, 0.0],
        [0.0,   0.0,   1.0]
    ])

    # Применяем обратные преобразования в обратном порядке
    M_inverse = S_inv @ R_inv @ T_inv

    # Восстанавливаем точки
    restored_h = transformed_h @ M_inverse.T
    restored = restored_h[:, :2]

    # ── 4. Проверка ────────────────────────────────────────────
    is_close = np.allclose(points, restored, atol=1e-12)
    print(f"Точки восстановлены с точностью 1e-12: {is_close}")

    # ── 5. Визуализация ────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(8, 8))

    # Исходные (синие кружки)
    ax.scatter(points[:, 0], points[:, 1], color='steelblue', alpha=0.5, label='Исходные')
    # Преобразованные (красные крестики)
    ax.scatter(transformed[:, 0], transformed[:, 1], color='crimson', marker='x', alpha=0.7, label='Преобразованные')
    # Восстановленные (зеленые контуры)
    ax.scatter(restored[:, 0], restored[:, 1], facecolors='none', edgecolors='green', s=80, linewidths=1.5, label='Восстановленные')

    ax.axhline(0, color='black', lw=0.5)
    ax.axvline(0, color='black', lw=0.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_title('Исходные, преобразованные и восстановленные точки')

    plt.tight_layout()
    plt.show()


def main():
    task1()
    task2()

main()