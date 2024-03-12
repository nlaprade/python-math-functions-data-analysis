# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:09:55 2024

@author: lapra
"""

# 1
def diff(number_one, number_two):
    if number_one > number_two:
        return number_one - number_two
    else:
        return number_two - number_one

print(diff(6, 2))
print(diff(10, 20))

# 2
def commissionff(commission):
    if commission > 1000:
        return (commission - 1000) * 0.01
    else:
        return 0

print(commissionff(900))
print(commissionff(1100))
print(commissionff(2000))

# 3
import math
def cal_trig(angle):
    sin = math.sin(angle)
    cos = math.cos(angle)
    tan = math.tan(angle)
    return str(sin) + " " + str(cos) + " " + str(tan)

print(cal_trig(0.2))
print(cal_trig(0))

# 4
def fac(number):
    if number == 0:
        return 1
    else:
        return number * fac(number - 1)

print(fac(3))
print(fac(6))

# 5
import random
def foo(number):
    count = {'evens': 0, 'odds': 0}
    for num in number:
       if num % 2 == 0:
           count['evens'] += 1
       else:
           count['odds'] += 1
    return count

lst = [random.randint(0, 10) for _ in range(10)]
print(lst)
print(foo(lst))

# 6
def count_letter(sentence, to_find):
    count = 0
    for char in sentence:
        if char == to_find:
            count += 1
    return count

sentence = 'Hello world, from narendra'
to_find = 'o'
print(f"There are {count_letter(sentence, to_find)} '{to_find}'s in '{sentence}'")

# 7
data = {}

text_data = '''Aksheshkumar,60.75,11.55,279.58
Aleksander,85.65,72.62,788.60
Aravind,46.15,37.72,627.42
Arielle,61.45,45.68,309.94
Arthur,51.60,20.20,423.43
Ashish,28.75,83.11,604.74
Carlos,8.65,29.51,287.57
Erwin,66.70,23.20,409.71
Femees,78.60,53.50,504.75
Gurneet,18.5,49.88,833.28
Harmandeep,87.80,51.34,145.15
Helal,42.35,33.75,940.60
Hoi,79.85,60.54,185.69
Hyunjune,28.0,64.91,703.63
Imane,6.40,66.90,384.85
Ishan,29.25,30.80,685.29
Jatin,60.55,76.33,502.21
Jiaxing,43.25,71.76,572.32
Jiya,91.55,93.50,958.41
John,13.10,91.64,970.18
Jongmin,62.80,74.57,312.19
Kenneth,58.15,79.23,171.61
Manan,41.95,85.34,502.70
Marvin,23.70,20.31,163.91
Megha,72.70,24.40,733.33
Mintu,73.50,99.78,413.14
Nusrat,98.95,35.64,417.89
Riaz,6.75,77.83,751.43
Ritesh,55.15,73.40,541.30
Sanchit,80.95,65.72,101.97
Santiago,11.10,33.42,725.69
Seoyoung,70.55,54.95,819.36
Shruthi,65.70,63.68,129.76
Thiri,70.70,49.74,191.98
Thu,14.20,38.55,913.43
Vincent,19.60,36.99,876.12
Yashkumar,57.35,18.95,934.21
Zhen,85.5,25.24,663.49'''

lines = text_data.split('\n')

for line in lines:
    parts = line.split(',')
    name = parts[0]
    values = parts[1:]
    data[name] = values

print(data)

# 8

data = {}

for line in lines:
    parts = line.split(',')
    name = parts[0]
    values = parts[1:]
    total = sum(float(part) for part in values)
    data[name] = total

print(data)













































