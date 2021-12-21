from typing import Iterator
from itertools import product
from copy import deepcopy


class OctopusField:
    grid: list[list[int]]
    nc: int
    nr: int

    def __init__(self, raw: str):
        self.grid = [[int(c) for c in line] for line in raw.splitlines()]
        self.nc = len(self.grid[0])
        self.nr = len(self.grid)

    def __repr__(self):
        out = ""
        for row in self.grid:
            for c in row:
                out += str(c)
            out += "\n"
        return out

    def get_neighbours(self, r: int, c: int) -> Iterator[tuple[int, int]]:
        """
        A list of neighbouring points
        """
        steps = [-1, 0, 1]
        for dc, dr in product(steps, steps):
            if (
                not (dc == dr == 0) and 0 <= r + dr < self.nr and 0 <= c + dc < self.nc
            ):  # don't yield yourself and only yield things in the grid
                yield r + dr, c + dc

    def timestep(self):
        """
        Increment the octopus field by a timestep
        """
        newgrid = [[x + 1 for x in row] for row in self.grid]
        flashed = set()
        flash = []
        for r, c in product(range(self.nr), range(self.nc)):
            if newgrid[r][c] > 9:
                flash.append((r, c))
            flashed = set(flash)

        counter = 0
        while flash:
            sparky = flash.pop()
            counter += 1
            for r, c in self.get_neighbours(*sparky):
                newgrid[r][c] += 1
                if newgrid[r][c] > 9 and (r, c) not in flashed:
                    flash.append((r, c))
            flashed = flashed.union(flash)

        newgrid = [[x if x < 10 else 0 for x in row] for row in newgrid]
        self.grid = newgrid
        return counter


TEST1 = """1111
2222
3333
"""
tg = OctopusField(TEST1)
assert tg.nc == 4
assert tg.nr == 3

INPUT = """11111
19991
19191
19991
11111
"""
tg = OctopusField(INPUT)
for _ in range(2):
    print(tg)
    tg.timestep()

INPUT2 = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""
tg = OctopusField(INPUT2)
flashes = 0
for s in range(100):
    flashes += tg.timestep()
    print(s)
    print(tg)
    print()


tg = OctopusField(INPUT2)
steps = 1  # the first check will be after the first step (not the 0th)
while tg.timestep() != tg.nr * tg.nc:
    steps += 1
assert steps == 195

assert flashes == 1656
step100 = """0397666866
0749766918
0053976933
0004297822
0004229892
0053222877
0532222966
9322228966
7922286866
6789998766
"""
# assert tg.__repr__() == step100

with open("day11.txt") as f:
    raw = f.read()

OF = OctopusField(raw)
flashes = 0
for _ in range(100):
    flashes += OF.timestep()

OF = OctopusField(raw)
steps = 1
while OF.timestep() != OF.nr * OF.nc:
    steps += 1
print(steps)
