# Brian Beard 2024

import pyxel as px

BLOCK_SIZE = 12

BALL_SIZE = 5

LEVEL_1 = """
##############################
#                            #
#                            #
#                            #
#                            #
#              0             #
#                            #
#                            #
#                            #
#                            #
#                            #
#                            #
#    H                       #
#                            #
#                            #
#                            #
#                            #
#                            #
#                            #
#                            #
#                            #
#                            #
#                            #
#                            #
#                            #
#             B              #
#                            #
#                            #
#                            #
#                            #
##############################
"""


class Level():
    def __init__(self):
        self.block = Block()
        self.ball = Ball()

    def load(self, level_data: str):
        level_str = LEVEL_1.split("\n")
        block_type = None
        for char in level_str:
            match char:
                case "#":
                    block_type = self.block.wall
                case "H":
                    block_type = self.block.hazard
                case "B":
                    pass
                case "0":
                    block_type = self.block.hole
                case _:
                    block_type = self.block.floor

            self.block.draw()


class Ball():
    def __init__(self):
        pass

    def draw(self, x: int, y: int) -> None:
        px.circ(x, y, BALL_SIZE, px.COLOR_WHITE)


class Block():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = None
        self.hazard = False
        self.wall = False
        self.floor = False
        self.hole = False

    def draw_hole(self, x: int, y: int) -> None:
        px.circb(x, y, 6, px.COLOR_WHITE)
        px.circ(x, y, 5, px.COLOR_BLACK)

    def draw(self, x: int, y: int, type: str) -> None:
        if type == "hazard":
            self.hazard = True
            self.color = px.COLOR_LIGHT_BLUE
        elif type == "wall":
            self.wall = True
            self.color = px.COLOR_BROWN
        elif type == "floor":
            self.floor = True
            self.color = px.COLOR_LIME
        elif type == "hole":
            self.hole = True
            self.draw_hole(x, y)
            return

        px.rect(x, y, BLOCK_SIZE, BLOCK_SIZE, self.color)


class App():
    def __init__(self):
        px.init(600, 600, "Mini-Putt", display_scale=2)
        px.mouse(True)

        self.level = Level()
        self.level.load(LEVEL_1)

        px.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        px.cls(0)


if __name__ == "__main__":
    App()
