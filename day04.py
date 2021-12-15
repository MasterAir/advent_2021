from typing import List

test_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


class BingoBoard:
    grid: List[List[int]]
    marked: List[List[bool]]
    WIDTH: int

    def __init__(self, indata: str) -> None:
        self.grid = [int(d) for d in indata.split()]
        self.marked = [False for _ in self.grid]
        self.WIDTH = 5

    def mark(self, i: int) -> None:
        try:
            self.marked[self.grid.index(i)] = True
        except ValueError:
            pass

    def check(self) -> bool:
        # check horizontal
        i = 0
        while i < len(self.marked):
            if all(self.marked[i : i + self.WIDTH]):
                return True
            i += self.WIDTH
        i = 0
        # check vertical
        while i < self.WIDTH:
            if all(self.marked[i :: self.WIDTH]):
                return True
            i += 1
        return False

    def score(self, num):
        out = [d for d, m in zip(self.grid, self.marked) if not m]
        return sum(out) * num


class Game:
    boards: List[BingoBoard]
    seq: List[int]
    indata: List[str]
    turn: int

    def __init__(self, infile: str) -> None:
        self.indata = infile.split("\n\n")
        self.seq = [int(d) for d in self.indata[0].split(",")]
        self.boards = [BingoBoard(d) for d in self.indata[1:]]
        self.turn = 0

    def take_turn(self) -> int:
        num = self.seq[self.turn]
        print(num)
        for board in self.boards:
            board.mark(num)
            if board.check():
                return board.score(num)
        self.turn += 1
        return 0

    def take_turn_2(self) -> int:
        # Chuck boards that win until we have only one board
        num = self.seq[self.turn]
        for board in self.boards:
            board.mark(num)
        winners = [board.check() for board in self.boards]
        self.boards = [board for board, win in zip(self.boards, winners) if not win]
        self.turn += 1
        return num

    def play(self) -> int:
        score = 0
        while score == 0:
            # print(self.seq[self.turn], len(self.boards))
            score = self.take_turn()
        if self.turn > len(self.seq):
            raise RuntimeError
        return score

    def wins_last(self) -> int:
        while len(self.boards) > 1:
            print(self.seq[self.turn], len(self.boards))
            num = self.take_turn_2()
        breakpoint()
        return self.play()


g = Game(test_data)
b = g.boards[0]
score = g.play()
g = Game(test_data)
last_board = g.wins_last()

with open("day04.txt") as fi:
    input_cards = fi.read()
g2 = Game(input_cards)
print(g2.play())
g2 = Game(input_cards)
print(g2.wins_last())