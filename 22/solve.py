import math
from collections import defaultdict

from aocd import data

MODULO = 16777216


def evolve(num):
    # Step 1
    num ^= (num << 6) % MODULO
    # Step 2
    num ^= (num // 32) % MODULO
    # Step 3
    num ^= (num << 11) % MODULO
    return num


def evolve_n_times(num, n):
    for i in range(n):
        num = evolve(num)
    return num


def ones_and_delta(init_secret, times):
    prev = init_secret % 10
    secret = init_secret
    yield (prev, None)
    for _i in range(times):
        secret = evolve(secret)
        nxt = secret % 10
        yield (nxt, nxt - prev)
        prev = nxt


def part1(init_secrets):
    evolved_sum = sum(evolve_n_times(init_secret, 2000) for init_secret in init_secrets)
    print(f"Part 1 total sum: {evolved_sum}")


def get_scores(init_secret, times):
    prices = {}
    iter_ones_delta = ones_and_delta(init_secret, times)
    next(iter_ones_delta)  # Skip first
    (_, a) = next(iter_ones_delta)
    (_, b) = next(iter_ones_delta)
    (_, c) = next(iter_ones_delta)
    (price, d) = next(iter_ones_delta)
    while True:
        if (a, b, c, d) not in prices:
            prices[(a, b, c, d)] = price
        a, b, c = b, c, d
        (price, d) = next(iter_ones_delta, (None, None))
        if d is None:
            break
    return prices


def part2(init_secrets):
    evolves = 2000
    sum_sequence_scores = defaultdict(int)
    for init_secret in init_secrets:
        secret_scores = get_scores(init_secret, evolves)
        for seq, price in secret_scores.items():
            sum_sequence_scores[seq] += price
    best_price = max(price for price in sum_sequence_scores.values())
    print(f"Part 2 best price: {best_price}")


secrets = [int(line) for line in data.splitlines()]
part1(secrets)
part2(secrets)
