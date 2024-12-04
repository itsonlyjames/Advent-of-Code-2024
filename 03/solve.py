import re

from aocd import data, submit

sum = 0
all = re.findall("do\(\)|don't\(\)|mul\(\d+,\d+\)", data)
enabled = True
for mul in all:
    if mul == "don't()":
        enabled = False
    elif mul == "do()":
        enabled = True
    if enabled and mul.startswith("mul"):
        calc = re.split("\(|,|\)", mul)
        sum += int(calc[1]) * int(calc[2])

submit(sum)
