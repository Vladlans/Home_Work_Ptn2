# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 

N = int(input("Введите число больше двух "))
if N > 0:
    ran = range(-N, N+1)
else:
    ran = range(N, -N+1)
numbers = list(ran)
import random
position = [random.randint(0,N*2), random.randint(0,N*2)]
result = numbers[position[0]]*numbers[position[1]]
print(numbers)
print(position)
print('Произведение элементов на позициях [',position[0], '] и [', position[1],'] равна ', result)