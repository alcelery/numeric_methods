# Практика на втором занятии 03.11.2026

import math, mpmath

def experiment(f_bad, f_good, xs, f_exact):
    print(f"{'x':>10} | {'bad':>14} | {'good':>14} | "
          f"{'err_bad':>10} | {'err_good':>10}")
    
    print("-" * 70)

    for x in xs:
        bad = f_bad(x)
        good = f_good(x)
        exact = f_exact(x)
        error_b = abs(bad - exact) / abs(exact) if exact else float('inf')
        error_g = abs(good - exact) / abs(exact) if exact else float('inf')
        print(f"{x:>10.0e} | {bad:>14.8e} | {good:>14.8e} | "
              f"{error_b:>10.2e} | {error_g:>10.2e}")

xs = [1e10, 1e12, 1e14]

print("\n------------------------- Большие значения ---------------------------")
experiment(
    f_bad = lambda x: math.sqrt(x + 1) - math.sqrt(x),
    f_good = lambda x: 1 / (math.sqrt(x + 1) + math.sqrt(x)),
    xs = xs,
    f_exact = lambda x: float(1 / ((mpmath.sqrt(x) + 1) + mpmath.sqrt(x)))
)


xs = [1e-10, 1e-12, 1e-14]

print("\n------------------------- Маленькие значения -------------------------")
experiment(
    f_bad = lambda x: math.sqrt(x + 1) - math.sqrt(x),
    f_good = lambda x: 1 / (math.sqrt(x + 1) + math.sqrt(x)),
    xs = xs,
    f_exact = lambda x: float(1 / ((mpmath.sqrt(x) + 1) + mpmath.sqrt(x)))
)