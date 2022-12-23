# Реализуйте алгоритм перемешивания списка (рандомно поменять местами элементы списка между собой).

import random
n = int(input("Введите целое положительное число "))
ran = range(n)
numbers = list(ran)
print(numbers)

for i in numbers:
    x = random.randint(0, n-1)
    temp = numbers[i]
    numbers[i] = numbers[x]
    numbers[x] = temp
print(numbers)