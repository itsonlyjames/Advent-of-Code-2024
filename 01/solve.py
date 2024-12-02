from aocd import data, submit

[la, ra] = [[], []]
for i in data.splitlines():
    [l,r] = i.split('   ')
    l = int(l)
    r = int(r)
    la.append(l)
    ra.append(r)

la = sorted(la)
ra = sorted(ra)

sum = 0
for i in range(len(la)):
    dist = abs(la[i] - ra[i])
    count = ra.count(la[i])
    sum += (la[i] * count)

submit(sum)
