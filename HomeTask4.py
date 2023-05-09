"""Задача 22: 
n = int(input('число n: '))
m = int(input('число m: '))
num1=[]
num2=[]
itog=[]
for i in range(n):
    num1.append(input('Введите: ' ))
for j in range(m):
    num2.append(input('Введите: '))
print(num1)
print(num2)

if n > m:
    for _ in range(n):
        if num1[_] in num2:
            itog.append(num1[_])
else:
    for c in range(m):
        if num2[c] in num1:
            itog.append(num2[c])

print(itog)"""

"""Задача 24"""


    