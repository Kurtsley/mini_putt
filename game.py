# Brian Beard 2024

import pyxel as px

BLOCK_SIZE = 16

BALL_SIZE = 6

HOLE_OUTLINE = 8
HOLE_INSIDE = 7

LEVEL_1 = """
##############################
#                            #
#                            #
#                            #
#                            #
#              0             #
#                            #
############                 #
#                            #
#                            #
#                            #
#HHHHHHHHHHH                 #
#HHHHHHHHHHH                 #
#HHHHHHHHHHH                 #
#HHHHHHHHHHH                 #
#HHHHHHHHHHH                 #
#                            #
#                            #
#                            #
#                  ###########
#                            #
#                            #
#                            #
#                            #
#                            #
#              B             #
#                            #
#                            #
#                            #
##############################
"""


class Level():
    def __init__(self):
        self.block = Block()
        self.ball = Ball()

    def draw(self, level_data: str):
        level_str = level_data.strip().split("\n")
        block_x = -BLOCK_SIZE
        block_y = -BLOCK_SIZE

        for str in level_str:
            block_y += BLOCK_SIZE
            for char in str:
                block_x += BLOCK_SIZE

                if block_x == 30 * BLOCK_SIZE:
                    block_x = 0

                if char == "#":
                    self.block.draw(block_x, block_y, "wall")
                elif char == "H":
                    self.block.draw(block_x, block_y, "hazard")
                elif char == "0":
                    self.block.draw(block_x, block_y, "hole")
                elif char == "B":
                    self.block.draw(block_x, block_y, "ball")
                else:
                    self.block.draw(block_x, block_y, "floor")


class Ball():
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

        self.ball = Ball()

    def draw_hole(self, x: int, y: int) -> None:
        px.circb(x, y, HOLE_OUTLINE, px.COLOR_WHITE)
        px.circ(x, y, HOLE_INSIDE, px.COLOR_BLACK)

    def draw(self, x: int, y: int, type: str) -> None:
        if type == "hazard":
            self.hazard = True
            self.color = px.COLOR_LIGHT_BLUE
        elif type == "wall":
            self.wall = True
            self.color = px.COLOR_BROWN
        else:
            self.floor = True
            self.color = px.COLOR_LIME

        px.rect(x, y, BLOCK_SIZE, BLOCK_SIZE, self.color)

        if type == "hole":
            self.draw_hole(x, y)

        if type == "ball":
            self.ball.draw(x, y)


class App():
    def __init__(self):
        px.init(600, 600, "Mini-Putt", fps=60)
        px.mouse(True)

        self.level = Level()

        px.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        px.cls(0)

        self.level.draw(LEVEL_1)


if __name__ == "__main__":
    App()
