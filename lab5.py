expertMarks = [
    [1,3,2,6,5,6],
    [2,4,1,5,6,3]
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
mMaxI = [i for i, x in enumerate(weights) if x == maxW]
print('Цели с наибольшим весом:', mMaxI)
