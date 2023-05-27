# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


import os
def clear_console():
    os.system("cls")
clear_console()


print("Введи N: ")
degree = N = int(input())
i = 0
while 2**i <= N:
    print(2**i, end = " ")
    i = i + 1
