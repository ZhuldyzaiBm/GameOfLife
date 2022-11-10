import time
from typing import List, Tuple, Generator


class Life:
    state: List[List[bool]]
    m: int
    n: int

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.state = []
        for i in range(m):
            self.state.append([False for j in range(n)])

    def __repr__(self) -> str:
        return str(self.state)

    def neighbours(self, i: int, j: int) -> Generator[Tuple[int, int], None, None]:
        for line in range(self.m):
            for clmn in range(self.n):
                if line + 1 == i and clmn + 1 == j:
                    yield line, clmn
                if line + 1 == i and clmn == j:
                    yield line, clmn
                if line + 1 == i and clmn - 1 == j:
                    yield line, clmn
                if line == i and clmn + 1 == j:
                    yield line, clmn
                if line == i and clmn - 1 == j:
                    yield line, clmn
                if line - 1 == i and clmn - 1 == j:
                    yield line, clmn
                if line - 1 == i and clmn + 1 == j:
                    yield line, clmn
                if line - 1 == i and clmn == j:
                    yield line, clmn

    def nextstate(self) -> None:
        next = []
        for i in range(self.m):
            linee = []
            for j in range(self.n):
                num = 0
                for ln, cl in self.neighbours(i, j):
                    if self.state[ln][cl]:
                        num = num + 1
                if self.state[i][j] and 2 <= num and num<= 3:
                    linee.append(True)
                elif not self.state[i][j] and num == 3:
                    linee.append(True)
                else:
                    linee.append(False)
            next.append(linee)
        self.state = next

    def __str__(self) -> str:
        c = ""
        for i in range(self.m):
            for j in range(self.n):
                if self.state[i][j]:
                    c = c + "#"
                if not self.state[i][j]:
                    c = c + "."
            c = c + "\n"
        return c

    def addfigure(self, i: int, j: int, figure: List[str]) -> None:
        hor = 0
        for rw in figure:
            vert = 0
            for cn in rw:
                if 0 > i + hor or i + hor > self.m or 0 > j + vert or j + vert > self.n:
                    raise ValueError("Out of grid")
                if cn == '#':
                    self.state[i + hor][j + vert] = True
                vert = vert + 1
            hor = hor + 1


def start():
    toad = [".###",
            "###."]
    blinker = ["###"]
    block = ["..##..",
             "..##.."]
    glidergun = ["...................................#............",
                 ".................................#.#............",
                 ".......................##......##............##.",
                 "......................#...#....##............##.",
                 "...........##........#.....#...##...............",
                 "...........##........#...#.##....#.#............",
                 ".....................#.....#.......#............",
                 "......................#...#.....................",
                 ".......................##......................."]
    lf = Life(50, 80)

    lf.addfigure(10, 10, glidergun)
    lf.addfigure(30, 10, toad)
    lf.addfigure(40, 15, blinker)
    while True:
        print(lf)
        print("press Ctrl-C to stop")
        lf.nextstate()
        time.sleep(0.25)


start()
