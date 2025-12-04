# виды сортировок 7 типов
import random
import time as t
import sys
sys.setrecursionlimit(20_000)
# количество элементов в слайсах для сортировки
n = [10, 100, 1000, 10_000]

# разброс значений m
m = [10, 100, 1000]

# создаем слайсы
# n=10, m=10
# n=10, m=100
# n=10, m=1000
# n=100, m=10
# n=100, m=100
# n=100, m=1000
# n=1000, m=10
# n=1000, m=100
# n=1000, m=1000
# n=10_000, m=10
# n=10_000, m=100
# n=10_000, m=1000

list_unsorted_slices = []

for i in range(len(n)):
    for j in range(len(m)):
        unsorted_slice = [random.randint(0, m[j]) for _ in range(n[i])]
        data = [unsorted_slice, n[i], m[j]]
        list_unsorted_slices.append(data)



# 1) Пузырьковая сортировка
# сравнивает соседние элементы, если i > i+1, то меняем местами
def bubble_sort(arr):
    name = "Bubble sorting"
    swaps, comps = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            comps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1

    return name, arr, swaps, comps


# 2) Улучшенная пузырьковая сортировка
# работает как и 1), но в каждом проходе уменьшаем кол-во проходов на i
# т.к. за 1 итерацию мы всегда перетаскиваем самое большое значение в конец слайса
def improved_bubble_sort(arr):
    name = "Improved bubble sorting"
    swaps, comps = 0, 0
    change=True
    while change:
        changes = False
        for j in range(len(arr)-1):
            comps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                changes = True


    return name, arr, swaps, comps

# 3) Шейкер сортировка
# работает как 1), но за 1 проход самый большой эл опускается на свое место
# и самый маленький поднимается на 1 позицию
def shaker_sort(arr):
    name = "Shaker sorting"
    swaps, comps = 0, 0
    k = len(arr)-1
    left = 0
    right = k


    while left < right:
        # туда
        for j in range(left, right):
            comps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                k=j
        right = k

        # Обратно
        for j in range(right, left, -1):
            comps += 1
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swaps += 1
                k=j
        left = k


    return name, arr, swaps, comps

# 4) Вставка сортировка
# разделяет слайс на 2 части, отсортированный и несотсортированный
# за проход берет начальный эл. из неотсортированной части, а
# дальше вставляет его в нужное место в отсортированной части слайса
def insert_sort(arr):
    name = "Insert sorting"
    comps, swaps = 0, 0
    for i in range(1, len(arr)):
        tmp = arr[i]
        hole = i
        while hole > 0 and arr[hole - 1] > tmp:
            comps += 1
            arr[hole] = arr[hole-1]
            hole -= 1
            swaps += 1
        if hole > 0:
            comps += 1
        arr[hole] = tmp
    return name, arr, swaps, comps

# 5) алгоритм шелла
# улучшенный 4), но разделяется на несколько этапов

# 1. берется шаг (обычно n//2, n - кол-во эл.)
# дальше с этим шагом сравниваем эл., как во вставке
# (сортируем эл. которые попали под шаг способом вставки каждую итерацию)

# 2. после прохода, делим шаг нацело на 2,
# повторяем из 1. сортировку с шагом

# 3. когда шаг == 1, мы используем обычную вставку и завершаем сортировку
# список сортировок
def shell_sort(arr):
    name = "shell sorting"
    swaps, comps = 0, 0

    step = len(arr) // 2

    while step > 0:
        for i in range(step, len(arr)):
            tmp = arr[i]
            hole = i
            while hole - step >= 0:
                comps += 1
                if arr[hole-step] > tmp:
                    arr[hole] = arr[hole-step]
                    hole -= step
                    swaps += 1
                else:
                    break
            arr[hole] = tmp
        step //= 2

    return name, arr, swaps, comps

# 6) quick sort
def quick_sort(arr):
    name = "quick sorting"
    swaps, comps = 0, 0

    def QS(left, right):
        nonlocal swaps, comps
        if left >= right:
            return

        pivot = arr[right]   # опорный элемент
        i = left - 1

        # разбиение (partition)
        for j in range(left, right):
            comps += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

        # ставим pivot на своё место
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        swaps += 1

        p = i + 1  # индекс опорного элемента

        # рекурсивно сортируем левую и правую части
        QS(left, p - 1)
        QS(p + 1, right)

    QS(0, len(arr) - 1)
    return name, arr, swaps, comps

def select_sort(arr):
    name = "select sorting"
    swaps, comps = 0, 0

    for i in range(len(arr)-1):
        min_index = i
        for j in range(1, len(arr)):
            comps += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    return name, arr, swaps, comps

sorting_algos = [
    bubble_sort,
    improved_bubble_sort,
    shaker_sort,
    insert_sort,
    shell_sort,
    quick_sort,
    select_sort
]

# Запуск сортировок
for func in sorting_algos:
    for i in range(len(list_unsorted_slices)):
        time_amount = 0
        swaps_amount = 0
        comps_amount = 0
        name = ""

        for _ in range(10):
            start = t.perf_counter()
            name, arr, swaps, comps = func(list_unsorted_slices[i][0][:])
            end = t.perf_counter()
            time_spent = end - start

            # print("\n", sort_name)
            # print("n=", list_unsorted_slices[i][1])
            # print("m=", list_unsorted_slices[i][2])
            # print("Отсортированный список:", arr)
            # print("Количество перестановок:", swaps)
            # print("Количество сравнений:", comps)
            # print("Количество затраченного времени:", time_spent)

            time_amount += time_spent
            swaps_amount += swaps
            comps_amount += comps

        print(name)
        print("n=", list_unsorted_slices[i][1])
        print("m=", list_unsorted_slices[i][2])
        print("Среднее значение перестановок:", swaps_amount/10)
        print("Среднее значение проверок:", comps_amount/10)
        print("Среднее значение времени:", time_amount/10)
        print("\n")
