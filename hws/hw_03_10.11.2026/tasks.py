import numpy as np

# БЛОК 1 

# Задание 1
def task1():
    print("\n\t--- Задание 1 ---\n")

    arr = np.arange(60).reshape(3, 4, 5)

    print("\tСвойства созданного массива:")
    print(f"\t\tShape: {arr.shape}")
    print(f"\t\tNdim: {arr.ndim}")
    print(f"\t\tSize: {arr.size}")
    print(f"\t\tDtype: {arr.dtype}")
    print(f"\t\tStrides: {arr.strides}")
    print(f"\t\tC_CONTIGUOUS: {arr.flags['C_CONTIGUOUS']}")

    print("\n\t--- Вывод к заданию 1 ---")
    print("\tStrides — это кортеж из 3 чисел, показывающий сколько")
    print("\tбайт нужно пройти в памяти, чтобы перейти к следующему элементу по каждому из измерений.")
    print("\tПервое число показывает сдвиг для перехода к следующему")
    print("\tблоку по оси 0. Так как элементы у нас целые числа шаги будут кратны этому размеру байта.")
    print("\n\tАтрибут size показывает общее количество элементов в массиве.")
    print("\tФункция np.arange(60) создает одномерный массив из 60 чисел,")
    print("\tа метод .reshape(3, 4, 5) меняет только его форму, но не количество")
    print("\tэлементов (3 * 4 * 5 = 60). Поэтому size равен 60.")

# Задание 2
def task2():
    print("\n\t--- Задание 2 ---\n")

    a = np.array([1, 2, 3, 4])
    print(f"\tИсходный массив a:", a)
    print(f"\t\ta / 2: {a / 2}")
    print(f"\t\ta // 2: {a // 2}")
    print(f"\t\ta / 2.0: {a / 2.0}")
    print(f"\t\ta.dtype: {a.dtype}")
    print(f"\t\t(a / 2).dtype: {(a / 2).dtype}")
    print(f"\t\t(a // 2).dtype: {(a // 2).dtype}")

    b = np.array([1, 2, 3], dtype=np.int8)
    print("\n\tИсходный массив b:", b)
    
    b_plus = b + 127
    print(f"\t\tb + 127: {b_plus}")
    print(f"\t\t(b + 127).dtype: {b_plus.dtype}")

    print("\n\t--- Вывод к заданию 2 ---")
    print("\ta / 2 не меняет a, потому что деление в NumPy возвращае новый массив.")
    print("\tПоэтому a не меняется, а результат создается в памяти заново с типом float64.")
    print("\tПоэтому a.dtype = int, а (a / 2).dtype = float.")
    print("\n\tb + 127 дает странный результат, потому что тип np.int8 хранить числа только от -128 до 127.")
    print("\tЧисло 127 - это максимальное значение для int8.")
    print("\tПри сложении 1 + 127 = 128 происходит перепронение.")
    print("\tВ двоичной системе 128 для 8-битного числа выглядит как -128.")
    print("\tВ Python (и NumPy) это не вызывает ошибку, потому что NumPy по умолчанию работает по правилам языка C.")
    print("\tОн просто  128 переводит в -128, 129 в -127 и т.д.")

# Задание 3
def task3():
    print("\n\t--- Задание 3 ---\n")

    true_val = 0.1
    err_32 = float(np.float32(0.1)) - true_val
    err_64 = float(np.float64(0.1)) - true_val

    print("\tОшибка float32:")
    print(f"\t\tВ repr:   {repr(err_32)}")
    print(f"\t\tВ :.20e:  {err_32:.20e}")

    print("\n\tОшибка float64:")
    print(f"\t\tВ repr:   {repr(err_64)}")
    print(f"\t\tВ :.20e:  {err_64:.20e}")

    if err_64 == 0:
        print("\tОшибка float64 настолько мала, что компьютер округлил её до нуля.")
        print(f"\tПри этом ошибка float32 составляет: {err_32}")
    else:
        ratio = abs(err_32) / abs(err_64)
        print(f"\n\tОтношение ошибок (|err_32| / |err_64|): {ratio:.2e} раз")


    print("\n\t--- Вывод к заданию 3 ---")
    print("\tfloat32 допустим для таких задач:")
    print("\t - Компьютерная графика и рендеринг (там важен объем памяти и скорость).")
    print("\t - Машинное обучение на видеокартах и нейросети (точности хватает).")
    print("\t - Быстрые инженерные расчеты с низкими требованиями к точности.")
    print("\n\tfloat32 недопустим для таких задач:")
    print("\t - Решение систем линейных алгебраических уравнений высоких порядков.")
    print("\t - Задачи на собственные значения и поиск корней уравнений.")
    print("\t - Численное интегрирование и дифференцирование с высокой точностью.")
    print("\t - Любые вычисления, где происходит накопление ошибки.")

# Задание 4
def task4():
    print("\n\t--- Задание 4 ---\n")

    arr_zeros_64 = np.zeros((2, 3), dtype=np.float64)
    arr_zeros_32 = np.zeros((2, 3), dtype=np.float32)
    arr_ones_16  = np.ones((2, 3), dtype=np.int16)
    arr_full_8   = np.full((2, 3), 7, dtype=np.uint8)

    print("\tСвойства массивов:")
    print(f"\t\tzeros (float64): dtype = {arr_zeros_64.dtype}, nbytes = {arr_zeros_64.nbytes} байт")
    print(f"\t\tzeros (float32): dtype = {arr_zeros_32.dtype}, nbytes = {arr_zeros_32.nbytes} байт")
    print(f"\t\tones  (int16):   dtype = {arr_ones_16.dtype}, nbytes = {arr_ones_16.nbytes} байт")
    print(f"\t\tfull  (uint8):   dtype = {arr_full_8.dtype}, nbytes = {arr_full_8.nbytes} байт")

    size = 1000 * 1000  
    mem_64 = size * 8   
    mem_32 = size * 4 
    
    saved_bytes = mem_64 - mem_32
    saved_mb = saved_bytes / (1024 * 1024)

    print(f"\n\tДля массива (1000, 1000):")
    print(f"\t\tfloat64 займет: {mem_64 / (1024 * 1024)} МБ")
    print(f"\t\tfloat32 займет: {mem_32 / (1024 * 1024)} МБ")
    print(f"\t\tЭкономия: {saved_mb} МБ / {saved_bytes} байт)")

    print("\n\t--- Вывод к заданию 4 ---")
    print("\tИспользование float32 экономит в 2 раза больше памяти по сравнению с float64.")
    print("\tДля больших массивов данных экономит оперативную память и ускоряет работу.")
    print("\n\tsfloat32 имеет гораздо меньшую точность. В задачах численных методов это может")
    print("\tпривести к накоплению огромных ошибок (при всех задачах где нужно точное решение).")
    print("\tПоэтому при выборе типа данных надо дрежать баланс между тем,")
    print("\tсколько у нас есть памяти, и тем, какая точность")
    print("\tнам нужна для получения достоверного результата.")

# БЛОК 2

# Задание 5
def task5():
    print("\n\t--- Задание 5 ---\n")

    a = np.arange(24)
    print(f"\tМассив a: shape = {a.shape}, размер = {a.size}")

    a46 = a.reshape(4, 6)
    print(f"\n\t(4, 6):")
    print(f"\t\tshape: {a46.shape}")
    print(f"\t\tДанные не потерялись: {np.array_equal(a, a46.ravel())}")

    a234 = a46.reshape(2, 3, 4)
    print(f"\n\t(2, 3, 4):")
    print(f"\t\tshape: {a234.shape}")
    print(f"\t\tДанные не потерялись: {np.array_equal(a, a234.ravel())}")

    a226 = a234.reshape(2, 2, 6)
    print(f"\n\t(2, 2, 6):")
    print(f"\t\tshape: {a226.shape}")
    print(f"\t\tДанные не потерялись: {np.array_equal(a, a226.ravel())}")

    a24 = a226.reshape(24)
    print(f"\n\t(24,):")
    print(f"\t\tshape: {a24.shape}")
    print(f"\t\tДанные не потерялись: {np.array_equal(a, a24.ravel())}")

    print("\n\t--- Вывод к заданию 5 ---")
    print("\treshape обычно не копирует данные, потому что метод по умолчанию пытается")
    print("\tвернуть view массива. Это значит, что он не выделяет новую память,")
    print("\tа просто создает новую обертку с другими размерами,")
    print("\tкоторая ссылается на те же самые байты в памяти.")
    
    print("\n\treshape вынужден скопировать данные, когда новый порядок элементов невозможно")
    print("\tпрочитать, просто шагая по старой памяти. Например, если вы делаете")
    print("\tтранспонирование или меняете порядок элементов с C-стиля на")
    print("\tFortran-стиль. В таких случаях NumPy создает копию")
    print("\tв новой области памяти, чтобы элементы лежали в нужном порядке.")

# Задание 6
def task6():
    print("\n\t--- Задание 6 ---\n")

    M = np.arange(12).reshape(3, 4)
    print("\tМассив M:\n", M)

    f = M.flatten()
    r = M.ravel()

    print("\n\tПроверка .base (откуда берутся данные):")
    print(f"\t\tf.base is None:   {f.base is None}  (f - это копия)")
    print(f"\t\tr.base is not None: {r.base is not None} (r - это представление)")
    
    f[0] = 999
    print(f"\n\tПосле f[0] = 999:")
    print(f"\t\tM[0, 0] = {M[0, 0]} (Осталось прежним, M не изменился)")

    r[1] = 888
    print(f"\n\tПосле r[1] = 888:")
    print(f"\t\tM[0, 1] = {M[0, 1]} (Изменилось, т.к. r связан с M)")

    print("\n\tМассив M после манипуляций:\n", M)

    print("\n\t--- Вывод по заданию 6 ---")
    print("\tМетод .flatten() возвращает новый массив, с выделенной память.")
    print("\tИзменение элементов в f никак не влияет на исходный M.")
    print("\tАтрибут .base у него равен None.")
    
    print("\n\tМетод .ravel() возвращает представление исходного массива.")
    print("\tОн не выделяет новую память, а просто ссылается на старую.")
    print("\t Поэтому изменение r меняет M. .base указывает на исходный M.")
    
    print("\n\t.ravel() лучше использовать, если нужно просто прочитать данные")
    print("\tв одномерном виде, и надо сэкономить память и время.")
    print("\tА .flatten() лучше использовать, если вам нужно безопасно изменить")
    print("\tодномерный массив, не затрагивая исходный массив.")

# Задание 7
def task7():
    print("\n\t--- Задание 7 ---\n")

    v = np.arange(5)
    print(f"\tМассив v: {v}, shape = {v.shape}")

    v_col = v[:, None]
    print(f"\n\tv[:, None] (столбец):")
    print(f"\t\tshape: {v_col.shape}")
    print(f"\t\tДобавлена новая ось (None) на место второго измерения")

    v_row = v[None, :]
    print(f"\n\tv[None, :] (строка):")
    print(f"\t\tshape: {v_row.shape}")
    print(f"\t\tДобавлена новая ось на место первого измерения")

    v_squeezed = np.squeeze(v[:, None])
    print(f"\n\tnp.squeeze(v[:, None]):")
    print(f"\t\tshape: {v_squeezed.shape}")
    print(f"\t\tnp.squeeze() удалил все оси, размер которых равен 1 (вернул обратно к (5,)).")

    m = np.arange(6).reshape(2, 3).T
    print(f"\n\tnp.arange(6).reshape(2, 3).T:")
    print(f"\t\tshape: {m.shape}")
    print(f"\t\tСодержимое:\n{m}")
    print(f"\t\tМассив (2,3) транспонирован, строки стали столбцами, получилась форма (3,2).")

    outer_product = v_col + v_row
    print(f"\n\tРезультат v[:, None] + v[None, :]:")
    print(f"\t\tshape: {outer_product.shape}")
    print(f"\t\tСодержимое:\n{outer_product}")

    print("\n\t--- Вывод к заданию 7 ---")
    print("\tv[:, None] имеет форму (5, 1) — это столбец.")
    print("\tv[None, :] имеет форму (1, 5) — это строка.")
    print("\tПри их сложении срабатывает broadcasting. NumPy растягивает")
    print("\tстолбец на 5 позиций вправо, а строку на 5 позиций вниз.")
    print("\tВ результате каждый элемент (i, j) равен v[i] + v[j].")
    print("\tПолучилась матрица сумм.")

# Задание 8
def task8():
    print("\n\t--- Задание 8 ---\n")

    A = np.arange(6).reshape(2, 3)
    print("\tМассив A:\n", A)
    print(f"\tshape A: {A.shape}, strides A: {A.strides}")

    B = A.T
    print("\n\tТранспонированный массив B = A.T:\n", B)
    print(f"\tshape B: {B.shape}, strides B: {B.strides}")

    print("\n\tСвязь B и A:")
    print(f"\t\tB.base is A: {B.base is A}")
    print(f"\t\tB.base is not None: {B.base is not None}")

    print("\n\tИзменяем B[0, 1] = 999...")
    B[0, 1] = 999
    
    print("\n\tМассив A после изменения B:")
    print(A)
    print(f"\t\tA[1, 0] = {A[1, 0]}")
    
    print("\n\t--- Вывод к заданию 8 ---")
    print("\t.T — это view, потому что NumPy не копирует данные при транспонировании,")
    print("\tт.к. было бы крайне неэффективно для памяти и времени. Вместо этого")
    print("\tон просто создает новый объект-обертку, который ссылается на")
    print("\tте же самые байты в памяти. Атрибут .base подтверждает это.")
    print("\n\tStrides — это шаги в байтах, которые нужно сделать, чтобы")
    print("\tперейти к следующему элементу по каждому измерению.")
    print(f"\tУ исходного A (2, 3) strides: {A.strides}.")
    print(f"\tУ транспонированного B (3, 2) strides: {B.strides}.")
    print("\tЧисла в strides просто поменялись местами.")
    print("\tНикакого копирования не произошло, NumPy просто поменял")
    print("\tправила чтения той же самой памяти.")
    print("\tПоэтому когда мы изменили B[0, 1], мы на самом деле изменили")
    print("\tA[1, 0], потому что это одна и та же ячейка памяти.")

# БЛОК 3

# Задание 9
def task9():
    print("\n\t--- Задание 9 ---\n")

    A = np.arange(6).reshape(2, 3)
    B = np.arange(6).reshape(3, 2)
    print(f"\tМассив A (форма {A.shape}):\n{A}")
    print(f"\n\tМассив B (форма {B.shape}):\n{B}")

    matmul_AB = A @ B
    print(f"\n\tA @ B:")
    print(f"\t\tshape: {matmul_AB.shape}")
    print(f"\t\tЗначения:\n{matmul_AB}")

    matmul_AT_BT = A.T @ B.T
    print(f"\n\tA.T @ B.T:")
    print(f"\t\tshape: {matmul_AT_BT.shape}")
    print(f"\t\tЗначения:\n{matmul_AT_BT}")

    elem_mul_AA = A * A
    print(f"\n\tA * A:")
    print(f"\t\tshape: {elem_mul_AA.shape}")
    print(f"\t\tЗначения:\n{elem_mul_AA}")

    print(f"\n\tПроверка A * B:")
    try:
        elem_mul_AB = A * B
        print(f"\t\tshape: {elem_mul_AB.shape}")
        print(f"\t\tЗначения:\n{elem_mul_AB}")
        print("\t\t(Сработал механизм broadcasting)")
    except ValueError as e:
        print(f"\t\tОШИБКА: {e}")
        print("\t\t(Матрицы разных форм нельзя перемножить поэлементно)")

    print("\n\tПример, где * и @ дают одинаковый результат:")
    D = np.diag([2, 3, 4])
    print(f"\t\tДиагональная матрица D:\n{D}")
    
    result_star = D * D
    result_matmul = D @ D
    print(f"\t\tD * D:\n{result_star}")
    print(f"\t\tD @ D:\n{result_matmul}")
    print(f"\t\tРезультаты равны: {np.array_equal(result_star, result_matmul)}")

    print("\n\t--- Вывод к заданию 9 ---")
    
    print("\tОператор * выполняет поэлементное умножение. Он перемножает соответствующие элементы матриц один на один.")
    print("\tОператор @ выполняет матричное умножение. Он умножает строку первой матрицы на столбец второй.")
    print("\tКоличество столбцов левой матрицы должно равняться количеству строк правой.")
    print("\n\tA * B работает, потому что A имеет форму (2, 3), а B — (3, 2). При поэлементном умножении")
    print("\tNumPy пытается применить broadcasting. Он растягивает меньшую матрицу. Так как размеры не совпадают и не являются единицами,")
    print("\tNumPy выдает ошибку ValueError. Если бы B была формы (1, 3) или (2, 1),  то broadcasting сработал бы и A * B выполнилось бы.")
    print("\n\t* и @ дают одинаковый результат только для диагональных матриц. У диагональной матрицы все")
    print("\tнедиагональные элементы равны нулю. При матричном умножении D @ D все внедиагональные произведения обнуляются, и остается")
    print("\tтолько возведение диагональных элементов в квадрат — то же самое, что дает поэлементное умножение D * D.")

# Задание 10
def task10():
    print("\n\t--- Задание 10 ---\n")

    M = np.arange(12).reshape(3, 4)
    print("\tМассив M:\n", M)
    print(f"\tФорма: {M.shape} (3 строки, 4 столбца)")

    sum_0 = M.sum(axis=0)
    sum_1 = M.sum(axis=1)
    print(f"\n\tM.sum(axis=0): {sum_0}, shape: {sum_0.shape}")
    print(f"\tM.sum(axis=1): {sum_1}, shape: {sum_1.shape}")

    mean_0 = M.mean(axis=0)
    mean_1 = M.mean(axis=1)
    print(f"\n\tM.mean(axis=0): {mean_0}, shape: {mean_0.shape}")
    print(f"\tM.mean(axis=1): {mean_1}, shape: {mean_1.shape}")

    argmax_0 = M.argmax(axis=0)
    argmax_1 = M.argmax(axis=1)
    print(f"\n\tM.argmax(axis=0): {argmax_0}, shape: {argmax_0.shape}")
    print(f"\tM.argmax(axis=1): {argmax_1}, shape: {argmax_1.shape}")

    print("\n\tПроверка на маленьком примере:")
    small = np.array([[1, 2],
                      [3, 4]])
    print("\tМаленькая матрица:\n", small)
    print(f"\tСумма axis=0: {small.sum(axis=0)}")
    print(f"\tСумма axis=1: {small.sum(axis=1)}")
    print(f"\tСумма по столбцам (вручную): {[small[0,0]+small[1,0], small[0,1]+small[1,1]]}")

    print("\n\t--- Вывод к заданию 10 ---")
    print("\tЧитать axis проще всего читать, как axis — это номер измерения, которое мы удаляем.")
    print("\tУ матрицы (3, 4): ось 0 — это строки, ось 1 — это столбцы.")
    print("\n\taxis=0 дДля двумерного массива означает пройти по всем строкам вниз для каждого столбца.")
    print("\tРезультатот будет одномерный массив длины 4. Это суммы")
    print("\tэлементов в столбцах. Форма меняется с (3, 4) на (4,).")
    print("\n\taxis=1 для двумерного массива это значит, что надо пройти по всем столбцам вправо для каждой строки.")
    print("\tРезультат — одномерный массив длины 3. Это суммы элементов в строках. Форма меняется с (3, 4) на (3,).")
    print("\n\targmax возвращает не значение максимума, а его индекс. Для axis=0 он вернет для каждого столбца номер строки,")
    print("\tгде  находится наибольший элемент. Для axis=1 он вернет для каждой строки номер столбца, где")
    print("\t где находится наибольший элемент.")

# Задание 11
def task11():
    print("\n\t--- Задание 11 ---\n")

    rng = np.random.default_rng(42)
    X = rng.normal(size=(5, 3))
    print(f"\tМассив X (форма {X.shape}):\n{np.round(X, 3)}")

    mean_0 = X.mean(axis=0)
    mean_0_keep = X.mean(axis=0, keepdims=True)
    
    print(f"\n\tX.mean(axis=0):")
    print(f"\t\tshape: {mean_0.shape}, значения: {np.round(mean_0, 3)}")
    
    print(f"\n\tX.mean(axis=0, keepdims=True):")
    print(f"\t\tshape: {mean_0_keep.shape}, значения:\n{np.round(mean_0_keep, 3)}")

    centered_0 = X - mean_0
    centered_0_keep = X - mean_0_keep
    print(f"\n\tФорма X - X.mean(axis=0): {centered_0.shape}")
    print(f"\tФорма X - X.mean(axis=0, keepdims=True): {centered_0_keep.shape}")
    print("\t\t(Обе операции сработали благодаря broadcasting)")

    std_1 = X.std(axis=1)
    std_1_keep = X.std(axis=1, keepdims=True)
    
    print(f"\n\tX.std(axis=1):")
    print(f"\t\tshape: {std_1.shape}, значения: {np.round(std_1, 3)}")
    print(f"\n\tX.std(axis=1, keepdims=True):")
    print(f"\t\tshape: {std_1_keep.shape}")
    print(f"\t\tЗначения:\n{np.round(std_1_keep, 3)}")

    normalized = (X - X.mean(axis=1, keepdims=True)) / std_1_keep
    
    print(f"\n\tНормированные данные (Z-score):")
    print(f"\t\tshape: {normalized.shape}")
    print(f"\t\tСреднее по строкам:  {np.round(normalized.mean(axis=1), 5)}")
    print(f"\t\tStd по строкам:      {np.round(normalized.std(axis=1), 5)}")

    print("\n\t--- Пояснения по заданию 11 ---")
    print("\tkeepdims=True нужен потому что по умолчанию операции mean, std, sum с axis=0")
    print("\tудаляют это измерение. Вместо формы (5, 3) мы получаем (3,).")
    print("\tФлаг keepdims=True сохраняет измерение, превращая (3,) в (1, 3).")
    print("\n\tЭто критично для broadcasting, потому что при вычитании X (5, 3) - mean_0 (3,) NumPy применяет правила")
    print("\tbroadcasting и растягивает вектор (3,) вдоль первой оси. В данном случае это работает,")
    print("\tпотому что 3 совпадает с последним измерением X. Но если бы мы делали операции по axis=1,")
    print("\tформа была бы (5,). Вычитая (5,) из (5, 3), NumPy выдал бы ошибку, так как 5 не совпадает с 3.")
    print("\tkeepdims Сохраняет форму (5, 1) при свертке по axis=1, мы явно указываем, что это вектор-столбец.")
    print("\tПри вычитании из X (5, 3) он растягивается на 3 столбца. Это делает код безопаснее и понятнее.")

# БЛОК 4

# Задание 12
def task12():
    print("\n\t--- Задание 12 ---\n")

    a = np.arange(10)
    print(f"\tМассив a: {a}")

    b = a[2:5]
    print(f"\n\tСрез b: {b}")
    
    b[0] = 999
    print(f"\tПосле b[0] = 999:")
    print(f"\t\tМассив b: {b}")
    print(f"\t\tМассив a: {a}")
    print("\t\t(Оригинал a изменился. b — это view)")

    a = np.arange(10)
    c = a[2:5].copy()
    print(f"\n\tСбросили a: {a}")
    print(f"\tСрез c (через.copy()): {c}")
    
    c[0] = 888
    print(f"\tПосле c[0] = 888:")
    print(f"\t\tМассив c: {c}")
    print(f"\t\tМассив a: {a}")
    print("\t\t(Оригинал a не изменился. c — это копия)")

    print("\n\t--- Вывод к заданию 12 ---")
    
    print("\t1. Почему это важно для численных методов:")
    print("\tэто важно для численных методов, потому что если вы загрузили массив")
    print("\tданных. Вы делаете срез для анализа и передаете его в функцию, которая вычитает")
    print("\tсреднее данные. Если это view, то функция изменит исходный массив.")
    print("\tВаш оригинальный масиив будет испорчен, а вы даже не знаете, где произошла утечка изменений.")
    print("\tview — это преимущетсво, если вам нужно просто прочитать часть огромного массива,")
    print("\tсоздание копии — это пустая трата оперативной памяти. View позволяет работать с данными без копирования.")
    
    print("\n\t3. Когда view — это БАГ (ловушка):")
    print("\tview — это баг если вы собираетесь изменять срез, и при этом вам нужно сохранить")
    print("\tисходные данные нетронутыми. В этом случае надо использовать .copy().")

# Задание 13
def task13():
    print("\n\t--- Задание 13: Булева маска и fancy indexing ---\n")

    rng = np.random.default_rng(0)
    a = rng.normal(size=20)
    print(f"\tМассив a:\n{np.round(a, 3)}")

    mask_pos = a[a > 0]
    print(f"\n\ta[a > 0] кол-во элементов")
    print(f"\t\tКоличество: {len(mask_pos)}")
    print(f"\t\tЗначения: {np.round(mask_pos, 3)}")

    mask_range = a[(a > -1) & (a < 1)]
    print(f"\n\ta[(a > -1) & (a < 1)] кол-во элементов")
    print(f"\t\tКоличество: {len(mask_range)}")
    
    fancy_idx = a[[0, 5, 10, 15]]
    print(f"\n\ta[[0, 5, 10, 15]] выборка")
    print(f"\t\tЗначения: {np.round(fancy_idx, 3)}")
    print("\t\tЭто выборка элементов по конкретным индексам.")
    print("\t\tМы явно попросили 0, 5, 10 и 15 элементы в этом порядке.")
    
    outliers = a[np.abs(a) > 2]
    print(f"\n\t4. a[np.abs(a) > 2] выбросы")
    print(f"\t\tЗначения: {np.round(outliers, 3)}")
    print(f"\t\tКоличество: {len(outliers)}")

    print("\n\tЗаменяем все отрицательные на 0 через a[a < 0]")
    a[a < 0] = 0
    print(f"\t\tРезультат a:\n{np.round(a, 3)}")

    print("\n\t--- Вывод к заданию 13 ---")
    
    print("\ta[a > 0] & (a < 1) дает ошибку, а a[(a > 0) & (a < 1)] работает, потому что")
    print("\tоператор & требует, чтобы оба операнда были булевыми массивами.")
    print("\tВ первом случае Python пытается ычислить результат a[a > 0] (который уже является массивом чисел, а не булевых значений),")
    print("\tа затем применить к нему И. Из-за приоритета операций  это приводит к ошибке, потому что")
    print("\tиндексация [] выполняется раньше &, и это приводит к ошибке.")
    print("\tВо втором случае мы сначала заключаем каждое сравнение в скобки, получаем два булевых массива одинаковой")
    print("\tдлины, и только потом применяем к ним &, что работает корректно.")
    print("\ta[a < 0] = 0 делает, что мы создаем булеву маску, а затем присваиваем значение 0 только тем элементам")
    print("\tгде маска True. Это способ очистки данных от отрицательных значений.")


# Задание 14
def task14():
    print("\n\t--- Задание 14 ---\n")

    rng = np.random.default_rng(1)
    X = rng.normal(size=(100, 3))
    print(f"\tМассив X (форма {X.shape}):")
    print(f"\t\tСреднее по столбцам: {np.round(X.mean(axis=0), 3)}")
    print(f"\t\tStd по столбцам:    {np.round(X.std(axis=0), 3)}")

    X_norm = (X - X.mean(axis=0)) / X.std(axis=0)
    
    print(f"\n\tНормированные данные X_norm (форма {X_norm.shape}):")
    print(f"\t\tСреднее по столбцам (должно быть ~0): {np.round(X_norm.mean(axis=0), 5)}")
    print(f"\t\tStd по столбцам (должно быть ~1):     {np.round(X_norm.std(axis=0), 5)}")

    diff = X_norm[:, None, :] - X_norm[None, :, :]
 
    D = np.sqrt(np.sum(diff ** 2, axis=2))
    
    print(f"\n\tМатрица расстояний D (форма {D.shape}):")
    print(f"\t\tРазмер: {D.shape}")
    print(f"\t\tДиагональ (должна быть ~0): {np.round(np.diag(D)[:5], 5)}...")
    print(f"\t\tСимметричность (D == D.T): {np.allclose(D, D.T)}")
    
    print(f"\n\tПроверка:")
    print(f"\t\tD.shape == (100, 100): {D.shape == (100, 100)}")
    print(f"\t\tДиагональ < 1e-10: {np.all(np.diag(D) < 1e-10)}")
    print(f"\t\tМатрица симметрична: {np.allclose(D, D.T)}")

    print("\n\t---Вывод к заданию 14 ---")
    print("\tМы использовали X.mean(axis=0) и X.std(axis=0). Это векторы формы (3,). При вычитании (100, 3) - (3,)")
    print("\tNumPy применяет broadcasting и растягивает вектор (3,) на все 100 строк. Это позволяет обойтись")
    print("\tбез цикла for и работает в сотни раз быстрее.")
    print("\n\tX_norm[:, None, :] создает форму (100, 1, 3), в которой 100 слоев по одному наблюдению в каждом.")
    print("\tX_norm[None, :, :] создает форму (1, 100, 3) один слой со всеми наблюдениями. При вычитании этих")    
    print("\tмассивов NumPy автоматически растягивает ервый по второй оси, а второй — по первой.")
    print("\tВ результате получается трехмерный массив формы (100, 100, 3), где элемент [i, j, k]")
    print("\tэто разность k-го признака между i-м и j-м наблюдением. Затем мы берем сумму квадратов по")
    print("\tпоследней оси (k) и извлекаем квадратный корень — получаем матрицу расстояний (100, 100).")
    print("\n\t - Диагональ матрицы D равна нулю, потому что расстояние от наблюдения до самого себя равно 0.")
    print("\t- Матрица симметрична, потому что расстояние от A до B равно расстоянию от B до A (D[i, j] = D[j, i]).")
    print("\t- Средние по столбцам X_norm равны нулю, а std — единице, что подтверждает правильность нормировки.")

# Задание 15
def task15():
    print("\n\t--- Задание 15 ---\n")

    rng = np.random.default_rng(42)
    raw = rng.normal(loc=20, scale=2, size=(30, 4))
    
    raw[7, 2] = 100
    print("\tИсходные данные (с выбросом raw[7, 2] = 100):")
    print(f"\tФорма: {raw.shape}")
    print(f"\tПервые 3 строки:\n{np.round(raw[:3], 2)}")

    print("\n\t--- Шаг 1: Атрибуты массива ---")
    print(f"\tshape: {raw.shape}")
    print(f"\tdtype: {raw.dtype}")
    print(f"\tsize:  {raw.size}")

    print("\n\t--- Шаг 2: Поиск выбросов ---")
    mean_col = raw.mean(axis=0)
    std_col = raw.std(axis=0)

    outlier_mask = np.abs(raw - mean_col) > 3 * std_col
    outlier_count = np.sum(outlier_mask)
    print(f"\tКоличество выбросов: {outlier_count}")
    print(f"\tИх индексы (координаты): {np.argwhere(outlier_mask)}")

    print("\n\t--- Шаг 3: Замена на NaN и подсчет среднего ---")
    raw_nan = raw.copy()
    raw_nan[outlier_mask] = np.nan
    print(f"\tМассив после замены (первые 9 строк, столбец 2):\n{np.round(raw_nan[:9, 2], 2)}")
    
    mean_nan = np.nanmean(raw_nan, axis=0)
    print(f"\tСреднее по столбцам (без учета NaN):\n{np.round(mean_nan, 2)}")

    raw_restored = np.where(outlier_mask, np.nan, raw)
    print(f"\tПроверка через np.where: {np.allclose(raw_restored, raw_nan, equal_nan=True)}")

    print("\n\t--- Шаг 4: Транспонирование ---")
    raw_T = raw.T
    print(f"\tФорма после .T: {raw_T.shape}")
    
    raw_back = raw_T.T
    print(f"\tФорма после обратного .T: {raw_back.shape}")
    print(f"\tДанные не потерялись: {np.array_equal(raw, raw_back)}")

    print("\n\t--- Шаг 5: Ravel и reshape ---")
    raw_flat = raw.ravel()
    print(f"\tФорма после ravel: {raw_flat.shape}")
    
    raw_reshape = raw_flat.reshape(30, 4)
    print(f"\tФорма после reshape: {raw_reshape.shape}")
    print(f"\tДанные не потерялись: {np.array_equal(raw, raw_reshape)}")

    print("\n\t--- Шаг 6: Средние и std по каждому датчику (axis=0) ---")
    means = raw.mean(axis=0)
    stds = raw.std(axis=0)
    for i in range(4):
        print(f"\tДатчик {i+1}: среднее = {means[i]:.2f}, std = {stds[i]:.2f}")

    print("\n\t--- Шаг 7: Нормировка (Z-score) ---")
    # Используем keepdims=True, чтобы формы были (1, 4) и broadcasting сработал без ошибок
    X_norm = (raw - raw.mean(axis=0, keepdims=True)) / raw.std(axis=0, keepdims=True)
    
    print(f"\tСредние по столбцам (должны быть ~0): {np.round(X_norm.mean(axis=0), 5)}")
    print(f"\tStd по столбцам (должны быть ~1):     {np.round(X_norm.std(axis=0), 5)}")

    print("\n\t--- Вывод к заданию 15 ---")
    print("\tcopy() потребовалась на шаге 3. Мы использовали raw.copy(), чтобы заменить выбросы на NaN,")
    print("\tне испортив исходный массив raw. Если бы мы написали просто raw[outlier_mask] = np.nan, то данные были бы потеряны.")
    print("\n\tbroadcasting сработал на шаге 2 при вычислении маски (raw - mean_col) и на шаге 7")
    print("\tпри нормировке. Везде NumPy растягивал вектор формы (4,) или (1, 4) на всю матрицу (30, 4) без явных циклов.")
    print("\n\tОшибка формы могла возникнуть на шаге 7, если бы мы не использовали keepdims=True или не написали")
    print("\tбы raw.mean(axis=0) правильно. При вычитании (30, 4) - (4,) все работает, но при более сложных операциях")
    print("\t(например, (30, 4) - (30,)) NumPy выдал бы ValueError, так как размеры не совпадают по последней оси.")
    print("\n\tТранспонирование (.T), ravel() и reshape() не потеряли ни одного")
    print("\tэлемента, что подтверждено функцией np.array_equal(). Это доказывает,")
    print("\tчто NumPy использует view (представления) там, где это возможно.")

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
    print("-------- БЛОК 3 --------")
    task9()
    task10()
    task11()
    print("-------- БЛОК 4 --------")
    task12()
    task13()
    task14()
    task15()

main()