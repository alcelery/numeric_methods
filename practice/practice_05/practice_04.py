# Практика на четвертом занятии 10.11.2026

import time
import math
import numpy as np

# Для проверки задачи просто раскоментируйте его и запустите файл

# Задача 1
# m = 10**7
# rng = np.random.default_rng(42).normal(size=m)


# def loop_sum_rows(a):
#     s = 0
#     for x in a: 
#         s += x
#     return s

# def numpy_sum_rows(a):
#     return a.sum()

# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best


# r_loop,  t_loop  = measure(loop_sum_rows,  rng)
# r_numpy, t_numpy = measure(numpy_sum_rows, rng)

# print(f"n = {m}")
# print(f"цикл:   {t_loop*1000:10.2f} мс")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")
# print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}\n")


# print("n          | Цикл (мс)       | NumPy (мс)      | Ускорение")
# print("------------------------------------------------------------")
# print("10**5      | 3.19            | 0.02            | 176.3x")
# print("10**6      | 32.11           | 0.27            | 118.2x")
# print("10**7      | 335.37          | 6.60            | 50.8x")

# print("\n--- Выводы ---")
# print("Разница >10x заметна уже при n = 10^5 (ускорение ~176x).")
# print("Ускорение падает с ростом n, потому что на больших данных скорость ограничена пропускной способностью оперативной памяти.")





# # Задача 2
# n = 10 ** 6
# rng = np.random.default_rng(42)
# m = rng.normal(size=n)



# def loop_mean_std(arr):
#     total_sum = 0.0
#     sum_sq = 0.0
#     n = len(arr)
    
#     for x in arr:
#         total_sum += x
#         sum_sq += x * x
        
#     mean = total_sum / n
#     variance = (sum_sq / n) - (mean ** 2) 
#     std = variance ** 0.5 
    
#     return mean, std


# def numpy_mean_std(arr):
#     return arr.mean(), arr.std()


# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best


# (mean_loop, std_loop), t_loop = measure(loop_mean_std, m)
# (mean_np, std_np), t_numpy = measure(numpy_mean_std, m)

# print(f"n = {n}")
# print(f"цикл:   {t_loop*1000:10.2f} мс")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")
# print("Проверка точности:")
# print(f"Разница в среднем: {abs(mean_loop - mean_np):.2e}") 
# print(f"Разница в std:     {abs(std_loop - std_np):.2e}")

# is_close = abs(std_loop - std_np) < 1e-12
# print(f"Совпадает до 1e-12: {is_close}")

# print("\n--- Выводы ---")
# if is_close:
#     print("На данных около нуля наивная формула дала точный результат.")
#     print("Но если сдвинуть данные (например, к 1000), формула 'в лоб'")
#     print("начнет терять точность. sum_sq станет огромным, и при")
#     print("вычитании (sum_sq/n - mean^2) произойдет 'катастрофическая потеря")
#     print("значимости' из-за ограничений float64.")
# else:
#     print("Формула 'в лоб' потеряла точность из-за вычитания больших чисел.")

# print("NumPy считает std устойчивее, потому что использует")
# print("двухпроходный алгоритм (сначала считает среднее, потом сумму")
# print("квадратов отклонений от него sum((x - mean)^2)).")
# print("А также использует компенсированное суммирование, которое")
# print("минимизирует ошибки округления при сложении миллионов чисел.")




# # Задача 3
# n = 10**6
# rng = np.random.default_rng(42)
# m = rng.normal(size=n)


# def loop_transform(arr):
#     result = [0.0] * len(arr)
#     for i in range(len(arr)):
#         x = arr[i]
#         result[i] = math.sin(x) + x * x
#     return result

# def numpy_transform(arr):
#     return np.sin(arr) + arr ** 2


# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best


# r_loop, t_loop = measure(loop_transform, m)
# r_numpy, t_numpy = measure(numpy_transform, m)


# print(f"n = {n}")
# print(f"Цикл:   {t_loop*1000:10.2f} мс")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс")
# print(f"Ускорение: {t_loop / t_numpy:.1f}x")

# print(f"Результаты совпадают: {np.allclose(r_loop, r_numpy)}")



# print("\n--- Вывод ---")
# print("Список Python выделяет память под каждый объект отдельно.")
# print("Массив NumPy хранит 'сырые' числа типа float64 подряд в одном блоке памяти,")
# print(" поэтому занимает меньше места.")

# print("NumPy-версия короче за счет векторизации. Вместо явного цикла мы применяем операцию ко всему")
# print("массиву сразу. Там это выполняется на быстром C-коде.")

# print("Создается 3 временных массива в памяти:")
# print("- Первый: a**2 (возведение в квадрат)")
# print("- Второй: np.sin(a) (синус)")
# print("- Третий: результат их сложения (массив, который мы возвращаем)")
# print("Цикл же пишет результат сразу в один список, не создавая промежуточных массивов.")





# # Задача 4
# n = 10**6
# rng = np.random.default_rng(42)
# # Чтобы были числа и меньше 0, и больше 1
# a = rng.normal(loc=0.5, scale=1.0, size=n)


# def loop_clip(arr):
#     result = [0.0] * len(arr)
#     for i in range(len(arr)):
#         x = arr[i]
#         if x < 0:
#             result[i] = 0
#         elif x > 1:
#             result[i] = 1
#         else:
#             result[i] = x
#     return result

# def numpy_clip(arr):
#     return np.clip(arr, 0, 1)

# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best

# r_loop, t_loop = measure(loop_clip, a)
# r_numpy, t_numpy = measure(numpy_clip, a)

# print(f"n = {n}")
# print(f"Цикл:   {t_loop*1000:10.2f} мс")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс")
# print(f"Ускорение: {t_loop / t_numpy:.1f}x\n")

# changed_count = np.sum((a < 0) | (a > 1))
# print(f"Элементов было изменено: {changed_count} (из {n})")
# print(f"Результаты совпадают: {np.allclose(r_loop, r_numpy)}")

# print("\n---- Вывод ----")
# print("Версия в лоб требует явного цикла и двух ветвлений условий.")
# print("Версия NumPy вызывает всего одну функцию np.clip(), внутри которой нет")
# print("ни одного цикла и ни одного if на уровне Python. Все делает скомпилированный C-код.")





# # Задача 5
# n = 10**5
# rng = np.random.default_rng(42)
# matrix = rng.normal(size=(n, 10)) 

# def loop_sum_rows(m):
#     n_rows = m.shape[0]
#     n_cols = m.shape[1]
#     result = [0.0] * n_rows
    
#     for i in range(n_rows):
#         s = 0.0
#         for j in range(n_cols):
#             s += m[i, j]
#         result[i] = s
#     return result

# def numpy_sum_rows(m):
#     return m.sum(axis=1)

# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best

# r_loop, t_loop = measure(loop_sum_rows, matrix)
# r_numpy, t_numpy = measure(numpy_sum_rows, matrix)

# print(f"n = {n} (матрица {matrix.shape})")
# print(f"Цикл:   {t_loop*1000:10.2f} мс  | SLOC: 7 строк")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс  | SLOC: 1 строка")
# print(f"Ускорение: {t_loop / t_numpy:.1f}x")
# print(f"Результаты совпадают: {np.allclose(r_loop, r_numpy)}\n")

# print("\n---- Вывод ----")
# print("NumPy-версия в 7 раз короче по SLOC и в разы быстрее.")




# # Задача 6
# n = 10**5
# rng = np.random.default_rng(42)
# matrix = rng.normal(size=(n, 10))

# def loop_center(m):
#     n_rows, n_cols = m.shape
#     result = [[0.0] * n_cols for _ in range(n_rows)]
    
#     for j in range(n_cols):
#         col_sum = 0.0
#         for i in range(n_rows):
#             col_sum += m[i, j]
#         col_mean = col_sum / n_rows
        
#         for i in range(n_rows):
#             result[i][j] = m[i, j] - col_mean
            
#     return result

# def numpy_center(m):
#     return m - m.mean(axis=0)

# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best

# r_loop, t_loop = measure(loop_center, matrix)
# r_numpy, t_numpy = measure(numpy_center, matrix)

# print(f"n = {n} (матрица {matrix.shape})")
# print(f"Цикл:   {t_loop*1000:10.2f} мс")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс")
# print(f"Ускорение: {t_loop / t_numpy:.1f}x")
# print(f"Результаты совпадают: {np.allclose(r_loop, r_numpy)}\n")

# print(f"Средние по столбцам после нормировки (NumPy):\n{numpy_center(matrix).mean(axis=0)}")