# Необходимо сравнить скорость работы 2 алгоритмов вычисления чисел
# Фибоначчи и определить, какой из них работает быстрее. Так различия
# начнутся уже с 40 члена последовательности.

from random import randint
from time import time
fib1 = 1
fib2 = 1
n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)
i = 0
start = time()
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
print("Значение этого элемента:", fib2)
print(f"На это ушло времени {time() - start}")
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
start = time()
print(fibonacci(40))
print(f"На это ушло времени {time() - start}")