test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


class Submarine:
    x: int
    y: int

    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def move(self, instruction: str) -> None:
        direction, distance = instruction.split()
        distance = int(distance)
        if direction == "forward":
            self.x += distance
        elif direction == "down":
            self.y += distance
        elif direction == "up":
            self.y -= distance
        else:
            raise RuntimeError("Unexected direction")

    def follow_instructions(self, instructions: str) -> None:
        for inst in instructions.splitlines():
            self.move(inst)
            print(self.x, self.y)


class OvercomplicatedSubmarine:
    x: int
    y: int
    aim: int

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.aim = 0

    def move(self, instruction: str) -> None:
        direction, distance = instruction.split()
        distance = int(distance)
        if direction == "forward":
            self.x += distance
            self.y += self.aim * distance
        elif direction == "down":
            self.aim += distance
        elif direction == "up":
            self.aim -= distance
        else:
            raise RuntimeError("Unexected direction")

    def follow_instructions(self, instructions: str) -> None:
        for inst in instructions.splitlines():
            self.move(inst)
            print(self.x, self.y)


test_sub = Submarine()
test_sub.follow_instructions(test_input)
assert test_sub.x * test_sub.y == 150

real_sub = Submarine()
with open("day02.txt") as fi:
    instructions = fi.read()

real_sub.follow_instructions(instructions)
print(real_sub.x * real_sub.y)


test_sub_2 = OvercomplicatedSubmarine()
test_sub_2.follow_instructions(test_input)
assert test_sub_2.x * test_sub_2.y == 900

real_sub_2 = OvercomplicatedSubmarine()
with open("day02.txt") as fi:
    instructions = fi.read()

real_sub_2.follow_instructions(instructions)
print(real_sub_2.x * real_sub_2.y)
