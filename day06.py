from collections import Counter


class Population:
    fish: Counter

    def __init__(self, raw: str) -> None:
        fish = [int(i) for i in raw.split(",")]
        self.fish = Counter(fish)

    def step(self) -> None:
        """
        Update fish so that fish reproduce after 7 days, new fish reproduce after 9
        """
        update = Counter()
        for new, old in zip(range(0, 8), range(1, 9)):
            update[new] = self.fish[old]
        # now reset the fish that have spawned new fish ...
        update[6] = update[6] + self.fish[0]
        # ... and add the new fish
        update[8] = self.fish[0]
        self.fish = update

    def number(self) -> int:
        return sum(self.fish.values())


INPUT = "3,4,3,1,2"
p = Population(INPUT)
for _ in range(256):
    p.step()
    print(p.number())

assert p.number() == 26984457539

day6in = "2,5,5,3,2,2,5,1,4,5,2,1,5,5,1,2,3,3,4,1,4,1,4,4,2,1,5,5,3,5,4,3,4,1,5,4,1,5,5,5,4,3,1,2,1,5,1,4,4,1,4,1,3,1,1,1,3,1,1,2,1,3,1,1,1,2,3,5,5,3,2,3,3,2,2,1,3,1,3,1,5,5,1,2,3,2,1,1,2,1,2,1,2,2,1,3,5,4,3,3,2,2,3,1,4,2,2,1,3,4,5,4,2,5,4,1,2,1,3,5,3,3,5,4,1,1,5,2,4,4,1,2,2,5,5,3,1,2,4,3,3,1,4,2,5,1,5,1,2,1,1,1,1,3,5,5,1,5,5,1,2,2,1,2,1,2,1,2,1,4,5,1,2,4,3,3,3,1,5,3,2,2,1,4,2,4,2,3,2,5,1,5,1,1,1,3,1,1,3,5,4,2,5,3,2,2,1,4,5,1,3,2,5,1,2,1,4,1,5,5,1,2,2,1,2,4,5,3,3,1,4,4,3,1,4,2,4,4,3,4,1,4,5,3,1,4,2,2,3,4,4,4,1,4,3,1,3,4,5,1,5,4,4,4,5,5,5,2,1,3,4,3,2,5,3,1,3,2,2,3,1,4,5,3,5,5,3,2,3,1,2,5,2,1,3,1,1,1,5,1"

REALP = Population(day6in)
for _ in range(256):
    REALP.step()
print(REALP.number())
