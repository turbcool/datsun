n=4
e1 = [
    [0, 29/30, 27/30, 1],
    [1/30, 0, 2/30, 1],
    [3/30, 28/30, 0, 1],
    [0, 0, 0, 0],
]
e2 = [
    [0, 28/30, 1/30, 29/30],
    [2/30,0,0,29/30],
    [29/30,1,0,1],
    [1/30,1/30,0,0],
]

pref1 = [sum(x) for x in e1]
pref2 = [sum(x) for x in e2]

q1 = [x/(n*(n-1)) for x in pref1]
q2 = [x/(n*(n-1)) for x in pref2]

w = [x + y for x, y in zip(q1, q2)]

print(w)

maxW = max(w)
mMaxI = [i+1 for i, x in enumerate(w) if x == maxW]

print('Цели с наибольшим весом:', mMaxI)
