from copy import deepcopy

RAW = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

RAW2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

RAW3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


class Pathway:
    path: list[str]
    small_caves: set[str]
    small_cave_twice: bool

    def __init__(self, room: str) -> None:
        self.path = [room]
        self.small_caves = set()
        self.small_cave_twice = False

    def travel(self, room: str) -> None:
        if room.islower() and room in self.small_caves:
            self.small_cave_twice = True
        elif room.islower():
            self.small_caves.add(room)
        self.path.append(room)

    def allowed_step(self, room: str) -> bool:
        if room == "start":
            return False
        return not (room in self.path) or room.isupper()

    def allowed_step_long(self, room: str) -> bool:
        if room == "start":
            return False
        if self.small_cave_twice:
            return self.allowed_step(room)
        else:
            return True

    def __repr__(self) -> str:
        out = ""
        for r in self.path:
            out += f" --> {r}"
        return out


class Navigator:
    paths: dict[str, set[str]]

    def __init__(self, raw, end="end"):
        paths = {}
        for line in raw.splitlines():
            pathway = line.split("-")
            for fr, to in zip(pathway, reversed(pathway)):
                if fr in paths:
                    paths[fr].add(to)
                else:
                    paths[fr] = set([to])
        if end is not None:
            paths[end] = set()
        self.paths = paths
        print(self.paths)

    def find_routes(self, start="start", end="end"):
        routes = [Pathway(start)]
        finished_routes = []
        counter = 0
        while routes:
            counter += 1
            updated_routes = []
            for route in routes:
                room = route.path[-1]
                for step in self.paths[room]:
                    if step == end:
                        r = deepcopy(route)
                        r.travel(step)
                        finished_routes.append(r)
                    elif route.allowed_step(step):
                        r = deepcopy(route)
                        r.travel(step)
                        updated_routes.append(r)
            routes = updated_routes

        return finished_routes

    def find_long_routes(self, start="start", end="end"):
        routes = [Pathway(start)]
        finished_routes = []
        counter = 0
        while routes:
            counter += 1
            updated_routes = []
            for route in routes:
                room = route.path[-1]
                for step in self.paths[room]:
                    if step == end:
                        r = deepcopy(route)
                        r.travel(step)
                        finished_routes.append(r)
                    elif route.allowed_step_long(step):
                        r = deepcopy(route)
                        r.travel(step)
                        updated_routes.append(r)
            routes = updated_routes

        return finished_routes


n1 = Navigator(RAW)
n2 = Navigator(RAW2)
n3 = Navigator(RAW3)

input = open("day12.txt").read()
puzzle = Navigator(input)
print(len(puzzle.find_routes()))
print(len(puzzle.find_long_routes()))
