from typing import Counter


test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

with open("day03.txt") as fi:
    report = fi.read()


def find_delta_and_epsilon(report: str) -> str:
    data = report.splitlines()
    delta = ""
    epsilon = ""
    for i, _ in enumerate(data[0]):
        pos = [p[i] for p in data]
        c = Counter(pos)
        mc = c.most_common()
        delta += mc[0][0]
        epsilon += mc[1][0]
    return delta, epsilon


def filter_value(data, pos, most=True):
    vals = [d[pos] for d in data]
    c = Counter(vals)
    if c["1"] >= c["0"]:
        mc = 1
    else:
        mc = 0
    if not most:
        mc = abs(mc - 1)
    return str(mc)


def find_ratings(report: str, most: bool) -> str:
    data = report.splitlines()
    for pos, _ in enumerate(data[0]):
        mc = filter_value(data, pos, most)
        data = [d for d in data if d[pos] == mc]
        if len(data) == 1:
            break
    return data[0]


delta, epsilon = find_delta_and_epsilon(test_input)
print(delta, epsilon)
assert int(delta, 2) * int(epsilon, 2) == 198
assert int(find_ratings(test_input, True), 2) == 23
assert int(find_ratings(test_input, False), 2) == 10

delta, epsilon = find_delta_and_epsilon(report)
print(int(delta, 2), int(epsilon, 2), int(delta, 2) * int(epsilon, 2))
o2 = int(find_ratings(report, True), 2)
co2 = int(find_ratings(report, False), 2)
print(o2, co2, o2 * co2)
