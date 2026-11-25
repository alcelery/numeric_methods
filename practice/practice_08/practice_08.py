import numpy as np
import matplotlib.pyplot as plt
import math

def bisection(f, a, b, eps=1e-9, max_iter=200):
    """
        Метод половинного деления с журналом итераций.

        Возвращает: (корень, журнал, статус)
            статус = 'ok' — достигнута точность по длине интервала
            статус = 'f_zero' — f(c) == 0 (точное попадание)
            статус = 'max_iter' — исчерпан лимит итераций
    """

    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError(f"Нет смены знака на [{a}, {b}]: f(a)={fa}, f(b)={fb}")

    journal = [] # список словарей — каждая запись = одна итерация

    for k in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        length = b - a

        # записываем всё, что нужно для аудита
        journal.append({
            "iter": k,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": fc,
            "length": length,
        })

        # условия остановки
        if fc == 0:
            return c, journal, "f_zero"
        if length < eps:
            return c, journal, "ok"

        # обновляем интервал
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return c, journal, "max_iter"

def print_journal(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
        print(f"{'k':>3} | {'a':>12} | {'b':>12} | {'c':>12} | {'f(c)':>14} | {'b-a':>10}")
        print("-" * 80)
        for row in journal:
            print(f"{row['iter']:>3} | {row['a']:>12.6f} | {row['b']:>12.6f} | {row['c']:>12.6f} | {row['f(c)']:>14.3e} | {row['length']:>10.2e}")


def newton(f, df, x0, eps=1e-12, max_iter=100):
    """
    Метод Ньютона (касательных).
    Возвращает: (корень, журнал, статус)
    """
    journal = []
    x = x0
    for k in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            return x, journal, "zero_derivative"
        x_new = x - fx / dfx
        journal.append({
        "iter": k,
        "x": x,
        "f(x)": fx,
        "f'(x)": dfx,
        "x_new": x_new,
        "step": abs(x_new - x),
        })
        if abs(x_new - x) < eps or abs(fx) < eps:
            return x_new, journal, "ok"
        x = x_new
    return x, journal, "max_iter"

def secant(f, x0, x1, eps=1e-12, max_iter=100):
    """
    Метод секущих.
    Возвращает: (корень, журнал, статус)
    """
    journal = []
    x_prev, x_curr = x0, x1
    f_prev, f_curr = f(x_prev), f(x_curr)

    for k in range(1, max_iter + 1):
        if f_curr - f_prev == 0:
            return x_curr, journal, "zero_denominator"
        x_new = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
        journal.append({
        "iter": k,
        "x_prev": x_prev,
        "x_curr": x_curr,
        "f_curr": f_curr,
        "x_new": x_new,
        "step": abs(x_new - x_curr),
        })
        if abs(x_new - x_curr) < eps or abs(f_curr) < eps:
            return x_new, journal, "ok"
        x_prev, f_prev = x_curr, f_curr
        x_curr = x_new
        f_curr = f(x_curr)
    return x_curr, journal, "max_iter"

def print_journal_newton(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'x':>14} | {'f(x)':>14} | {'f\'(x)':>14} | {'шаг':>10}")
    print("-" * 70)
    for row in journal:
        print(f"{row['iter']:>3} | {row['x']:>14.10f} | {row['f(x)']:>14.3e} | "
        f"{row['f\'(x)']:>14.3e} | {row['step']:>10.2e}")

def print_journal_secant(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'x_prev':>14} | {'x_curr':>14} | {'f_curr':>14} | {'шаг'::>10}")
    print("-" * 70)
    for row in journal:
        print(f"{row['iter']:>3} | {row['x_prev']:>14.10f} | {row['x_curr']:>14.6f} |"
        f"{row['f_curr']:>14.3e} | {row['step']:>10.2e}")




# # ── Задание 1 ──────────────────────────────
# # Функцию и производная
# f = lambda x: x**3 - 2*x + 2
# df = lambda x: 3*x**2 - 2

# # График
# x_plot = np.linspace(-3, 3, 400)
# y_plot = f(x_plot)

# fig, ax = plt.subplots(figsize=(8, 5))
# ax.plot(x_plot, y_plot, label="f(x) = x³ - 2x + 2", color="blue", linewidth=2)
# ax.axhline(0, color='black', linewidth=1)
# ax.axvline(0, color='black', linewidth=1)
# ax.set_xlabel("x", fontsize=12)
# ax.set_ylabel("f(x)", fontsize=12)
# ax.set_title("График функции f(x) = x³ - 2x + 2 на [-3, 3]", fontsize=14, fontweight="bold")
# ax.grid(True, alpha=0.3)
# ax.legend()
# plt.show()

# print("\n--- Метод Ньютона с x0 = 0 ---")
# try:
#     root_n0, jn0, status_n0 = newton(f, df, x0=0, eps=1e-9)
#     print_journal_newton(jn0, "Ньютон: x0 = 0")
#     print(f"Корень: {root_n0:.6f}, статус: {status_n0}, итераций: {len(jn0)}")
# except Exception as e:
#     print(f"Ошибка при запуске: {e}")

# print("\n--- Метод Ньютона с x0 = -2 ---")
# root_n2, jn2, status_n2 = newton(f, df, x0=-2, eps=1e-9)
# print_journal_newton(jn2, "Ньютон: x0 = -2")
# print(f"Корень: {root_n2:.12f}, статус: {status_n2}, итераций: {len(jn2)}")

# print("\n--- Метод секущих с x0 = -2, x1 = -1 ---")
# root_s, js, status_s = secant(f, x0=-2, x1=-1, eps=1e-9)
# print_journal_secant(js, "Секущие: x0 = -2, x1 = -1")
# print(f"Корень: {root_s:.12f}, статус: {status_s}, итераций: {len(js)}")

# print("\n--- Бисекция на [-2, -1] ---")
# root_b, jb, status_b = bisection(f, a=-2, b=-1, eps=1e-9)
# print_journal(jb, "Бисекция: [-2, -1]")
# print(f"Корень: {root_b:.12f}, статус: {status_b}, итераций: {len(jb)}")


# print("\n--- Таблица метод → старт → корень → итераций ---")
# print(f"{'Метод':>15} | {'Старт':>15} | {'Корень':>12} | {'Итераций':>9} | {'Статус':>15}")
# print("-" * 80)

# if status_n0 in ['max_iter', 'zero_derivative']:
#     status_n0_str = "Застрял (max_iter)" if status_n0 == 'max_iter' else "Деление на 0"
# else:
#     status_n0_str = status_n0

# print(f"{'Ньютон':>15} | {'x0 = 0':>15} | {root_n0:>12.4f} | {len(jn0):>9} | {status_n0_str:>15}")
# print(f"{'Ньютон':>15} | {'x0 = -2':>15} | {root_n2:>12.4f} | {len(jn2):>9} | {status_n2:>15}")
# print(f"{'Секущие':>15} | {'x0=-2, x1=-1':>15} | {root_s:>12.4f} | {len(js):>9} | {status_s:>15}")
# print(f"{'Бисекция':>15} | {'[-2, -1]':>15} | {root_b:>12.4f} | {len(jb):>9} | {status_b:>15}")


# print("\nВыбор начального приближения критичен для метода Ньютона.")
# print("При x0 = 0 производная f'(0) = -2 (не ноль), но метод попадает в цикл.")
# print("f(x) и f'(x) начинают повторяться (x уходит в бесконечность или цикл).")
# print("При x0 = -2 и метода секущих сходимость быстрая (около 5-6 итераций).")
# print("Метод бисекции надежен, но требует больше итераций (около 30).")



# # ── Задание 2 ──────────────────────────────
# print("\n--- Теоретическая проверка ---")
# print("f(x) = e^x - kx,  f'(x) = e^x - k")
# print("Условие экстремума: f'(x) = 0 => e^x = k , тогда  x = ln(k)")
# print("Минимум функции: f(ln(k)) = k - k*ln(k) = k(1 - ln(k))")

# k1 = 1
# x_min1 = math.log(k1)
# f_min1 = k1 * (1 - math.log(k1))
# print(f"Для k=1: минимум в x={x_min1:.2f}, f_min={f_min1:.2f}. Корней нет (минимум > 0).")

# k_e = math.e
# x_min_e = math.log(k_e)
# f_min_e = k_e * (1 - math.log(k_e))
# print(f"Для k=e: минимум в x={x_min_e:.2f}, f_min={f_min_e:.2e}. Один корень (касание).")
# print("Метод Ньютона: f'(x)=0, деление на ноль. Секущие: f(x_prev) прмиерно равен f(x_curr), знаменатель ≈ 0.")
# print("Бисекция: f(x) >= 0 везде, нет смены знака.")



# def solve_for_k(k):
#     f = lambda x: np.exp(x) - k * x
#     df = lambda x: np.exp(x) - k
    
#     print(f"\nAнализ для k = {k}")
    
#     x_peak = math.log(k)
#     intervals = []
#     if k == 3:
#         # x=0.6 и x=1.5
#         intervals = [(0.1, 0.9), (1.1, 2.0)] 
#     elif k == 5:
#         # x=0.2 и x=2.5
#         intervals = [(0.1, 0.5), (1.5, 3.0)]    
#     results = []
    
#     for i, (a, b) in enumerate(intervals):
#         print(f"\n-- Поиск корня #{i+1} на интервале [{a}, {b}] --")
        
#         x0_newton = (a + b) / 2 
#         try:
#             root_n, jn, status_n = newton(f, df, x0=x0_newton, eps=1e-9)
#             iter_n = len(jn) if status_n == 'ok' else "Не сош."
#         except:
#             root_n, iter_n, status_n = None, "Ошибка", "error"
            
#         x0_sec, x1_sec = a, b
#         try:
#             root_s, js, status_s = secant(f, x0=x0_sec, x1=x1_sec, eps=1e-9)
#             iter_s = len(js) if status_s == 'ok' else "Не сош."
#         except:
#             root_s, iter_s, status_s = None, "Ошибка", "error"

#         try:
#             root_b, jb, status_b = bisection(f, a, b, eps=1e-9)
#             iter_b = len(jb) if status_b == 'ok' else "Не сош."
#         except Exception as e:
#             root_b, iter_b, status_b = None, "Ошибка", str(e)

#         results.append({
#             'interval': f"[{a}, {b}]",
#             'newton': (root_n, iter_n),
#             'secant': (root_s, iter_s),
#             'bisect': (root_b, iter_b)
#         })

#     # Вывод таблицы для текущего k
#     print(f"\nk = {k}:")
#     print(f"{'Метод':>12} | {'Интервал':>10} | {'Корень':>12} | {'Итераций':>10}")
#     print("-" * 55)
#     for r in results:
#         print(f"{'Ньютон':>12} | {r['interval']:>10} | {r['newton'][0]:>12.6f} | {r['newton'][1]:>10}")
#         print(f"{'Секущие':>12} | {r['interval']:>10} | {r['secant'][0]:>12.6f} | {r['secant'][1]:>10}")
#         print(f"{'Бисекция':>12} | {r['interval']:>10} | {r['bisect'][0]:>12.6f} | {r['bisect'][1]:>10}")
#         print("-" * 55)

# solve_for_k(3)
# solve_for_k(5)


# print("\n--- График зависимости корней от k ---")
# k_array = np.arange(math.e, 10.1, 0.1)
# root1_array = []
# root2_array = []

# for k_val in k_array:
#     f_k = lambda x: np.exp(x) - k_val * x
#     a1, b1 = 0.0, math.log(k_val)
#     a2, b2 = math.log(k_val), k_val
    
#     try:
#         r1, _, _ = bisection(f_k, a1 + 1e-5, b1 - 1e-5, eps=1e-6) # чуть отступаем от нуля производной
#         root1_array.append(r1)
#     except:
#         root1_array.append(np.nan)
        
#     try:
#         r2, _, _ = bisection(f_k, a2 + 1e-5, b2, eps=1e-6)
#         root2_array.append(r2)
#     except:
#         root2_array.append(np.nan)

# fig, ax = plt.subplots(figsize=(8, 5))
# ax.plot(k_array, root1_array, label="Корень 1 (меньший)", color='blue', linewidth=2)
# ax.plot(k_array, root2_array, label="Корень 2 (больший)", color='red', linewidth=2)

# ax.set_xlabel("Параметр k", fontsize=12)
# ax.set_ylabel("Корень x*", fontsize=12)
# ax.set_title("Зависимость корней уравнения e^x - kx = 0 от параметра k", fontsize=14, fontweight="bold")
# ax.grid(True, alpha=0.3)
# ax.legend()
# plt.show()

# print("\nВывод")
# print("Влияние на число корней:")
# print(" - При k < e корней нет ")
# print(" - При k = e есть ровно один корень")
# print(" - При k > e два действительных корня")
# print("Влияние на сходимость методов:")
# print(" - При k > e все методы работают. Ньютон и секущие сходятся за 4-7 итераций.  Метод бисекции надежен, но медленный (31 итерация)")
# print(" - При k = e (кратный корень) методы теряют сходимость, а именно")
# print("     - У ньютона случается деление на ноль, так как f'(x) = 0")
# print("     - У секущих знаменатель разности f(x) стремится к нулю")
# print("     - У бисекции нет смены знака, так как f(x) >= 0.")