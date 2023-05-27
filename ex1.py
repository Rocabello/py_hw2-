# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
import os
def clear_console():
  os.system('cls')
clear_console()
import random


print ("Введи кол-во монеток: ")
money = int(input())
serve=[0,1]
print("Орел - 1, решка - 0")


eagle = tail = 0
res = []
for i in range(money):
    x = random.choice(serve)
    res.append(x)
    if x == 0:
      tail += 1
    else: 
      eagle += 1

print(f'Получившийся бросок: {res}') 

if eagle>tail:
   print(f'Орлов больше - их: {eagle}, нужно перевернуть {tail} решек.')
elif eagle==tail:
   print(f'Выпало одинаковые количество орлов и решек по {eagle}')
else:
   print(f'Решек больше - их: {tail}, нужно перевернуть {eagle} орла.')


    


