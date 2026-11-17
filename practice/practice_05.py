import timeit
import matplotlib.pyplot as plt
import numpy as np
import tracemalloc

def task1():
    print("Задание 1")
    n_values = [100, 1000, 10000]
    list_times = []
    set_times = []
    speedups = []

    for n in n_values: 
        data_list = list(range(n))
        data_set =  set(range(n))
        target = -1
        globals = {"target": target, "data_list": data_list, "data_set": data_set}

        t_list = min(timeit.repeat("target in data_list", globals=globals, number=1000, repeat=5)) / 1000 * 1_000_000
        list_times.append(t_list)

        t_set = min(timeit.repeat("target in data_set", globals=globals, number=1000, repeat=5)) / 1000 * 1_000_000
        set_times.append(t_set)

        speedup = t_list / t_set
        speedups.append(speedup)
        print(f"n = {n}: list = {t_list:.2f} мкс, set = {t_set:.2f} мкс, set быстрее в {speedup:.1f} раз")

    plt.figure(figsize=(10, 6))

    plt.plot(n_values, list_times, marker='o', label='list (O(n))', color='red')
    plt.plot(n_values, set_times, marker='o', label='set (O(1))', color='green')

    plt.yscale("log")
    plt.grid(True, which="both", alpha=0.2)

    plt.title("Сравнение проверки вхождения у list и set")
    plt.xlabel("Размер коллекции (n)")
    plt.ylabel("Время (микросекунды, лог-шкала)")
    plt.legend()
    plt.xticks(n_values)
    plt.show()

def task2():
    print("Задание 1")
    n_values = [100000, 1000000]

    code_loop = "out = []\nfor i in range(N):\n    out.append(i*i)"
    code_comp = "out = [i*i for i in range(N)]"
    code_map = "out = list(map(lambda i: i*i, range(N)))"

    algorithms = {
    "Loop + append": code_loop,
    "List comprehension": code_comp,
    "map + lambda": code_map
    }

    times = {name: [] for name in algorithms}
    memories = {name: [] for name in algorithms}

    for n in n_values:
        for name, code in algorithms.items():
            t = min(timeit.repeat(code, globals={"N": n}, number=1, repeat=5)) * 1000
            times[name].append(t)
            
            tracemalloc.start()
             
            exec(code, {"N": n})
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
             
            mem_mb = peak / (1024 * 1024)
            memories[name].append(mem_mb)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    markers = ['o', 's', '^']
    for i, (name, t_vals) in enumerate(times.items()):
        ax1.plot(n_values, t_vals, marker=markers[i], label=name, linewidth=2)
    ax1.set_title("Время выполнения")
    ax1.set_xlabel("N")
    ax1.set_ylabel("Время (мс)")
    ax1.set_xticks(n_values)
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    x = np.arange(len(n_values))
    width = 0.25

    for i, (name, m_vals) in enumerate(memories.items()):
        offset = (i - 1) * width  # Сдвигаем столбцы: -width, 0, +width
        ax2.bar(x + offset, m_vals, width, label=name)

    ax2.set_title("Пиковая память")
    ax2.set_xlabel("N")
    ax2.set_ylabel("Память (МБ)")
    ax2.set_xticks(x)
    ax2.set_xticklabels([f"N={n}" for n in n_values])
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.legend()

    plt.tight_layout()
    plt.show()

    print("Вывод:")
    print("а) По памяти все способы равны, потому что результат одинаковый.")
    print("б) По времени list comprehension быстрее из-за отсутствия вызовов append.")
    print("в) map + lambda медленнее из-за накладных расходов на lambda.")

def main(): 
    # task1()
    task2()

main()