print('Выберите номер задания')
task = int(input())

if (task==0):
    expertMarks = [
        [1,3,2,6,5,6],
        [2,4,1,5,6,3]]
if (task==1):
    expertMarks = [
        [1,5,4,2,6,3],
        [3,4,1,6,5,2],
        [5,2,4,6,3,1]]
if (task==2):
    expertMarks = [
        [2,3,4,1],
        [3,1,2,4],
        [1,4,3,2],
        [1,3,4,2]]
if (task==3):
    expertMarks = [
        [1,2,3],
        [2,1,3],
        [2,3,1],
        [3,2,1],
        [3,1,2],
        [1,2,3]
    ]
if (task==4):
    expertMarks = [
        [1,3,2,5,4],
        [2,3,1,4,5],
        [4,2,1,3,5],
        [3,5,2,1,4],
        [1,4,2,3,5]
    ]
if (task==5):
    expertMarks = [
        [3,2,4,1],
        [1,4,3,2],
        [2,3,4,1]
    ]
if (task==6):
    expertMarks = [
        [1,2,3],
        [2,1,3],
        [2,3,1],
        [3,2,1],
        [3,1,2],
        [1,2,3]
    ]

n=len(expertMarks[0])
#marksMod = [n-mark for e in expertMarks for mark in e]
marksMod = []
for e in expertMarks:
    marksMod.append([n-mark for mark in e])
    
mSum = [0] * n
for e in marksMod:
    for i, m in enumerate(e):
        mSum[i] = mSum[i] + e[i]
        
allSum = sum(mSum)
weights = [round(m/allSum, 2) for m in mSum]

print('Веса целей:', weights)

maxW = max(weights)
mMaxI = [i+1 for i, x in enumerate(weights) if x == maxW]
print('Цели с наибольшим весом:', mMaxI)
