class State:
    def __init__(self, left=None, right=None, boat=None):
        self.left = [0, 0, 0, 1, 1, 1] if left is None else left
        self.right = [] if right is None else right
        self.boat = "left" if boat is None else boat

    def showState(self):
        print(self.left, " < ç > | " if self.boat == 'left' else " | < ç > ", self.right)

    def getSides(self):
        return (self.left, self.right) if self.boat == "left" else (self.right, self.left)

    def getSidesString(self):
        return ("left", "right") if self.boat == "left" else ("right", "left")

    def switchBoatSide(self):
        self.boat = "right" if self.boat == 'left' else "left"

    def move(self, ele1, _from, to):

        if _from == to:
            print("Same side")
            return False

        if _from == "left" and to == "right":
            self.left.remove(ele1)
            self.right.append(ele1)
            return True

        if _from == "right" and to == "left":
            self.right.remove(ele1)
            self.left.append(ele1)
            return True

        print(f"Wrong from/to {_from} - {to}")
        return False

    def move_2(self, ele1, ele2, _from, to):

        if _from == to:
            print("Same side")
            return False

        if _from == "left" and to == "right":
            self.left.remove(ele1)
            self.left.remove(ele2)
            self.right.append(ele1)
            self.right.append(ele2)
            return True

        if _from == "right" and to == "left":
            self.right.remove(ele1)
            self.right.remove(ele2)
            self.left.append(ele1)
            self.left.append(ele2)
            return True

        print(f"Wrong from/to {_from} - {to}")
        return False


def isGameOver(s: State):
    # for each shore, check if game is over
    # for shore in [s.left, s.right]:
    #     if len(shore) > 0:
    #         if shore.count(1) > shore.count(0):
    #             print(f"there are more devils than priests in one shore")
    #             return True

    # print(type(s))
    # print(s.showState())

    if s.left.count(1) > 0 and s.left.count(0) > 0:
        if s.left.count(1) > s.left.count(0):
            print(f"there are more devils than priests in one shore")
            s.showState()
            return True

    if s.right.count(1) > 0 and s.right.count(0) > 0:
        if s.right.count(1) > s.right.count(0):
            print(f"there are more devils than priests in one shore")
            s.showState()
            return True

    # if len(s['left']) > 0:
    #     if s['left'].count(1) > s['left'].count(0):
    #         print(f"there are more devils than priests in the {'left'} side of the shore")
    #         return True
    #
    # if len(s['right']) > 0:
    #     if s['right'].count(1) > s['right'].count(0):
    #         print(f"there are more devils than priests in the {'right'} side of the shore")
    #         return True

    return False


def isWin(s):
    if len(s.left) == 0:
        print("\nWIN!!\n")
        s.showState()
        return True
    return False


def row_2(s, a, b) -> State:
    sideA, sideB = s.getSides()

    # if the move isn't possible
    if a not in sideA or b not in sideA:
        print("Impossible move - no characters")
        return s

    # not enough people too move
    if a == b and sideA.count(a) < 2:
        print("Impossible move - not enough people")
        return s

    s.move_2(a, b, *s.getSidesString())
    s.switchBoatSide()

    return s


def row(s, a) -> State:
    sideA, sideB = s.getSides()

    # if the move isn't possible
    if a not in sideA:
        print("Impossible move - no characters")
        return s

    s.move(a, *s.getSidesString())
    s.switchBoatSide()

    return s


def manualPlay(s: State):
    if isGameOver(s):
        return False

    if isWin(s):
        return True

    s.showState()

    choice = input("""
    1 - send 1 priest 🕋
    2 - send 2 priests 🕋
    3 - send 1 devil 👿
    4 - send 2 devils 👿
    5 - send 1 priest + 1 devil ☯
    0 - reset
    """)

    if choice == "1":
        # send 0
        manualPlay(row(s, 0))

    if choice == "2":
        # send 0 0
        manualPlay(row_2(s, 0, 0))

    if choice == "3":
        # send 1
        manualPlay(row(s, 1))

    if choice == "4":
        # send 1 1
        manualPlay(row_2(s, 1, 1))

    if choice == "5":
        # send 0 1
        manualPlay(row_2(s, 0, 1))

    if choice == "0":
        # reset
        print("\n## New Game ##")
        manualPlay(State())


# TODO : BFS, DFS, fix bugs
def solve_dfs(s: State):
    if isGameOver(s):
        return False

    if isWin(s):
        return True

    # send 0 0
    solve_dfs(row_2(s, 0, 0))
    # send 0 1
    solve_dfs(row_2(s, 0, 1))
    # send 1 1
    solve_dfs(row_2(s, 1, 1))


if __name__ == '__main__':
    # state = State()
    # state.showState()
    # play(state)
    while 1:
        print("\n## New Game ##")
        manualPlay(State())
