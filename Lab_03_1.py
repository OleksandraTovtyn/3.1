# Lab_03_1.py
# Товтин ОЛександра
# Лабораторна робота №3.1
# Розгалуження, задане формулою: функція однієї змінної
# Варіант  21
import math
def method1(x):
    x = 3
    A = 2 + 1 / (1 + x)
    if x < 1:
        B =  - math.sqrt(math.cos(3) + 13)
    if x >= 1 and x <= 5:
        B = - 3 + 1 / math.tan((4 + x) / math.sqrt(2))
    if x > 5:
        B = - 8 + 0.7 * x
    y = A + B
    return y
result1 = method1(3)
print(result1)

def method2(x):
    x = 3
    A = 2 + 1 / (1 + x)
    if x < 1:
        B =  - math.sqrt(math.cos(3) + 13)
    elif x >= 1 and x <= 5:
        B = - 3 + 1 / math.tan((4 + x) / math.sqrt(2))
    else: 
        B = - 8 + 0.7 * x
    y = A + B
    return y
result2 = method2(3)
print(result2)



