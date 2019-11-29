import itertools
import random
n = int(input('Введите количество проектов: '))
e = int(input('Введите количество экспертов: '))

prNum = [0] * n
for i, p in enumerate(prNum):
    prNum[i] = i+1

prComb = list(itertools.combinations(prNum, 2))
cols = len(prComb) * 2
#1. Сгенерируем оценки:
marks = [[0] * cols]*e
for i, e in enumerate(marks):
    # итерация по парам:
    tempE = [0]*cols
    for j in range(0, len(e), 2):
        tempE[j] = random.randint(0, 20)*0.05
        tempE[j + 1] = 1 - tempE[j]
        tempE[j] = round(tempE[j], 2)
        tempE[j + 1] = round(tempE[j + 1], 2)
    marks[i] = tempE

#2. Посчитаем суммы оценок
numbers = [item for sublist in prComb for item in sublist]
sumByCol = [sum(x) for x in zip(*marks)]
marksByNumber = list(zip(numbers, sumByCol))
sums = []
for i, g in itertools.groupby(sorted(marksByNumber), key=lambda x: x[0]):
    sums.append((i, sum(v[1] for v in g)))

#3. Посчитаем их веса
sumAll = sum(v[1] for v in sums)
weights = [(v[0], v[1] / sumAll) for v in sums]
weights.sort(key=lambda x: x[1], reverse=True)

#4. Выведем на экран
# переменные
table_width = cols * 7
# форматы
header_f = '{:^'+str(table_width)+'}'
row_f = '{:^6} {:^6}|' * int(cols / 2)
# заголовок
header_top_line = '+' + '-' * (table_width - 1) + '+'
header_numbers = '|' + \
    row_f.format(*numbers)
header_bot_line = '+' + '-------------+' * int(cols / 2)
console_clear = '\n' * 100

# вызов вывода
print(console_clear)
print(header_f.format('Сгенерированные оценки'))
print(header_top_line)
print(header_numbers)
print(header_bot_line)
for l in marks:
    print('|'+row_f.format(*l))

print()
print(header_f.format('Веса проектов'))

for i, w in weights:
    print('Проект ' + str(i) + ': ' + str(round(w, 2)))

print('\nЛучший проект: ' + str(weights[0][0]))
