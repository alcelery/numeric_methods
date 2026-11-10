import math 

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




def main():
    print("-------- БЛОК 1 --------")
    task1()

main()