# Практика на первом занятии 03.11.2026

import math

def relative_error(approx, exact): 
    delta = abs(approx - exact)
    print(f"Δx = {delta}")
    sigma = delta / abs(exact)
    return sigma

def main():
    print("--- Проверка ---\n")
    print("--- π и 3.14 ---")
    print(f"δx = {relative_error(3.14159, 3.14)}\n")

    print("--- (0.1 + 0.2) и 0.3 ---")
    print(f"δx = {relative_error((0.1 + 0.2), 0.3)}\n")

    print("--- Сумма миллиона(0.1) и math.fsum ---")
    list_01 = [0.1] * 1000000
    sum_norm = sum(list_01)
    sum_fsum = math.fsum(list_01)
    print(f"δx = {relative_error(sum_norm, sum_fsum)}\n")

    print("Сравнение (Δx) и (δx):")
    print("- В первом случае абсолютная мала, а относительная велика (0.05% много для точных вычислений)")
    print("- Во втором обе малы")
    print("- В третьем равны нулю, так как math.fsum выдал результат, который компьютер считает идентичным точному значению. Ошибки округления не накопились")

main()