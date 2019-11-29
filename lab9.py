prefs = [
    [1, 3, 2, 5, 4],
    [1, 2, 4, 3, 5],
    [1, 2, 5, 3, 4],
    [2, 3, 1, 5, 4],
    [2, 4, 3, 1, 5]
]

prefs = [
    [1,2,3],
    [3,2,1],
    [2,1,3]
]

n = len(prefs[0])
marks = []

for i in range(0, n):
    temp = [0]*n
    for j in range(0, n):
        count = 0
        for k in range(0, n):
            if prefs[k].index(i + 1) < prefs[k].index(j + 1):
                count = count + 1
        temp[j] = count
    marks.append(temp)

for m in marks:
    print(m)

w = [0]*n
for i in range(0, n):
    for j in range(0, n):
        if marks[i][j] > marks[j][i] and i != j:
            w[i] = w[i] + 1

print()
print(w)

maxW = max(w)
mMaxI = [i+1 for i, x in enumerate(w) if x == maxW]

print('Лучшая цель: ' + str(mMaxI))
