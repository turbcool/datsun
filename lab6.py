print('Выберите номер задания')
task = 1#int(input())

if (task==0):
    expertMarks = [
        [10,7,9,3,4,5],
        [8,6,10,4,2,7]]
if (task==1):
    expertMarks = [
        [10,5,6,2],
        [6,2,9,4],
        [3,8,4,6]]
if (task==2):
    expertMarks = [
        [2,5,4,2,9,3],
        [6,8,2,10,5,4],
        [5,4,8,9,3,2]]
if (task==3):
    expertMarks = [
        [4,8,9,2],
        [7,2,3,10],
        [2,10,6,4],
        [1,6,9,3]]
if (task==4):
    expertMarks = [
        [1,6,9],
        [7,2,10],
        [5,8,3],
        [9,5,2],
        [10,4,6],
        [3,7,9]
    ]
if (task==5):
    expertMarks = [
        [1,6,4,10,4],
        [4,5,2,8,9],
        [8,4,1,5,10],
        [6,9,3,1,4],
        [2,7,4,6,9]
    ]
if (task==6):
    expertMarks = [
        [9,5,7,2],
        [1,8,9,4],
        [4,10,7,2]]
if (task==7):
    expertMarks = [
        [1,6,10],
        [7,2,9],
        [5,7,3],
        [9,5,2],
        [9,4,6],
        [3,8,10]]

n=len(expertMarks[0])
#marksMod = [n-mark for e in expertMarks for mark in e]
marksSum = [sum(e) for e in expertMarks]

mNorm = expertMarks
for i, e in enumerate(expertMarks):
    mNorm[i] = [m/marksSum[i] for m in e]

allSum = sum([m for expM in mNorm for m in expM])

mNormSum = [0] * n
for e in mNorm:
    for i, m in enumerate(e):
        mNormSum[i] = mNormSum[i] + e[i]

weights = [m/allSum for m in mNormSum]

print('Искомые веса целей:', weights)

maxW = max(weights)
mMaxI = [i+1 for i, x in enumerate(weights) if x == maxW]
print('Цели с наибольшим весом:', mMaxI)
