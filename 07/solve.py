from aocd import data

L = [x.split(": ") for x in data.splitlines()]
M = [(int(s), [int(x) for x in e.split()]) for (s,e) in L]
find = lambda t, L, ops: L[0] == t if len(L) == 1 else any(find(t, [f(L[0], L[1])] + L[2:], ops) for f in ops)
print(sum(t for (t,L) in M if find(t, L, ops := [int.__add__, int.__mul__])))
print(sum(t for (t,L) in M if find(t, L, ops + [lambda x, y: int(str(x)+str(y))])))
