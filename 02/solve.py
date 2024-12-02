from aocd import data, submit

safe = 0 

def is_safe(levels):
    isI = True
    isD = True
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if not (1 <= abs(diff) <= 3):
            isI = False
            isD = False
            break
        if diff < 0:
            isI = False
        if diff > 0:
            isD = False
    return isI or isD

for report in data.splitlines():
    levels = list(map(int, report.split()))

    if is_safe(levels):
        safe += 1
        continue

    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe(modified_levels):
            safe += 1
            break

submit(safe)
