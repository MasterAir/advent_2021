test_input = """199
200
208
210
200
207
240
269
260
263"""

with open("day01.txt") as fi:
    data = fi.read()


def increasing_depth(data: str):
    data = data.splitlines()
    counter = 0
    for depth, next_depth in zip(data, data[1:]):
        if int(next_depth) > int(depth):
            counter += 1
    return counter


def increasing_ave_depth(data: str):
    data = data.splitlines()
    data = [int(i) for i in data]
    data = [a + b + c for a, b, c in zip(data, data[1:], data[2:])]

    # I'm lazy, this should call increasing_depth
    counter = 0
    for depth, next_depth in zip(data, data[1:]):
        if int(next_depth) > int(depth):
            counter += 1
    return counter


assert increasing_depth(test_input) == 7
print(increasing_depth(data))

assert increasing_ave_depth(test_input) == 5
print(increasing_ave_depth(data))