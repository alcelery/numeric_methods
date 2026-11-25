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
        print(f"{row['iter']:>3} | {row['x_prev']:>14.10f} | {row['x_curr']:>14.1} |"
        f"{row['f_curr']:>14.3e} | {row['step']:>10.2e}")
