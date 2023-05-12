"""Задача 26:Факториал и треугольное число

n = int(input('Введите число: '))
factorial=1

def factorial(n):
    if n==1:
        return n
    else:
        return n * factorial(n-1)
    
print(factorial(n))"""

