#Задача 2: Найдите сумму цифр трехзначного числа.
"""
a = str(input('Введите трехзначное число: '))
b = int(a[0])
c = int(a[1])
d = int(a[2])
sum = int(b+c+d)
print(f'Сумма чисел равна:{sum}')
"""
#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
"""
overal = int(input('Кол-во сделанных журавликов: '))
boy = int(overal/6)
katya = int(boy*4)
print(f'Катя сделала: {katya}, а  Петя и Сережа сделали: {boy}')
"""
"""решение 4 задачи актуально лишь для чисел кратных 6"""
#Задача 6: Вам требуется написать программу, которая проверяет счастливость билета.
"""
number = str(input('Введите номер билета: '))
a1 = int(number[0])
a2 = int(number[1])
a3 = int(number[2])
a4 = int(number[3])
a5 = int(number[4])
a6 = int(number[5])
sum1 = int (a1+a2+a3)
sum2 = int (a4+a5+a6)
if sum1==sum2:
    print('Ура!!!билет счастливый')
else:
    print('Увы( билет НЕ счастливый')
"""
#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
"""
a = int(input('введите колличество столбцов:'))
b = int(input('введите колличество строк:'))
c = int(input('введите колличество долек, которые нужно отломить:'))
k = int(a*b)
if (a == 1) and (c<b):
    print('возможно')
elif (b==1) and (c<a):
    print('возможно')
elif (k%2==0) and (c<k and (c%a==0 or c%b==0)):
    print('возможно')
else:
    print('Невозможно')
"""