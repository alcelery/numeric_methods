# Практика на третем занятии 10.11.2026

import numpy as np

print("---- Пункт 1 ----\n")
base = np.arange(24)
arr = base.reshape(6, 4)

print(arr.shape)   # (6, 4)
print(arr.ndim)    # 2
print(arr.size)    # 24
print(arr.dtype)   # int64

print("\n---- Пункт 2 ----\n")

arr_46 = arr.reshape(4, 6)
arr_234 = arr_46.reshape(2, 3, 4)
arr_flat = arr_234.reshape(24,)  

print("Значения не изменились:", np.array_equal(base, arr_flat)) 

print("\n---- Пункт 3 ----\n")

col = arr[:, 2]
print(f"Столбец: {col}")

col[0] = 999

print(f"\nСрез после изменения:  {col}")
print(f"Оригинальный массив arr после изменения среза:\n{arr}")
print("Это view")

print("\n---- Пункт 4 ----\n")

mask = arr > 10
filtered_elements = arr[mask]
mean_value = filtered_elements.mean()

print(f"Булева маска:\n{mask}")
print(f"\nОтфильтрованные элементы: {filtered_elements}")
print(f"\nИх среднее: {mean_value}")

print("\n---- Пункт 5 ----\n")

row_means = arr.mean(axis=1, keepdims=True)

print("Средние по строкам:")
print(row_means)

arr_centered = arr - row_means

print("\nРезультат:")
print(arr_centered)

print("\nФорма сохранилась:", arr_centered.shape == arr.shape)

row_sums = arr_centered.sum(axis=1)
print("Суммы по строкам:", row_sums)
print("Суммы ≈ 0:", np.allclose(row_sums, 0))