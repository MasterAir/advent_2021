from os import path
from typing import List, Tuple
from numpy import ndarray

test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def parse_path(path: str) -> Tuple[int]:
    point1, point2 = path.split(" -> ")
    x1, y1 = point1.split(",")
    x2, y2 = point2.split(",")
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    return int(x1), int(x2), int(y1), int(y2)


class Grid:
    grid: ndarray
    nx: int
    ny: int
    path_length: int
    num_paths: int

    def __init__(self):
        self.nx = 1000
        self.ny = 1000
        self.grid = ndarray([self.nx, self.ny], dtype=int)
        self.path_length = 0
        self.num_paths = 0

    def draw_orthogonal_paths(self, paths: str) -> None:
        for path in paths.splitlines():
            x1, x2, y1, y2 = parse_path(path)
            if not (x1 == x2 or y1 == y2):
                continue
            print(x1, x2, y1, y2)
            self.num_paths += 1
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    self.grid[x, y] += 1
                    self.path_length += 1

    def __repr__(self) -> str:
        return self.grid[:10, :10].__repr__()

    def n_crossings(self) -> int:
        counter = 0
        for row in self.grid:
            for val in row:
                if val > 1:
                    counter += 1
        return counter


grid = Grid()
grid.draw_orthogonal_paths(test_input)
assert grid.n_crossings() == 5

GRID = Grid()
indata = open("day05.txt").read()
GRID.draw_orthogonal_paths(indata)
print(GRID.n_crossings())