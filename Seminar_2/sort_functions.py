# lsdcnspdmc

import random
import time

def how_long(func, x):
    start = time.time()
    func(x)
    print(f"На это ушло времени {time.time() - start}")


# Задание 1
# 1.Необходимо написать один из простых алгоритмов сортировки, имеющий сложность O(n2).
# 2.Можно выбрать из пузырьковой сортировки, сортировки вставками и
# сортировки выбором.
# 3.Следует обратить внимание на сложность данных алгоритмов и
# указать признаки квадратичной сложности для каждого из них
 # пузырьковая сортировка
def sorting(array: list):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


# Задание 2
# Написать алгоритм быстрой сортировки (quicksort).
def quick_sort(array: list):
    if len(array) <= 1:
        return array
    q = random.choice(array)
    left_array = []
    middle_array = []
    right_array = []
    for el in array:
        if el == q:
            middle_array.append(el)
        elif el < q:
            left_array.append(el)
        else:
            right_array.append(el)
    return quick_sort(left_array) + middle_array + quick_sort(right_array)

    # Сортировка целых чисел
    # Исходная последовательность чисел длины n, а в конце отсортированная, хранится в массиве A.
    # Также используется вспомогательный массив C с индексами от 0  до k−1, изначально заполняемый нулями.
    # Последовательно пройдём по массиву A и запишем в C[i] количество чисел, равных i.
    # Теперь достаточно пройти по массиву C и для каждого number∈{0,...,k−1}  в массив A
    # последовательно записать число C[number] раз.
def counting_sort(array: list): # сортировка подсчетом
    temp_array = [0] * (max(array) + 1)
    for el in array:
        temp_array[el] += 1
    result_array = []
    for i in range(len(temp_array)):
        result_array += [i] * temp_array[i]
    return result_array


# Сортировка слиянием
def merge_two_list(a, b):
    result = []
    while a and b:
        result.append((a if a[0] < b[0] else b).pop(0))
    result += a + b
    return result

def merge_sort(s):
    mid = len(s) // 2
    return s if len(s) == 1 else merge_two_list(merge_sort(s[:mid]), merge_sort(s[mid:]))

# Генерация списка - рандомного в заданном диапазоне
new_list = [random.randint(0, 1_000_000) for _ in range(10_000)]
# print(new_list)

print("Merger sort")
list_1 = new_list[::]
start = time.time()
merge_sort(list_1)
print(f"На это ушло времени {time.time() - start}")

print("Counting sort") #
how_long(counting_sort, new_list)

print("Built in sorting") # Встроенная сортировка в Python
list_2 = new_list[::]# поэлементное копирование Срезами
start = time.time()
list_2.sort()
print(f"На это ушло времени {time.time() - start}")

print("Quick sort") # Быстрая сортировка
start = time.time()
quick_sort(new_list)
print(f"На это ушло времени {time.time() - start}")

print("Bubble sort") # Пузырьковая сортировка
how_long(sorting, new_list)
# print(new_list)

# Библиотека NumPy