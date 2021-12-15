from statistics import mean

RAW = "16,1,2,0,4,2,7,1,2,14"
INPUT = [int(x) for x in RAW.split(",")]

def total_distance(positons:list, loc:int) -> int:
    """Calculate the total distance to all line up at loc"""
    return sum([
        abs(x) for x in [
            i - loc for i in positons
        ]
    ])

assert total_distance(INPUT, 2) == 37
assert total_distance(INPUT, 1) == 41
assert total_distance(INPUT, 3) == 39
assert total_distance(INPUT, 10) == 71


def find_fuel(dist:int) -> int:
    """
    Find fuel as specified in part 2
    """
    return int((abs(dist) * (abs(dist) + 1)) / 2)


def find_total_fuel(positions:list, loc:int) -> int:
    return sum([
        find_fuel(x) for x in [
            i - loc for i in positions
        ]
    ])


def find_loc(positions:list, fuel_function=total_distance) -> int:
    """
    Find the location where crabs in positions need to move the least to line up
    """
    dist = sum(positions) ** 9
    
    for p in range(max(positions)):
        this_dist = fuel_function(positions, p)
        if this_dist < dist:
            loc = p
            dist = this_dist
            print(p, fuel_function(positions, p))
    return loc, dist

dist = find_loc(INPUT)[1]
assert dist == 37

assert find_total_fuel(INPUT, 2) == 206
assert find_loc(INPUT, find_total_fuel) == (5, 168)

if __name__ == "__main__":
    with open("day07.txt") as fi:
        raw = fi.read()
    input = [int(x) for x in raw.split(",")]
    print(find_loc(input))
    print(find_loc(input, find_total_fuel))