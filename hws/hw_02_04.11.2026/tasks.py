import math 
import mpmath
from decimal import Decimal, getcontext
import numpy as np
import sys
import random

# БЛОК 1 

# Задание 1
def task1(): 
    print("\n\t---- Задание 1 ----\n")

    # (Название, Функция f(x), Производная f'(x), Точка x)
    tasks = [
        ("f(x) = sqrt(x)", lambda x: math.sqrt(x), lambda x: 1 / (2 * math.sqrt(x)), 1e-8),
        ("f(x) = ln(x)", lambda x: math.log(x), lambda x: 1 / x, 1.001),
        ("f(x) = x - 1", lambda x: x - 1, lambda x: 1, 1.000001),
        ("f(x) = sin(x)", lambda x: math.sin(x), lambda x: math.cos(x), math.pi / 2)
    ]

    results = []

    for name, func, proiz, x in tasks:
        # Вычисляем значение функции и производной в точке
        fx = func(x)
        fpx = proiz(x)
        
        # cond = |x * f'(x) / f(x)|
        # если f(x) == 0, то обусловленность бесконечна (деление на ноль)
        if abs(fx) < 1e-15: # Обработка случая, близкого к нулю
            cond = float('inf')
        else:
            cond = abs(x * fpx / fx)
        
        results.append((name, x, cond))

        # Вывод результата
        print(f"\t{name} при x = {x}")
        print(f"\t\tf(x)  = {fx}")
        print(f"\t\tf'(x) = {fpx}")
        print(f"\t\tcond  = {cond}")
        
        if cond > 10:
            status = "плохо обусловлена"
        else:
            status = "хорошо обусловлена"
        print(f"\t\tСтатус: {status}\n")

    # Сортировка по возрастанию обусловленности
    results.sort(key=lambda item: item[2])
    
    print("\t--- Рейтинг (от лучшей к худшей) ---")
    for i, (name, x, cond) in enumerate(results, 1):
        print(f"\t{i}. {name} (x={x}): cond = {cond:.4g}")

    print("\n\t--- Вывод по заданию 1 ---")
    print("\tСамая 'опасная' задача: f(x) = x - 1 при x = 1.000001.")
    print("\tЧисло обусловленности огромно (~10^6). Это значит, что малые относительные")
    print("\tпогрешности в x приводят к огромным относительным погрешностям в f(x).")

# Задание 2
def task2():
    print("\n\t---- Задание 2 ----\n")

    print("\t--- Аналитика ---")
    print("\tФункция: f(a, b) = a - b")
    print("\tЧастные производные: df/da = 1, df/db = -1")
    print("\tЧисло обусловленности по 'a': cond = |a * (df/da) / f(a,b)| = |a / (a - b)|")
    print("\tЧисло обусловленности по 'b': cond = |b * (df/db) / f(a,b)| = |-b / (a - b)| = |b / (a - b)|")
    print("\tПри a ≈ b знаменатель (a - b) стремится к 0, поэтому оба cond стремятся к бесконечности.\n")

    print("\t--- Численная проверка ---")
    a = 1 + 10**-8
    b = 1
    delta_a = 10**-9
    
    f_orig = a - b
    
    a_new = a + delta_a
    f_new = a_new - b
    
    delta_f = f_new - f_orig
    
    rel_delta_a = abs(delta_a / a)
    rel_delta_f = abs(delta_f / f_orig)
    
    # cond_a = |a / (a - b)|
    cond_a = abs(a / f_orig)
    
    predicted_rel_error = cond_a * rel_delta_a
    actual_rel_error = rel_delta_f

    print(f"\tВходные данные: a = {a}, b = {b}")
    print(f"\tВозмущение: delta_a = {delta_a}")
    print(f"\tИсходное f(a,b) = {f_orig}")
    print(f"\tНовое f(a+da,b) = {f_new}")
    print(f"\tФактическое изменение df = {delta_f}")
    
    print(f"\n\tЧисло обусловленности cond_a = {cond_a:.1e}")
    print(f"\tОтносительная ошибка входа = {rel_delta_a:.4e}")
    print(f"\tПредсказанная отн. ошибка = {predicted_rel_error:.4e} (cond * отн. ошибка входа)")
    print(f"\tФактическая отн. ошибка = {actual_rel_error:.4e}\n")

    print("\t--- Вывод по заданию 2 ---")
    print("\tЧисло обусловленности огромно, что предсказывает сильное усиление ошибки.")
    print("\tФактическое изменение df и относительная ошибка сопоставимы")
    print("\tс предсказанием теории (относительная ошибка должна быть ~cond * (da/a) или 10%).")
    print("\tЭто подтверждает, что при a ≈ b операция вычитания катастрофически теряет точность.")
    print("\tИзменение входного 'a' на 0.0000001% привело к изменению результата на 10%.")

# Задание 3
def task3():
    print("\n\t---- Задание 3 ----\n")

    # Значения эпсилон
    epsilons = [1e-2, 1e-4, 1e-6]

    print(f"\t{'eps':<10} | {'Сдвиг корня':<15} | {'Отн. сдвиг':<15} | {'Отн. изм. коэф.':<15} | {'Отношение':<10}")
    print("\t" + "-" * 75)

    for eps in epsilons:
        # x^2 - 2x + (1 - eps) = 0
        a = 1.0
        b = -2.0
        c = 1.0 - eps
        
        # Вычисляем дискриминант
        disc = b*b - 4*a*c
        
        if disc < 0:
            print(f"\t{eps:<10.0e} | Нет действительных корней")
            continue
            
        sqrt_disc = math.sqrt(disc)
        
        # Корни по формуле
        x1 = (-b + sqrt_disc) / (2*a)
        x2 = (-b - sqrt_disc) / (2*a)
        
        # Ближайший к 1 корень — это x1 = (2 + sqrt(disc)) / 2 = 1 + sqrt(disc)/2
        shift = abs(x1 - 1.0)
        
        rel_shift = shift / 1.0
        rel_coef_change = eps / 1.0
        ratio = rel_shift / rel_coef_change
        
        print(f"\t{eps:<10.0e} | {shift:<15.4e} | {rel_shift:<15.4e} | {rel_coef_change:<15.4e} | {ratio:<10.1f}")

    print("\n\t--- Вывод по заданию 3---")
    print("\tПри уменьшении eps от 10^-2 до 10^-4, сдвиг корня уменьшается")
    print("\tтолько в 10 раз (так как sqrt(10^-2) = 10^-1, а sqrt(10^-4) = 10^-2).")
    print("\tОтношение сдвигов растет как 1/sqrt(eps). Для eps=10^-6 оно равно 1000.")
    print("\tЭто означает, что малое изменение коэффициента приводит")
    print("\tк относительно большому сдвигу корня.")
    print("\tКорень кратности 2 обладает плохой обусловленностью: ошибка в коэффициенте")
    print("\tусиливается в 1/sqrt(eps) раз.")

# Задание 4
def task4():
    print("\n\t---- Задание 4 ----\n")
    
    getcontext().prec = 50

    def f_bad(x):
        # Прямое вычисление
        return 1.0 / (1.0 + x) - 1.0 / (1.0 - x)

    def f_good(x):
        # Приведение к общему знаменателю
        return -2.0 * x / (1.0 - x * x)

    def f_exact(x):
        # Точное решение
        dx = Decimal(str(x))
        return float(1 / (1 + dx) - 1 / (1 - dx))

    xs = [1e-8, 1e-12, 1e-14, 1e-15, 1e-16]
    
    print(f"\t{'x':>10} | {'bad':>22} | {'good':>22} | {'exact':>22} | {'err_bad':>10} | {'err_good':>10}")
    print("\t" + "-" * 105)

    for x in xs:
        b  = f_bad(x)
        g  = f_good(x)
        ex = f_exact(x)
        
        # Относительную ошибку
        eb = abs(b - ex) / abs(ex) if ex != 0 else 0
        eg = abs(g - ex) / abs(ex) if ex != 0 else 0
        
        print(f"\t{x:>10.0e} | {b:>22.16e} | {g:>22.16e} | {ex:>22.16e} | {eb:>10.2e} | {eg:>10.2e}")

    print("\n\t--- Вывод ---")
    print("\tЗадача вычисления f(x) = 1/(1+x) - 1/(1-x) сама по себе хорошо обусловлена.")
    print("\tУстойчивый алгоритм (good) дает точный ответ на всем диапазоне.")
    print("\tПри прямом расчете при x -> 0 — это катастрофическое сокращение.")
    print("\tПри x = 10^-14 и меньше точность 'bad' катастрофически падает")
    print("\tдостигает 7-10%, так как при вычитании двух почти равных чисел")
    print("\t(1/(1+x) и 1/(1-x)) старшие значащие биты взаимно уничтожаются.")
    print("\tЭто доказывает, что математически верная формула может быть численно неустойчивой.")

# БЛОК 2

# Задание 5
def task5():
    print("\n\t---- Задание 5 ----\n")

    getcontext().prec = 50

    a = 1
    c = 1

    # b для проверки
    bs = [1e8, 1e4, 1e12]

    print(f"\t{'b':>10} | {'bad (x2)':>20} | {'good (x2)':>20} | {'exact':>20} | {'err_bad':>10} | {'err_good':>10}")
    print("\t" + "-" * 105)

    for b in bs:
        # Плохой способ
        disc = math.sqrt(b*b - 4*a*c)
        x2_bad = (-b + disc) / (2 * a)

        # Хороший способ
        x2_good = (2 * c) / (-b - disc)

        # Точное значение
        A = Decimal(str(a))
        B = Decimal(str(b))
        C = Decimal(str(c))
        
        D = B*B - 4*A*C
        sqrt_D = D.sqrt()
        x2_exact_dec = (2 * C) / (-B - sqrt_D)
        x2_exact = float(x2_exact_dec) 

        # Защита от деления на ноль
        err_bad = abs(x2_bad - x2_exact) / abs(x2_exact) if x2_exact != 0 else 0
        err_good = abs(x2_good - x2_exact) / abs(x2_exact) if x2_exact != 0 else 0

        print(f"\t{b:>10.0e} | {x2_bad:>20.12e} | {x2_good:>20.12e} | {x2_exact:>20.12e} | {err_bad:>10.2e} | {err_good:>10.2e}")

    print("\n\t--- Вывод ---")
    print("\tПри b = 10^4 'плохой' способ работает точно.")
    print("\tПри b = 10^8 'плохой' способ начинает сильно ошибаться.")
    print("\tПри b = 10^12 'плохой' способ катастрофически ломается и выдает 0,")
    print("\tхотя истинный корень -10^-12. Относительная ошибка достигает 100%.")
    print("\tПричина: в формуле (-b + sqrt(...)) при больших b происходит")
    print("\tвычитание двух почти равных чисел. В float они")
    print("\tстановятся неразличимы, и результат равен нулю.")
    print("\t'Хороший' способ использует сопряженное выражение, избегая вычитания,")
    print("\tи дает точный результат на всем диапазоне.")

# Задание 6
def task6():
    print("\n\t---- Задание 6 ----\n")

    mpmath.mp.dps = 50 

    def f_bad(x):
        # Прямое вычисление
        return (1.0 - math.cos(x)) / (x * x)

    def f_good(x):
        # Через тождество
        return 2.0 * (math.sin(x / 2.0) / x) ** 2

    xs = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]

    print(f"\t{'x':>10} | {'bad':>16} | {'good':>16} | {'exact':>16} | {'err_bad':>10} | {'err_good':>10}")
    print("\t" + "-" * 95)

    for x in xs:
        b = f_bad(x)
        g = f_good(x)
        
        x_mp = mpmath.mpf(str(x)) 
        ex = float((1 - mpmath.cos(x_mp)) / (x_mp**2))
        
        # Считаем ошибки
        eb = abs(b - ex) / abs(ex) if ex != 0 else 0
        eg = abs(g - ex) / abs(ex) if ex != 0 else 0

        print(f"\t{x:>10.0e} | {b:>16.8e} | {g:>16.8e} | {ex:>16.8e} | {eb:>10.2e} | {eg:>10.2e}")

    print("\n\t--- Вывод ---")
    print("\tСтолбец err_bad показывает рост ошибки при уменьшении x.")
    print("\tПри x = 10^-2 и 10^-4 ошибка еще очень мала (~10^-13 и 10^-5).")
    print("\tПри x = 10^-6 ошибка плохого способа растет, а при x = 10^-8 и меньше")
    print("\tплохой способ выдает 0.0 (относительная ошибка достигает 100%).")
    print("\tЭто потому что при малых x значение cos(x) очень близко к 1.")
    print("\tВычитание 1 - cos(x) приводит к потере старших значащих битов.")
    print("\tХороший способ (через тождество) полностью устраняет")
    print("\tэто вычитание и дает ошибку порядка машинного эпсилон на всем диапазоне.")
    print("\n\tОшибка плохого способа превышает 1% начиная с x = 10^-8.")

# Задание 7
def task7():
    print("\n\t---- Задание 7 ----\n")

    mpmath.mp.dps = 50

    def f_bad(x):
        # Плохой способ
        return math.sqrt(x + 1.0) - math.sqrt(x)

    def f_good(x):
        # Умножение на сопряженное
        return 1.0 / (math.sqrt(x + 1.0) + math.sqrt(x))

    xs = [1e4, 1e8, 1e12, 1e14, 1e16]

    print(f"\t{'x':>10} | {'bad':>20} | {'good':>20} | {'exact':>20} | {'err_bad':>12} | {'err_good':>12}")
    print("\t" + "-" * 110)

    # Запись роста ошибки
    errs_bad = []

    for x in xs:
        b = f_bad(x)
        g = f_good(x)
        
        # Точное значение
        x_mp = mpmath.mpf(str(x))
        ex = float(1 / (mpmath.sqrt(x_mp + 1) + mpmath.sqrt(x_mp)))
        
        # Относительные ошибки
        eb = abs(b - ex) / abs(ex) if ex != 0 else 0
        eg = abs(g - ex) / abs(ex) if ex != 0 else 0
        errs_bad.append(eb)

        print(f"\t{x:>10.0e} | {b:>20.12e} | {g:>20.12e} | {ex:>20.12e} | {eb:>12.2e} | {eg:>12.2e}")

    print("\n\t--- Оценка показателя степени ---")
    if errs_bad[0] > 0 and errs_bad[-1] > 0:
        x_ratio = xs[-1] / xs[0]
        err_ratio = errs_bad[-1] / errs_bad[0]
        k = math.log(err_ratio) / math.log(x_ratio)
        print(f"\tОшибка выросла в {err_ratio:.2e} раз при росте x в {x_ratio:.0e} раз.")
        print(f"\tОценка показателя степени: ошибка ~ O(x^{k:.2f}).")
    else:
        print("\tНевозможно оценить из-за нулевой ошибки.")

    print("\n\t--- Вывод ---")
    print("\tПри x = 10^4 ошибка плохого способа еще очень мала.")
    print("\tОднако при росте x ошибка растет пропорционально x (оценка O(x^1.06)).")
    print("\tПри x = 10^12 ошибка становится заметной, а при x = 10^16")
    print("\tплохой способ выдает 0, так как в float значения x + 1 и x")
    print("\tстановятся абсолютно одинаковыми. Относительная")
    print("\tошибка достигает 100%.")
    print("\tХороший способ дает точный результат на всем диапазоне.")
    print("\tПри вычитании корней больших чисел использовать умножение на сопряженное.")

# Задание 8
def task8():
    print("\n\t---- Задание 8 ----\n")

    mpmath.mp.dps = 50

    def f_bad(x):
        # Плохой способ
        return math.log(1.0 + x)

    def f_good(x):
        # Хороший способ
        return math.log1p(x)

    xs = [1e-2, 1e-8, 1e-12, 1e-16]

    print(f"\t{'x':>10} | {'bad (log(1+x))':>20} | {'good (log1p)':>20} | {'exact':>20} | {'err_bad':>12} | {'err_good':>12}")
    print("\t" + "-" * 110)

    for x in xs:
        b = f_bad(x)
        g = f_good(x)
        
        # Точное значение
        x_mp = mpmath.mpf(str(x))
        ex = float(mpmath.log(1 + x_mp))
        
        # Относительные ошибки
        eb = abs(b - ex) / abs(ex) if ex != 0 else 0
        eg = abs(g - ex) / abs(ex) if ex != 0 else 0

        # Вывод строки таблицы
        print(f"\t{x:>10.0e} | {b:>20.12e} | {g:>20.12e} | {ex:>20.12e} | {eb:>12.2e} | {eg:>12.2e}")

    print("\n\t--- Объяснение работы log1p ---")
    print("\tФункция math.log(1 + x) вычисляет сумму (1 + x) в стандартном float.")
    print("\tПри очень малых x (например, 10^-16) число 1 + x округляется до 1,")
    print("\tтак как x меньше машинного эпсилон. Логарифм от 1 равен 0,")
    print("\tхотя истинный ответ ~10^-16. Отсюда огромная относительная ошибка.")
    print("\tФункция math.log1p(x) внутри не складывает 1 + x напрямую.")
    print("\tОна использует специальные алгоритмы для вычисления ln(1+x)")
    print("\tнапрямую через x, сохраняя точность малых величин.")

    print("\n\t--- Вывод ---")
    print("\tПлохой способ начинает терять точность уже при x = 10^-8,")
    print("\tа при x = 10^-16 полностью ломается, т.к. 1 + 10^-16 округляется до 1,")
    print("\tи результат становится равен 0, а относительная ошибка 100%.")
    print("\tХороший способ дает точный результат на всем диапазоне,")
    print("\tтак как внутри не складывает 1 + x напрямую, а использует")
    print("\tспециальные алгоритмы для малых величин.")
    print("\n\tСтранные функции, например log1p, expm1, hypot являються")
    print("\tчисленно устойчивыми реализациями стандартных")
    print("\tопераций. Они предотвращают катастрофическое сокращение и переполнение")
    print("\tв граничных случаях, где обычные прямые вычесления дают сбой.")

# Задание 9
def task9():
    print("\n\t---- Задание 9 ----\n")

    mpmath.mp.dps = 50

    ns = [10**5, 10**6, 10**7]

    print(f"\t{'n':>10} | {'naive (цикл)':>16} | {'sum(arr)':>16} | {'math.fsum':>16} | {'err_naive':>10} | {'err_sum':>10} | {'err_fsum':>10}")
    print("\t" + "-" * 115)

    errs_naive = []

    for n in ns:
        # Генерируем массив
        arr = [1.0 / k for k in range(1, n + 1)]

        # Наивный цикл
        naive_sum = 0.0
        for val in arr:
            naive_sum += val

        # Функция sum()
        builtin_sum = sum(arr)

        # math.fsum()
        fsum_val = math.fsum(arr)

        # Точное значение
        exact_sum = mpmath.mpf(0)
        for k in range(1, n + 1):
            exact_sum += mpmath.mpf(1) / mpmath.mpf(k)
        
        ex_float = float(exact_sum)

        # Относительные ошибки
        eb = abs(naive_sum - ex_float) / abs(ex_float) if ex_float != 0 else 0
        es = abs(builtin_sum - ex_float) / abs(ex_float) if ex_float != 0 else 0
        ef = abs(fsum_val - ex_float) / abs(ex_float) if ex_float != 0 else 0

        errs_naive.append(eb)

        print(f"\t{n:>10.0e} | {naive_sum:>16.10f} | {builtin_sum:>16.10f} | {fsum_val:>16.10f} | {eb:>10.2e} | {es:>10.2e} | {ef:>10.2e}")

    print("\n\t--- Оценка роста ошибки наивного суммирования ---")
    if len(errs_naive) >= 2 and errs_naive[-2] > 0:
        n_ratio = ns[-1] / ns[-2]
        err_ratio = errs_naive[-1] / errs_naive[-2]
        k = math.log(err_ratio) / math.log(n_ratio)
        print(f"\tПри росте n в {n_ratio:.0f} раз, ошибка выросла в {err_ratio:.1f} раз.")
        print(f"\tОценка показателя степени: ошибка ~ O(n^{k:.2f}).")

    print("\n\t--- Вывод ---")
    print("\tОшибка наивного суммирования растет с увеличением n.")
    print("\tПри n = 10^5 ошибка ~ 7.6e-15 (незаметно).")
    print("\tПри n = 10^6 ошибка ~ 5.1e-14.")
    print("\tПри n = 10^7 ошибка ~ 1.5e-13 (и продолжает расти).")
    print("\tФункция math.fsum() и встроенная sum(arr) дают точный результат")
    print("\tна всем диапазоне (ошибка ~0), так как используют компенсированное суммирование.")
    print("\tОценка роста ошибки наивного суммирования: O(n^0.48).")
    print("\tТеоретически ошибка должна расти как O(n), однако из-за случайного")
    print("\tхарактера округления на малых выборках оценка может колебаться.")
    print("\n\tНаивная сумма становится неприемлемой при n равным 10^9.")

# Задание 10
def task10():
    print("\n\t---- Задание 10 ----\n")
    
    mpmath.mp.dps = 50

    def f_bad_64(x):
        # Плохой алгоритм в float64 
        return (1.0 - math.cos(x)) / (x * x)

    def f_good_64(x):
        # Хороший алгоритм в float64
        return 2.0 * (math.sin(x / 2.0) / x) ** 2

    def f_bad_32(x):
        # Плохой алгоритм в float32
        x32 = np.float32(x)
        return (np.float32(1.0) - np.cos(x32)) / (x32 * x32)

    def get_exact(x):
        # Точное значение
        x_mp = mpmath.mpf(str(x))
        return float((1 - mpmath.cos(x_mp)) / (x_mp**2))

    print("\tЭксперимент (а): Влияние x (плохой алгоритм, float64)")
    print(f"\t{'x':>10} | {'bad (float64)':>16} | {'exact':>16} | {'err_bad':>10}")
    print("\t" + "-" * 65)
    for x in [1e-4, 1e-6, 1e-8]:
        b = f_bad_64(x)
        ex = get_exact(x)
        eb = abs(b - ex) / ex
        print(f"\t{x:>10.0e} | {b:>16.8e} | {ex:>16.8e} | {eb:>10.2e}")
    print("\tВывод (а): при уменьшении x ошибка растет из-за катастрофического сокращения (обусловленность/сокращение).")

    x_fixed_b = 1e-2
    ex_fixed_b = get_exact(x_fixed_b)
    print(f"\n\tЭксперимент (б): Влияние типа float (плохой алгоритм, x = {x_fixed_b})")
    print(f"\t{'type':>10} | {'bad':>16} | {'exact':>16} | {'err_bad':>10}")
    print("\t" + "-" * 65)
    
    b64 = f_bad_64(x_fixed_b)
    err64 = abs(b64 - ex_fixed_b) / ex_fixed_b
    
    b32 = f_bad_32(x_fixed_b)
    err32 = abs(float(b32) - ex_fixed_b) / ex_fixed_b
    
    print(f"\t{'float64':>10} | {b64:>16.8e} | {ex_fixed_b:>16.8e} | {err64:>10.2e}")
    print(f"\t{'float32':>10} | {float(b32):>16.8e} | {ex_fixed_b:>16.8e} | {err32:>10.2e}")
    print(f"\tВывод (б): float32 дает ошибку на несколько порядков больше из-за меньшей машинной точности.")

    
    x_fixed_v = 1e-8
    ex_fixed_v = get_exact(x_fixed_v)
    print(f"\n\tЭксперимент (в): Влияние алгоритма (x = {x_fixed_v}, float64)")
    print(f"\t{'algorithm':>10} | {'result':>16} | {'exact':>16} | {'err':>10}")
    print("\t" + "-" * 65)
    
    b_bad = f_bad_64(x_fixed_v)
    b_good = f_good_64(x_fixed_v)
    
    err_bad_alg = abs(b_bad - ex_fixed_v) / ex_fixed_v
    err_good_alg = abs(b_good - ex_fixed_v) / ex_fixed_v

    print(f"\t{'bad':>10} | {b_bad:>16.8e} | {ex_fixed_v:>16.8e} | {err_bad_alg:>10.2e}")
    print(f"\t{'good':>10} | {b_good:>16.8e} | {ex_fixed_v:>16.8e} | {err_good_alg:>10.2e}")
    print("\tВывод (в): смена алгоритма (тождество) полностью устраняет ошибку, вызванную сокращением.")

    print("\n\t--- Итоговое сравнение факторов ---")
    
    err_x_1e4 = abs(f_bad_64(1e-4) - get_exact(1e-4)) / get_exact(1e-4)
    err_x_1e8 = abs(f_bad_64(1e-8) - get_exact(1e-8)) / get_exact(1e-8)
    ratio_x = err_x_1e8 / err_x_1e4 if err_x_1e4 != 0 else 0
    print(f"\tВлияние x (от 1e-4 до 1e-8): ошибка выросла в {ratio_x:.1e} раз.")
    
    ratio_type = err32 / err64 if err64 != 0 else 0
    print(f"\tВлияние типа (float64 и float32): ошибка изменилась в {ratio_type:.1e} раз.")
    
    if err_good_alg == 0:
        print(f"\tВлияние алгоритма (bad и good): ошибка упала до нуля (идеальный результат).")
    else:
        print(f"\tВлияние алгоритма (bad и good): ошибка упала в {err_bad_alg/err_good_alg:.1e} раз.")

    print("\n\t--- Общий вывод ---")
    print("\tЭксперимент (а) показал, что уменьшение x приводит к росту ошибки на ~8 порядков.")
    print("\tЭксперимент (б) показал, что переход на float32 добавляет еще ~9 порядков")
    print("\tошибки из-за низкой машинной точности. Влияние типа данных сопоставимо по силе с влиянием самого x.")
    print("\tЭксперимент (в) показал, что выбор правильного алгоритма")
    print("\tполностью устраняет ошибку. Это самый мощный фактор.")

# Задание 11
def task11():
    print("\n\t---- Задание 11 ----\n")
    mpmath.mp.dps = 50
    
    x = 1e-16

    def algo_1(x):
        return math.log(1.0 + x)

    def algo_2(x):
        return float(np.log(1.0 + x))

    def exact(x):
        x_mp = mpmath.mpf(str(x))
        return float(mpmath.log(1 + x_mp))

    res1 = algo_1(x)
    res2 = algo_2(x)
    res_ex = exact(x)

    print(f"\tВход: x = {x}")
    print(f"\tАлгоритм 1 (math.log):   {res1:.20e}")
    print(f"\tАлгоритм 2 (numpy.log):  {res2:.20e}")
    print(f"\tЭталон (mpmath):         {res_ex:.20e}\n")

    print("\t--- Сравнение float с float ---")
    if res1 == res2:
        print(f"\tres1 == res2: да (совпадают побитово)")
    else:
        print(f"\tres1 == res2: нет (различаются)")

    print("\n\t--- Сравнение с эталоном ---")
    err1 = abs(res1 - res_ex) / abs(res_ex) if res_ex != 0 else 0
    err2 = abs(res2 - res_ex) / abs(res_ex) if res_ex != 0 else 0
    print(f"\t|res1 - exact| = {abs(res1 - res_ex):.2e} (ошибка ~{err1*100:.1f}%)")
    print(f"\t|res2 - exact| = {abs(res2 - res_ex):.2e} (ошибка ~{err2*100:.1f}%)")

    print("\n\t--- Вывод ---")
    print("\tОба float-результата совпали между собой,")
    print("\tтак как оба используют операцию 1 + x.")
    print("\tЕсли бы мы не имели эталона, мы бы решили, что алгоритмы работают верно,")
    print("\tведь две разные библиотеки (math и numpy) дали одинаковый ответ.")
    print("\tОднако сравнение с mpmath показывает, что оба результата неверны.")
    print("\tИстинное значение ~1e-16, а они выдают 0.")
    print("\tЭто потому что при x = 1e-16 сложение 1 + x в float64 округляется до 1,")
    print("\tтак как x меньше машинного эпсилон. Логарифм от 1 равен 0.")
    print("\tСравнивать float с float без независимого эталона является ")
    print("\tгрубой ошибкой. Разные алгоритмы могут одинаково сломаться и дать")
    print("\tодинаково неверный результат.")

# Задание 12
def task12():
    print("\n\t---- Задание 12 ----\n")
    
    mpmath.mp.dps = 50

    def f_bad(x):
        return math.sqrt(x + 1.0) - math.sqrt(x)

    def f_exact(x):
        x_mp = mpmath.mpf(str(x))
        return float(1 / (mpmath.sqrt(x_mp + 1) + mpmath.sqrt(x_mp)))

    # 9 точек от 10^2 до 10^16
    xs = np.logspace(2, 16, 9)
    
    print(f"\t{'x':>12} | {'bad':>18} | {'exact':>18} | {'err_bad':>12}")
    print("\t" + "-" * 75)

    errs = []
    for x in xs:
        b = f_bad(x)
        ex = f_exact(x)
        eb = abs(b - ex) / abs(ex) if ex != 0 else 0
        errs.append(eb)
        print(f"\t{x:>12.1e} | {b:>18.10e} | {ex:>18.10e} | {eb:>12.2e}")

    log_x = []
    log_err = []
    for i in range(len(xs)):
        if errs[i] > 0:
            log_x.append(math.log10(xs[i]))
            log_err.append(math.log10(errs[i]))
    
    coeffs = np.polyfit(log_x, log_err, 1)
    k = coeffs[0]  
    b = coeffs[1]  

    print(f"\n\t--- Оценка наклона (показателя степени) ---")
    print(f"\tНаклон прямой в log-log: k = {k:.2f}")
    print(f"\tТеоретическая оценка: ошибка ~ O(x^1). k_теор = 1.0")
    print(f"\tСовпадение: {'ДА' if abs(k - 1.0) < 0.2 else 'НЕТ'}")

    print("\n\t--- Вывод ---")
    print("\tОшибка плохого способа растет линейно с увеличением x (наклон k ≈ 0.99).")
    print("\tЭто совпадает с теоретической оценкой: ошибка ~ eps_machine * x.")
    print("\tПри x = 1.8e+14 плохой способ начинает выдавать 0 вместо истинного")
    print("\tзначения, а при x = 10^16 относительная ошибка достигает 100%.")
    print("\tНужен диапазон, а не одна точка потому что одна точка")
    print("\tне показывает закономерность. Только на диапазоне видно, что ошибка")
    print("\tрастет по степенному закону, и можно оценить этот закон.")

# Задание 13
def task13():
    print("\n\t---- Задание 13 ----\n")

    print("\t--- Окружение ---")
    print(f"\tPython version: {sys.version.split()[0]}")
    print(f"\tNumPy version:  {np.__version__}\n")

    N = 10**5
    def generate_data(seed, use_numpy=True):
        # Генерирует массив случайных чисел с заданным seed.
        if use_numpy:
            rng = np.random.default_rng(seed)
            return rng.normal(size=N)
        else:
            random.seed(seed)
            return [random.gauss(0, 1) for _ in range(N)]

    def sum_naive(arr):
        # Наивное суммирование циклом
        s = 0.0
        for x in arr:
            s += x
        return s

    def sum_builtin(arr):
        # Встроенная функция sum() 
        return sum(arr)

    def sum_fsum(arr):
        # Компенсированное суммирование math.fsum() 
        return math.fsum(arr)

    def sum_numpy(arr):
        # Суммирование через numpy 
        return float(np.sum(arr))

    def run_experiment(seed, use_numpy=True):
        # Запускает эксперимент и возвращает результаты 4 способов
        data = generate_data(seed, use_numpy)
        return {
            'naive': sum_naive(data),
            'sum': sum_builtin(data),
            'fsum': sum_fsum(data),
            'numpy': sum_numpy(data)
        }

    def print_results(label, res):
        print(f"\t{label}")
        print(f"\t  naive: {res['naive']:.15f}")
        print(f"\t  sum:   {res['sum']:.15f}")
        print(f"\t  fsum:  {res['fsum']:.15f}")
        print(f"\t  numpy: {res['numpy']:.15f}")

    print("\t--- seed = 42 ---")
    res_42_a = run_experiment(42, use_numpy=True)
    print_results("Результаты:", res_42_a)

    print("\n\t--- seed = 42 ---")
    res_42_b = run_experiment(42, use_numpy=True)
    print_results("Результаты:", res_42_b)

    print("\n\t--- Проверка воспроизводимости (seed = 42) ---")
    if res_42_a == res_42_b:
        print("\tВсе результаты совпали. Эксперимент воспроизводим.")
    else:
        print("\tРезультаты различаются! Ошибка воспроизводимости.")

    print("\n\t--- seed = 43 (новый запуск) ---")
    res_43 = run_experiment(43, use_numpy=True)
    print_results("Результаты:", res_43)

    print("\n\t--- Сравнение расхождений между методами ---")
    
    def diff(res, a, b):
        return abs(res[a] - res[b])
    
    print(f"\t{'Метод':>20} | {'seed=42':>12} | {'seed=43':>12}")
    print("\t" + "-" * 50)
    print(f"\t{'|fsum - naive|':>20} | {diff(res_42_a, 'fsum', 'naive'):>12.2e} | {diff(res_43, 'fsum', 'naive'):>12.2e}")
    print(f"\t{'|fsum - sum|':>20} | {diff(res_42_a, 'fsum', 'sum'):>12.2e} | {diff(res_43, 'fsum', 'sum'):>12.2e}")
    print(f"\t{'|fsum - numpy|':>20} | {diff(res_42_a, 'fsum', 'numpy'):>12.2e} | {diff(res_43, 'fsum', 'numpy'):>12.2e}")

    print("\n\t--- Вывод ---")
    print("\tПри фиксированном seed результаты обоих запусков полностью")
    print("\tсовпадают. Эксперимент воспроизводим.")
    print("\tПри смене seed абсолютные значения сумм меняются,")
    print("\tно характер расхождения между методами сохраняется.")
    print("\tнаивный sum и naive цикл отличаются от fsum на величину")
    print("\tпорядка 10^-12...10^-13.")
    print("\tБез фиксации seed и версий библиотек эксперимент невоспроизводим.")
    print("\tРазные версии numpy могут использовать разные алгоритмы генерации")
    print("\tслучайных чисел, а разные версии Python — разные реализации sum().")
    print("\tПоэтому в отчете всегда нужно указывать seed, версию Python и numpy.")

# Задание 14
def task14():
    print("\n\t---- Задание 14 ----\n")

    # В каждом массиве есть одно проблемное число
    tests = {
        "Очень большие (~10^300)": [1e300, 1e300, -1e300],
        "Очень маленькие (~10^-300)": [1e-300, 1e-300, 1e-300],
        "Ноль": [1.0, 0.0, -1.0],
        "Денормализованные (~10^-320)": [5e-324, 5e-324, 1.0],
        "float('inf')": [1.0, float('inf'), 2.0],
        "float('nan')": [1.0, float('nan'), 2.0]
    }

    def sum_naive(arr):
        s = 0.0
        for x in arr:
            s += x
        return s

    def sum_fsum(arr):
        try:
            return math.fsum(arr)
        except Exception as e:
            return f"Error: {e}"

    print(f"\t{'Сценарий':>30} | {'naive sum':>20} | {'math.fsum':>20}")
    print("\t" + "-" * 75)

    for name, arr in tests.items():
        naive_res = sum_naive(arr)
        fsum_res = sum_fsum(arr)
        
        def fmt(val):
            if isinstance(val, float):
                return f"{val:.2e}" if val != 0 else "0.0"
            return str(val)

        print(f"\t{name:>30} | {fmt(naive_res):>20} | {fmt(fsum_res):>20}")

    print("\n\t--- Подробный анализ ---")
    print("\tfloat('inf'): naive: 1.0 + inf + 2.0 = inf. Результат заражается бесконечностью.")
    print("\tfsum: возвращает inf. fsum не игнорирует inf, а корректно возвращает его.\n")
    
    print("\tfloat('nan'): naive: 1.0 + nan + 2.0 = nan. NaN 'отравляет' любую сумму.")
    print("\tfsum: также возвращает nan. fsum НЕ выбрасывает ошибку при наличии NaN,")
    print("\tон возвращает NaN, как и обычный sum.")
    print("\t(ValueError возникает только при сложении +inf и -inf одновременно).")

    print("\n\t--- Вывод ---")
    print("\tПри наличии inf оба метода возвращают inf. fsum не пытается")
    print("\tисправить бесконечность, а возвращает ее.")
    print("\tПри наличии nan оба метода возвращают nan.")
    print("\tРазница в том, что math.fsum даст ValueError, если в массиве")
    print("\tодновременно есть +inf и -inf.")
    print("\tОбычный sum может потерять точность денормализованных чисел,")
    print("\tfsum старается учесть их максимально точно.")
    print("\tВ реальном коде всегда надо проверять данные на наличие inf/nan")
    print("\tперед суммированием. Если данные чистые, fsum даст максимальную точность.")

# Задание 15
def task15():
    print("\n\t--- Задание 15 ---\n")

    def experiment(f_bad, f_good, xs, f_exact):
        print(f"{'x':>10} | {'bad':>16} | {'good':>16} | "
            f"{'exact':>16} | {'err_bad':>10} | {'err_good':>10}")
        print("\t" + "-" * 92)

        for x in xs:
            bad = f_bad(x)
            good = f_good(x)
            exact = f_exact(x)

            error_b = abs(bad - exact) / abs(exact) if exact else float('inf')
            error_g = abs(good - exact) / abs(exact) if exact else float('inf')

            b_str = f"{bad:.12e}" if bad != 0 else "0.0"
            print(f"{x:>10.0e} | {b_str:>16} | {good:>16.12e} | "
                f"{exact:>16.12e} | {error_b:>10.2e} | {error_g:>10.2e}")

    print("\t" + "="*92)
    print("\tПолный эксперимент")
    print("\t" + "="*92)

    mpmath.mp.dps = 50

    xs = np.logspace(2, 16, 10)

    def f_exact_mp(x):
        x_mp = mpmath.mpf(str(x))
        return float(1 / (mpmath.sqrt(x_mp + 1) + mpmath.sqrt(x_mp)))

    print("\n\tРезультаты эксперимента")
    experiment(
        f_bad  = lambda x: math.sqrt(x + 1) - math.sqrt(x),
        f_good = lambda x: 1 / (math.sqrt(x + 1) + math.sqrt(x)),
        xs     = xs,
        f_exact= f_exact_mp
    )

    print("\n\t--- Вывод ---")
    print("\tПлохой алгоритм теряет точность из-за")
    print("\tкатастрофического сокращения. sqrt(x+1) и sqrt(x) почти равны.")
    print("\tПри x = 10^12 ошибка становится заметной, при x = 10^14")
    print("\tона достигает 0.57%, а при x = 10^16 алгоритм полностью ломается")
    print("\t(выдает ровно 0.0 вместо истинного значения 5e-09).\n")
    print("\tПлохой алгоритм дает приемлемую точность (ошибка < 1%) при x <= 10^12.")
    print("\tПри x > 10^12 он начинает быстро терять точность, а при x >= 10^16 — ломается.\n")
    print("\tХороший алгоритм дает ошибку на уровне машинного")
    print("\tэпсилон (~10^-16) на всем диапазоне вплоть до x = 10^16.\n")
    print("\tМатематическая задача хорошо обусловлена (предел = 0),")
    print("\tно прямой алгоритм численно неустойчив. Смена алгоритма")
    print("\tполностью решает проблему. Эксперимент корректен, так как использует")
    print("\tнезависимый эталон, диапазон точек и разделяет источники ошибки.")



def main():
    print("-------- БЛОК 1 --------")
    task1()
    task2()
    task3()
    task4()
    print("-------- БЛОК 2 --------")
    task5()
    task6()
    task7()
    task8()
    #task9()
    print("-------- БЛОК 3 --------")
    task10()
    task11()
    task12()
    task13()
    task14()
    task15()

main()