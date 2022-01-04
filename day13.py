RAW = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


class Paper:
    points: set[tuple[int, int]]
    nr: int
    nc: int
    folds: list[tuple[str, int]]

    def __init__(self, RAW: str) -> None:
        points, folds = RAW.split("\n\n")
        points = [line.split(",") for line in points.splitlines()]
        points = [tuple(xy) for xy in points]
        points = [(int(xy[0]), int(xy[1])) for xy in points]
        self.points = set(points)

        self.nc = max([x[0] for x in self.points]) + 1
        self.nr = max([y[1] for y in self.points]) + 1

        folds = folds.splitlines()
        self.folds = [self.get_instr(fold) for fold in folds]

    @staticmethod
    def get_instr(line: str) -> tuple[str, int]:
        instr = line.split()[-1].split("=")
        return (instr[0], int(instr[1]))

    def fold_vertical(self, y):
        keep = set()
        folded = set()
        for point in self.points:
            if point[1] < y:
                keep.add(point)
            else:
                new_point = (point[0], y + (y - point[1]))
                folded.add(new_point)
        self.points = keep.union(folded)
        self.nr = max([y[1] for y in self.points]) + 1

    def fold_horizontal(self, x):
        keep = set()
        folded = set()
        for point in self.points:
            if point[0] < x:
                keep.add(point)
            else:
                new_point = (x + (x - point[0]), point[1])
                folded.add(new_point)
        self.points = keep.union(folded)
        self.nc = max([x[0] for x in self.points]) + 1

    def fold(self, nfolds=0):
        if nfolds == 0:
            nfolds = len(self.folds)
        to_fold = self.folds[:nfolds]
        for fold in to_fold:
            d, loc = fold
            if d == "y":
                self.fold_vertical(loc)
            elif d == "x":
                self.fold_horizontal(loc)
            else:
                raise RuntimeError(f"unknown direction: {d}")
        self.folds = self.folds[nfolds:]

    def __repr__(self) -> str:
        out = ""
        for r in range(self.nr):
            for c in range(self.nc):
                if (c, r) in self.points:
                    out += "@"
                else:
                    out += "."
            out += "\n"
        return out


p = Paper(RAW)

INDATA = open("day13.txt").read()
puzzle = Paper(INDATA)
puzzle.fold(1)
print(len(puzzle.points))
puzzle.fold()
print(puzzle)
