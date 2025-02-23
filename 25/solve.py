from aocd import data

locks, keys = [], []

for schematic in data.split("\n\n"):
    cols = list(zip(*schematic.splitlines()))
    print(cols)
    if schematic[0] == "#":
        locks.append([col.count("#") - 1 for col in cols])
    else:
        keys.append([col.count("#") - 1 for col in cols])

print(locks, keys)
print(sum(all(a + b <= 5 for a, b in zip(key, lock)) for key in keys for lock in locks))
