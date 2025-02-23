from functools import cache

from aocd import data


@cache
def best_dirpad(x, y, dx, dy, robots, invalid):
    ret = None
    todo = [(x, y, "")]

    while len(todo) > 0:
        x, y, path = todo.pop(0)

        if x == dx and y == dy:
            temp = best_robot(path + "A", robots - 1)
            ret = temp if ret is None else min(ret, temp)
        elif (x, y) != invalid:
            if x < dx:
                todo.append((x + 1, y, path + ">"))
            elif x > dx:
                todo.append((x - 1, y, path + "<"))
            if y < dy:
                todo.append((x, y + 1, path + "v"))
            elif y > dy:
                todo.append((x, y - 1, path + "^"))

    return ret


def best_robot(path, robots):
    if robots == 1:
        return len(path)

    ret = 0
    pad = decode_pad("X^A<v>", 3)
    x, y = pad["A"]

    for val in path:
        dx, dy = pad[val]
        ret += best_dirpad(x, y, dx, dy, robots, pad["X"])
        x, y = dx, dy

    return ret


def cheapest(x, y, dx, dy, robots, invalid):
    ret = None
    todo = [(x, y, "")]
    while len(todo) > 0:
        x, y, path = todo.pop(0)
        if x == dx and y == dy:
            temp = best_robot(path + "A", robots)
            ret = temp if ret is None else min(ret, temp)
        elif (x, y) != invalid:
            if x < dx:
                todo.append((x + 1, y, path + ">"))
            elif x > dx:
                todo.append((x - 1, y, path + "<"))
            if y < dy:
                todo.append((x, y + 1, path + "v"))
            elif y > dy:
                todo.append((x, y - 1, path + "^"))
    return ret


def decode_pad(val, width):
    ret = {}
    for x, val in enumerate(val):
        ret[val] = (x % width, x // width)
    return ret


def calc(values, mode):
    ret = 0
    pad = decode_pad("789456123X0A", 3)
    for row in values:
        result = 0
        x, y = pad["A"]
        for val in row:
            dx, dy = pad[val]
            result += cheapest(x, y, dx, dy, 3 if mode == 1 else 26, pad["X"])
            x, y = dx, dy
        ret += result * int(row[:-1].lstrip("0"))
    return ret


def run(values):
    print(calc(values, 1))
    print(calc(values, 2))


values = data.splitlines()
run(values)
