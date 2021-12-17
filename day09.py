from itertools import product


RAW = """2199943210
3987894921
9856789892
8767896789
9899965678"""


orthogonal = ((-1, 0), (1, 0), (0, 1), (0, -1))


class Grid:
    points: list[list[int]]
    max_height: int
    xs: int
    ys: int

    def __init__(self, raw: str):
        self.points = []
        for line in raw.splitlines():
            self.points.append([int(c) for c in line])
        self.max_height = max(max(self.points))
        self.ys = len(self.points)
        self.xs = len(self.points[0])

    def get_neighbours(self, x, y) -> list[int]:
        neighbours = []
        for dx, dy in orthogonal:
            if y + dy < 0 or x + dx < 0:
                continue
            try:
                n = self.points[y + dy][x + dx]
                neighbours.append(n)
            except IndexError:
                pass
        return neighbours

    def find_minima(self) -> list[tuple[int, int]]:
        minima = []
        for y in range(self.ys):
            for x in range(self.xs):
                neighbours = self.get_neighbours(x, y)
                if all(self.points[y][x] < n for n in neighbours):
                    minima.append((x, y))
        return minima

    def get_value(self, x, y) -> int:
        if not self.in_grid(x, y):
            return 9
        return self.points[y][x]

    def in_grid(self, x, y) -> bool:
        return -1 < x < self.xs and -1 < y < self.ys

    def get_score(self) -> int:
        minima = self.find_minima()
        score = 0
        for minimum in minima:
            score += self.get_value(*minimum) + 1
        return score

    def get_baisins(self) -> dict[tuple[int, int], int]:
        baisins = {}
        minima = self.find_minima()
        for minimum in minima:
            checked = set()
            new = set([minimum])
            update = set()
            while new:
                for point in new:
                    for dx, dy in orthogonal:
                        trial = (point[0] + dx, point[1] + dy)
                        if (
                            self.get_value(*trial) < 9
                            and self.in_grid(*point)
                            and trial not in checked
                        ):
                            update.add(trial)
                checked = checked.union(new)
                new = update.copy()
                update = set()

            baisins[minimum] = checked

        return baisins


if __name__ == "__main__":
    input = open("day09.txt").read()
    GRID = Grid(input)
    print(GRID.get_score())
    baisins = GRID.get_baisins()
    size = {k: len(v) for k, v in baisins.items()}
    print(sorted(size.values())[-3:])


g = Grid(RAW)
