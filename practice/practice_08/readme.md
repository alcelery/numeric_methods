# Практическая работа: Задачи на отработку (2 задачи)

**Студент:** Кошина Александра Олеговна
**Дата:** 25.11.2026

## Задача 1. Сравнить методы на функции с плохим стартом
**Условие.** Дана функция f(x) = x³ − 2x + 2. У неё один действительный корень (около −1.769).
1. Постройте график на [−3, 3]. Убедитесь, что корень один.
2. Запустите метод Ньютона с x0 = 0. Что происходит? Почему метод не сходится? (Подсказка: постройте журнал и посмотрите на f′(xk).)
3. Запустите метод Ньютона с x0 = −2. Сколько итераций?
4. Запустите метод секущих с x0 = −2, x1 = −1. Сколько итераций?
5. Запустите бисекцию на [−2, −1]. Сколько итераций?
6. Постройте таблицу: метод → старт → корень → итераций. Объясните, почему метод Ньютона с x0 = 0 «застревает».

### Скрипт:

``` python
# ── Задание 1 ──────────────────────────────
# Функцию и производная
f = lambda x: x**3 - 2*x + 2
df = lambda x: 3*x**2 - 2

# График
x_plot = np.linspace(-3, 3, 400)
y_plot = f(x_plot)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_plot, y_plot, label="f(x) = x³ - 2x + 2", color="blue", linewidth=2)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("f(x)", fontsize=12)
ax.set_title("График функции f(x) = x³ - 2x + 2 на [-3, 3]", fontsize=14, fontweight="bold")
ax.grid(True, alpha=0.3)
ax.legend()
plt.show()

print("\n--- Метод Ньютона с x0 = 0 ---")
try:
    root_n0, jn0, status_n0 = newton(f, df, x0=0, eps=1e-9)
    print_journal_newton(jn0, "Ньютон: x0 = 0")
    print(f"Корень: {root_n0:.6f}, статус: {status_n0}, итераций: {len(jn0)}")
except Exception as e:
    print(f"Ошибка при запуске: {e}")

print("\n--- Метод Ньютона с x0 = -2 ---")
root_n2, jn2, status_n2 = newton(f, df, x0=-2, eps=1e-9)
print_journal_newton(jn2, "Ньютон: x0 = -2")
print(f"Корень: {root_n2:.12f}, статус: {status_n2}, итераций: {len(jn2)}")

print("\n--- Метод секущих с x0 = -2, x1 = -1 ---")
root_s, js, status_s = secant(f, x0=-2, x1=-1, eps=1e-9)
print_journal_secant(js, "Секущие: x0 = -2, x1 = -1")
print(f"Корень: {root_s:.12f}, статус: {status_s}, итераций: {len(js)}")

print("\n--- Бисекция на [-2, -1] ---")
root_b, jb, status_b = bisection(f, a=-2, b=-1, eps=1e-9)
print_journal(jb, "Бисекция: [-2, -1]")
print(f"Корень: {root_b:.12f}, статус: {status_b}, итераций: {len(jb)}")


print("\n--- Таблица метод → старт → корень → итераций ---")
print(f"{'Метод':>15} | {'Старт':>15} | {'Корень':>12} | {'Итераций':>9} | {'Статус':>15}")
print("-" * 80)

if status_n0 in ['max_iter', 'zero_derivative']:
    status_n0_str = "Застрял (max_iter)" if status_n0 == 'max_iter' else "Деление на 0"
else:
    status_n0_str = status_n0

print(f"{'Ньютон':>15} | {'x0 = 0':>15} | {root_n0:>12.4f} | {len(jn0):>9} | {status_n0_str:>15}")
print(f"{'Ньютон':>15} | {'x0 = -2':>15} | {root_n2:>12.4f} | {len(jn2):>9} | {status_n2:>15}")
print(f"{'Секущие':>15} | {'x0=-2, x1=-1':>15} | {root_s:>12.4f} | {len(js):>9} | {status_s:>15}")
print(f"{'Бисекция':>15} | {'[-2, -1]':>15} | {root_b:>12.4f} | {len(jb):>9} | {status_b:>15}")


print("\nВыбор начального приближения критичен для метода Ньютона.")
print("При x0 = 0 производная f'(0) = -2 (не ноль), но метод попадает в цикл.")
print("f(x) и f'(x) начинают повторяться (x уходит в бесконечность или цикл).")
print("При x0 = -2 и метода секущих сходимость быстрая (около 5-6 итераций).")
print("Метод бисекции надежен, но требует больше итераций (около 30).")
```

### График:

![График](img\t1_graph.png)

### Журналы:

![Таблица](img\t1_tab1.png)

![Таблица](img\t1_tab2.1.png)

![Таблица](img\t1_tab2.2.png)

![Таблица](img\t1_tab3.png)

![Таблица](img\t1_tab4.png)

### Таблица:

![Таблица](img\t1_tab5.png)

### Вывод:

![Вывод](img\t1_itog.png)

## Задача 2. Уравнение с параметром: e^x − kx = 0

**Условие.** Рассмотрите уравнение f(x) = ex − kx = 0, где k > 0 — параметр.
1. Для k = 1 уравнение не имеет действительных корней (проверьте: минимум f(x) равен 1 − ln 1 = 1 > 0).
2. Для k = e уравнение имеет один корень x = 1 (касание). Проверьте: f(1) = e − e · 1 = 0, f′(1) = e − e = 0. Метод Ньютона здесь не работает (деление на ноль). Метод секущих — тоже (знаменатель → 0). Бисекция — не работает (нет смены знака). Объясните, почему.
3. Для k = 3 уравнение имеет два корня. Найдите их методами Ньютона, секущих и бисекции. Постройте таблицу: метод → корень → итераций.
4. Для k = 5 повторите. Сравните число итераций.
5. Постройте график зависимости корней от k (для k от e до 10 с шагом 0.1). Как
ведут себя корни при k → e+? При k → ∞?

### Скрипт:
``` python
# ── Задание 2 ──────────────────────────────
print("\n--- Теоретическая проверка ---")
print("f(x) = e^x - kx,  f'(x) = e^x - k")
print("Условие экстремума: f'(x) = 0 => e^x = k , тогда  x = ln(k)")
print("Минимум функции: f(ln(k)) = k - k*ln(k) = k(1 - ln(k))")

k1 = 1
x_min1 = math.log(k1)
f_min1 = k1 * (1 - math.log(k1))
print(f"Для k=1: минимум в x={x_min1:.2f}, f_min={f_min1:.2f}. Корней нет (минимум > 0).")

k_e = math.e
x_min_e = math.log(k_e)
f_min_e = k_e * (1 - math.log(k_e))
print(f"Для k=e: минимум в x={x_min_e:.2f}, f_min={f_min_e:.2e}. Один корень (касание).")
print("Метод Ньютона: f'(x)=0, деление на ноль. Секущие: f(x_prev) прмиерно равен f(x_curr), знаменатель ≈ 0.")
print("Бисекция: f(x) >= 0 везде, нет смены знака.")



def solve_for_k(k):
    f = lambda x: np.exp(x) - k * x
    df = lambda x: np.exp(x) - k
    
    print(f"\nAнализ для k = {k}")
    
    x_peak = math.log(k)
    intervals = []
    if k == 3:
        # x=0.6 и x=1.5
        intervals = [(0.1, 0.9), (1.1, 2.0)] 
    elif k == 5:
        # x=0.2 и x=2.5
        intervals = [(0.1, 0.5), (1.5, 3.0)]    
    results = []
    
    for i, (a, b) in enumerate(intervals):
        print(f"\n-- Поиск корня #{i+1} на интервале [{a}, {b}] --")
        
        x0_newton = (a + b) / 2 
        try:
            root_n, jn, status_n = newton(f, df, x0=x0_newton, eps=1e-9)
            iter_n = len(jn) if status_n == 'ok' else "Не сош."
        except:
            root_n, iter_n, status_n = None, "Ошибка", "error"
            
        x0_sec, x1_sec = a, b
        try:
            root_s, js, status_s = secant(f, x0=x0_sec, x1=x1_sec, eps=1e-9)
            iter_s = len(js) if status_s == 'ok' else "Не сош."
        except:
            root_s, iter_s, status_s = None, "Ошибка", "error"

        try:
            root_b, jb, status_b = bisection(f, a, b, eps=1e-9)
            iter_b = len(jb) if status_b == 'ok' else "Не сош."
        except Exception as e:
            root_b, iter_b, status_b = None, "Ошибка", str(e)

        results.append({
            'interval': f"[{a}, {b}]",
            'newton': (root_n, iter_n),
            'secant': (root_s, iter_s),
            'bisect': (root_b, iter_b)
        })

    # Вывод таблицы для текущего k
    print(f"\nk = {k}:")
    print(f"{'Метод':>12} | {'Интервал':>10} | {'Корень':>12} | {'Итераций':>10}")
    print("-" * 55)
    for r in results:
        print(f"{'Ньютон':>12} | {r['interval']:>10} | {r['newton'][0]:>12.6f} | {r['newton'][1]:>10}")
        print(f"{'Секущие':>12} | {r['interval']:>10} | {r['secant'][0]:>12.6f} | {r['secant'][1]:>10}")
        print(f"{'Бисекция':>12} | {r['interval']:>10} | {r['bisect'][0]:>12.6f} | {r['bisect'][1]:>10}")
        print("-" * 55)

solve_for_k(3)
solve_for_k(5)


print("\n--- График зависимости корней от k ---")
k_array = np.arange(math.e, 10.1, 0.1)
root1_array = []
root2_array = []

for k_val in k_array:
    f_k = lambda x: np.exp(x) - k_val * x
    a1, b1 = 0.0, math.log(k_val)
    a2, b2 = math.log(k_val), k_val
    
    try:
        r1, _, _ = bisection(f_k, a1 + 1e-5, b1 - 1e-5, eps=1e-6) # чуть отступаем от нуля производной
        root1_array.append(r1)
    except:
        root1_array.append(np.nan)
        
    try:
        r2, _, _ = bisection(f_k, a2 + 1e-5, b2, eps=1e-6)
        root2_array.append(r2)
    except:
        root2_array.append(np.nan)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(k_array, root1_array, label="Корень 1 (меньший)", color='blue', linewidth=2)
ax.plot(k_array, root2_array, label="Корень 2 (больший)", color='red', linewidth=2)

ax.set_xlabel("Параметр k", fontsize=12)
ax.set_ylabel("Корень x*", fontsize=12)
ax.set_title("Зависимость корней уравнения e^x - kx = 0 от параметра k", fontsize=14, fontweight="bold")
ax.grid(True, alpha=0.3)
ax.legend()
plt.show()

print("\nВывод")
print("Влияние на число корней:")
print(" - При k < e корней нет ")
print(" - При k = e есть ровно один корень")
print(" - При k > e два действительных корня")
print("Влияние на сходимость методов:")
print(" - При k > e все методы работают. Ньютон и секущие сходятся за 4-7 итераций.  Метод бисекции надежен, но медленный (31 итерация)")
print(" - При k = e (кратный корень) методы теряют сходимость, а именно")
print("     - У ньютона случается деление на ноль, так как f'(x) = 0")
print("     - У секущих знаменатель разности f(x) стремится к нулю")
print("     - У бисекции нет смены знака, так как f(x) >= 0.")
```

### Таблицы: 

![Таблица](img\t2_tab1.png)

![Таблица](img\t2_tab2.png)

### Графики:

![График](img\t2_graph.png)

### Вывод:

![Вывод](img\t2_itog.png)