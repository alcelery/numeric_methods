# Практическая работа: Задачи на отработку (2 задачи)

**Студент:** Кошина Александра Олеговна
**Дата:** 25.11.2026

## Задача 1. Найти все корни полинома на заданном отрезке

**Условие.** Дана функция f(x) = x³ − 6x² + 11x − 6. Известно, что у неё три корня: x = 1, 2, 3.
1. Постройте график f(x) на отрезке [0, 4] и визуально определите интервалы,
содержащие каждый корень.
2. Для каждого интервала примените bisection с точностью ε = 10−9.
3. Выведите журнал для каждого корня (три таблицы).
4. Сравните число итераций для трёх корней. Объясните, почему они могут
отличаться (подсказка: длина стартового интервала).
5. Найдите корни аналитически (разложите полином на множители) и сравните с
численным результатом. Оцените абсолютную и относительную погрешность.

### Скрипт:

``` python
# ── Задача 1 ──────────────────────────
def f1(x):
    return x**3 - 6*(x**2) + 11*x - 6


# Бисекция
root1, j1, s1 = bisection(f1, 0.5, 1.5, eps=1e-9)
print_journal(j1, "f(x) = x^3 - 6x^2 + 11x - 6, [0.5, 1.5]")
print(f"корень: {root1:.12f}, f(root) = {f1(root1):.3e}, статус: {s1}")
print(f"итераций: {len(j1)}")

root2, j2, s2 = bisection(f1, 1.5, 2.4, eps=1e-9)
print_journal(j2, "f(x) = x^3 - 6x^2 + 11x - 6, [1.5, 2.4]")
print(f"корень: {root2:.12f}, f(root) = {f1(root2):.3e}, статус: {s2}")
print(f"итераций: {len(j2)}")

root3, j3, s3 = bisection(f1, 2.3, 3.3, eps=1e-9)
print_journal(j3, "f(x) = x^3 - 6x^2 + 11x - 6, [2.3, 3.3]")
print(f"корень: {root3:.12f}, f(root) = {f1(root3):.3e}, статус: {s3}")
print(f"итераций: {len(j3)}")

# График 
x = np.linspace(0, 4, 400)
y = f1(x)

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(x, y, label="f(x) = x^3 - 6x^2 + 11x - 6", color="blue", linewidth=2)
ax.axhline(0, color='black', linewidth=1)

ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("f(x)", fontsize=12)
ax.set_title("График полинома на отрезке [0, 4]", fontsize=14, fontweight="bold")
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n--- Сравнение итераций и теоретическая оценка ---")

roots_data = [
    (1, (0.2, 1.3), root1, j1),
    (2, (1.2, 2.3), root2, j2),
    (3, (2.2, 3.4), root3, j3)
]
eps = 1e-9

print(f"{'Корень':>8} | {'Интервал':>12} | {'Итераций':>9} | {'Δ0 (длина)':>10} | {'Теор. оценка n':>15}")
print("-" * 70)

for idx, (a, b), root, journal in roots_data:
    iters = len(journal)
    delta_0 = b - a
    theo_iters = math.ceil(math.log2(delta_0 / eps))
    
    print(f"{idx:>8} | [{a}, {b}]:>12 | {iters:>9} | {delta_0:>10.1f} | {theo_iters:>15}")

print("\nЧисло итераций зависит от начальной длины интервала Δ0 = b - a")
print("Теоретическая оценка n >= log2(Δ0 / ε) совпадает с практической (с точностью до округления вверх)")


print("\n--- Аналитическое решение и оценка погрешностей ---")

# Аналитическое разложение: f(x) = (x - 1)(x - 2)(x - 3)
exact_roots = [1.0, 2.0, 3.0]

print(f"{'Корень':>8} | {'Численный':>15} | {'Точный':>8} | {'Δ (абс.)':>12} | {'δ (отн.)':>12}")
print("-" * 70)

for (idx, (a, b), root, journal), exact in zip(roots_data, exact_roots):
    abs_error = abs(root - exact)
    rel_error = abs_error / abs(exact) if exact != 0 else abs_error
    
    print(f"{idx:>8} | {root:>15.12f} | {exact:>8.1f} | {abs_error:>12.2e} | {rel_error:>12.2e}")

print("\nВывод:")
print("Полином раскладывается как f(x) = (x-1)(x-2)(x-3). Точные корни: 1, 2, 3")
print("Численные корни совпадают с аналитическими с точностью до 10^-9,")
print("что подтверждает правильность метода бисекции")
```

### Журналы: 

![Журнал корня 1](img\t1_tab1.png)

![Журнал корня 2](img\t1_tab2.png)

![Журнал корня 3](img\t1_tab3.png)

### График:

![График задания 1](img\t1_graph.png)

### Остальное: 

![Таблица](img\t1_tab4.png)

![Таблица](img\t1_tab5.png)


## Задача 2. Бисекция для уравнения с параметром
**Условие.** Рассмотрите уравнение f(x) = cos x − kx = 0, где k > 0 — параметр. Это
уравнение возникает в задачах о равновесии маятника с трением.
1. Для k = 0.5 локализуйте корень на отрезке [0, 2] (проверьте смену знака). Примените бисекцию с ε = 10−9, выведите журнал.
2. Для k = 1, 2, 5 повторите процедуру. Постройте таблицу: k → корень → число итераций → |f(корень)|.
3. Постройте график зависимости корня от k (для k от 0.1 до 10 с шагом 0.1). Как ведёт себя корень при k → 0? При k → ∞? Объясните качественно.
4. Для k = 0.5 измените точность ε: 10−3, 10−6, 10−9, 10−12. Постройте таблицу: ε →число итераций → фактическая ошибка |x − x*|. Сравните с теоретическойоценкой n ≥ log2(Δ0 / ε).
5. Проверьте, что происходит при k = 0: уравнение cos x = 0. Работает ли бисекция на [0, 2]? Почему? Что нужно изменить?

### Скрипт:

``` python
# ── Задача 2 ──────────────────────────
def f2(x):
    return math.cos(x)

print("\n--- Журнал для k = 0.5 на [0, 2] ---")
k_val = 0.5
# Проверка смены знака
f_0 = np.cos(0) - k_val * 0
f_2 = np.cos(2) - k_val * 2
print(f"Проверка знаков: f(0) = {f_0:.3f} (>0), f(2) = {f_2:.3f} (<0). Знаки разные, корень есть.\n")

func_k05 = lambda x: np.cos(x) - k_val * x

root_05, journal_05, status_05 = bisection(func_k05, 0, 2, eps=1e-9)

print_journal(journal_05, "f(x) = cos(x) - 0.5*x, [0, 2]")
print(f"Корень: {root_05:.12f}, f(root): {func_k05(root_05):.3e}, статус: {status_05}")
print(f"Итераций: {len(journal_05)}\n")



print("\n--- Таблица k -> корень -> число итераций---")
print(f"{'k':>3} | {'Корень':>15} | {'Итераций':>10}")
print("-" * 35)

for k in [1, 2, 5]:
    f_k = lambda x, k=k: np.cos(x) - k * x
    root, journal, status = bisection(f_k, 0, 2, eps=1e-9)
    print(f"{k:>3} | {root:>15.9f} | {len(journal):>10}")



print("\n--- График зависимости корня от k ---")
k_array = np.arange(0.1, 10.1, 0.1)
roots_array = []

for k in k_array:
    f_k = lambda x, k=k: np.cos(x) - k * x
    root, _, _ = bisection(f_k, 0, 2, eps=1e-6)
    roots_array.append(root)

fig_k, ax_k = plt.subplots(figsize=(8, 5))
ax_k.plot(k_array, roots_array, color='purple', linewidth=2)
ax_k.set_xlabel("Параметр k", fontsize=12)
ax_k.set_ylabel("Корень x*", fontsize=12)
ax_k.set_title("Зависимость корня от параметра k", fontsize=14, fontweight="bold")
ax_k.grid(True, alpha=0.3)
plt.show()



print("\n--- Таблица точности для k = 0.5 ---")
print(f"{'eps':>8} | {'Итераций':>10} | {'Факт. ошибка |x - x*|':>25}")
print("-" * 50)

x_star = root_05 
eps_values = [1e-3, 1e-6, 1e-9, 1e-12]

for eps_val in eps_values:
    f_k = lambda x: np.cos(x) - 0.5 * x
    root, journal, _ = bisection(f_k, 0, 2, eps=eps_val)
    
    actual_error = abs(root - x_star)
    print(f"{eps_val:>8.0e} | {len(journal):>10} | {actual_error:>25.2e}")


iters_list = []
for eps_val in eps_values:
    f_k = lambda x: np.cos(x) - 0.5 * x
    _, journal, _ = bisection(f_k, 0, 2, eps=eps_val)
    iters_list.append(len(journal))

fig_eps, ax_eps = plt.subplots(figsize=(8, 5))
ax_eps.semilogx(eps_values, iters_list, marker='o', linestyle='-', color='red', linewidth=2)
ax_eps.set_xlabel("Точность eps (логарифмическая шкала)", fontsize=12)
ax_eps.set_ylabel("Число итераций", fontsize=12)
ax_eps.set_title("Зависимость числа итераций от точности (k=0.5)", fontsize=14, fontweight="bold")
ax_eps.grid(True, alpha=0.3, which="both")
ax_eps.invert_xaxis() 
plt.show()


print("\n--- Случай k = 0 ---")
f_k = lambda x, k=0: np.cos(x) - k * x
root, journal, status = bisection(f_k, 0, 2, eps=1e-9)

print_journal(journal, "f(x) = cos(x) - 0.5*x, [0, 2]")
print(f"Корень: {root:.12f}, f(root): {f_k(root):.3e}, статус: {status}")
print(f"Итераций: {len(journal)}\n")

print("Если k=0, то cos(x) = 0")
print("На отрезке [0, 2] корень x = pi/2 примерно равно 1.5708")
print("f(0) = 1 (>0), f(2) = -0.416 (<0) знаки разные, бисекция работает")
print("Если бы мы взяли [0, 1.5], то f(1.5) = 0.07 > 0, знаки одинаковые, тогда выдало бы ошибку")
```

### Журнал для k = 0.5:

![Таблица](img\t2_tab1.png)

### Таблицы:

![Таблица](img\t2_tab2.png)

![Таблица](img\t2_tab3.png)

![Таблица](img\t2_tab4.png)

### График «корень vs k»:

![График](img\t2_graph1.png)

### График «итерации vs ε»:

![График](img\t2_graph2.png)