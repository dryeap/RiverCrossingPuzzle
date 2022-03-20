from copy import copy, deepcopy


class State:
    def __init__(self, left=None, right=None, boat=None):
        self.left = [0, 0, 0, 1, 1, 1] if left is None else left
        self.right = [] if right is None else right
        self.boat = "left" if boat is None else boat

    def printState(self):
        print(self.showStateSimple())

    def showStateSimple(self):
        return self.left, "_ " if self.boat == 'left' else " _", self.right

    def getSides(self):
        return (self.left, self.right) if self.boat == "left" else (self.right, self.left)

    def getSidesString(self):
        return ("left", "right") if self.boat == "left" else ("right", "left")

    def switchBoatSide(self):
        self.boat = "right" if self.boat == 'left' else "left"

    def moveNoTemp(self, *eles):
        _from, to = self.getSides()

        if len(eles) == 2:
            if eles[0] == eles[1] and _from.count(eles[0]) < 2:
                # print("not enough people")
                # print(eles, _from)
                return False

            if eles[0] not in _from or eles[1] not in _from:
                # print("ele not in from")
                # print(eles, _from)
                return False
        else:
            if eles[0] not in _from:
                # print("ele not in from")
                # print(eles, _from)
                return False

        # print(f"before {self.printShowState()}")
        for ele in eles:
            _from.remove(ele)
            to.append(ele)

        # print(f"after  {self.printShowState()}")

        if isGameOver(self):
            return False
        self.switchBoatSide()

        return True


def isGameOver(s: State):
    # for each shore, check if game is over
    for shore in s.getSides():
        if shore.count(1) > 0 and shore.count(0) > 0:
            if shore.count(1) > shore.count(0):
                # print(f"there are more devils than priests in one shore")
                # print("no")
                return True

    return False


def isWin(s):
    if len(s.left) == 0:
        print(f"\n\n{s.showStateSimple()}\nGame won!!\n")
        return True
    return False


def row(s, eles) -> State:
    startState = deepcopy(s)

    # if move results in game over, return earlier state
    if not s.moveNoTemp(*eles):
        print(f"{eles} is game over")
        return startState

    return s


def manualPlay(s: State):
    if isGameOver(s):
        return False

    if isWin(s):
        return True
    s.printState()

    choice = input("""
    1 - send 1 priest 🕋
    2 - send 2 priests 🕋
    3 - send 1 devil 👿
    4 - send 2 devils 👿
    5 - send 1 priest + 1 devil ☯
    R - reset
    0 - exit
    """)

    if choice == "1":
        # send 0
        manualPlay(row(s, [0]))

    if choice == "2":
        # send 0 0
        manualPlay(row(s, [0, 0]))

    if choice == "3":
        # send 1
        manualPlay(row(s, [1]))

    if choice == "4":
        # send 1 1
        manualPlay(row(s, [1, 1]))

    if choice == "5":
        # send 0 1
        manualPlay(row(s, [0, 1]))

    if choice == "R":
        # reset
        print("\n## New Game ##")
        manualPlay(State())

    if choice == "0":
        return False


possible_moves = [[0], [0, 0], [1], [1, 1], [0, 1]]
seen = []
q = []
ctr = 0


def solve_dfs(s: State):
    global ctr

    if isWin(s):
        print(f"Moves tried: {ctr}")
        return True

    ctr += 1

    for m in possible_moves:
        # row() returns s unchanged if move is impossible
        temp_s = deepcopy(s)

        if temp_s.moveNoTemp(*m):
            t = (temp_s.showStateSimple(), m)  # tuple
            if t not in seen:
                q.append(temp_s)
                seen.append(t)

    print(f"Number of moves on queue: {ctr}")
    solve_dfs(q.pop(0))


# TODO : blue morphooooooo
def solve_dfs_verbose(s: State):
    global ctr

    if isWin(s):
        print(f"Moves tried: {ctr}")
        return True

    ctr += 1
    print(f"\nTrying moves for \n{s.showStateSimple()}\n")

    for m in possible_moves:
        # row() returns s unchanged if move is impossible
        temp_s = deepcopy(s)

        print(f"Move is {m}")

        if temp_s.moveNoTemp(*m):
            t = (temp_s.showStateSimple(), m)  # tuple
            if t not in seen:
                print(f"Valid move, add to queue")
                q.append(temp_s)
                seen.append(t)
            else:
                print(f"{t} has been checked")
        else:
            print("Move results in Game Over")

    print("\nMoves on queue:")
    for x in q:
        print(f"{x.showStateSimple()}")

    solve_dfs_verbose(q.pop(0))


def solve_bfs(s: State):
    global ctr
    if isWin(s):
        print(f"Moves tried: {ctr}")
        return True

    ctr += 1

    for m in possible_moves:
        # row() returns s unchanged if move is impossible
        temp_s = deepcopy(s)

        if temp_s.moveNoTemp(*m):
            t = (temp_s.showStateSimple(), m)  # tuple
            if t not in seen:
                q.append(temp_s)
                seen.append(t)

    print(f"Number of moves on stack: {ctr}")
    solve_bfs(q.pop(len(q) - 1))

def solve_bfs_verbose(s: State):
    global ctr
    if isWin(s):
        print(f"Moves tried: {ctr}")
        return True

    ctr += 1
    print(f"\nTrying moves for \n{s.showStateSimple()}\n")

    for m in possible_moves:
        # row() returns s unchanged if move is impossible
        temp_s = deepcopy(s)

        print(f"Move is {m}")

        if temp_s.moveNoTemp(*m):
            t = (temp_s.showStateSimple(), m)  # tuple
            if t not in seen:
                print(f"Valid move, add to queue")
                q.append(temp_s)
                seen.append(t)
            else:
                print(f"{t} has been checked")
        else:
            print("Move results in Game Over")

    print("\nMoves on stack:")
    for x in q:
        print(f"{x.showStateSimple()}")

    solve_bfs_verbose(q.pop(len(q) - 1))


if __name__ == '__main__':
    # state = State()
    # state.showState()
    # play(state)
    # solve_bfs(State())

    while (menu := input("""
        1 - Play
        2 - Solve using DFS
        2b- Solve using DFS (Verbose)
        3 - Solve using BFS
        3b- Solve using BFS (Verbose)
        0 - exit
        
        DFS uses Stack (LIFO)
        BFS uses Queue (FIFO)
""")) != "0":

        q, seen = [], []
        ctr = 0
        print(menu)

        if menu == "1":
            manual = True
            while manual:
                print("\n## New Game ##")
                manual = manualPlay(State())

        if menu == "2":
            solve_dfs(State())

        if menu == "3":
            solve_bfs(State())

        if menu == "2b":
            solve_dfs_verbose(State())

        if menu == "3b":
            solve_bfs_verbose(State())

    print("exit")

# TODO : add hints (right answer for each step)
