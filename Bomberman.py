import random
import arcade

CELL_W, CELL_H = 60, 60
ROW, COLUMN = 15, 17

SCREEN_WIDTH = CELL_W * COLUMN
SCREEN_HEIGHT = CELL_H * ROW
SCREEN_TITLE = 'BOMBERMAN'


class Map(arcade.Sprite):
    def __init__(self, pic):
        super().__init__(pic)


class Bombery(arcade.Sprite):
    def __init__(self, pic):
        super().__init__(pic)
    def update(self, delta_time: float = 1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y


class Block(arcade.Sprite):
    def __init__(self, pic):
        super().__init__(pic)

class Bomb(arcade.Sprite):
    def __init__(self, pic):
        super().__init__(pic)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title,update_rate = 1/1000)
        self.pole = arcade.load_texture('Blocks/BackgroundTile.png')

        self.bomber1_sprite = Bombery('Bomberman/Front/Bman_F_f00.png')
        self.bomber2_sprite = Bombery('Bomberman/Front/Bman_F_f00.png')

        self.bomber1_sprite.center_x = CELL_W
        self.bomber1_sprite.center_y = CELL_H
        self.bomber2_sprite.center_x = SCREEN_WIDTH - CELL_W
        self.bomber2_sprite.center_y = SCREEN_HEIGHT - CELL_H

        self.bedroc_sprite = arcade.SpriteList()
        self.nebedroc_sprite = arcade.SpriteList()
        self.bomb1_sprite = arcade.SpriteList()
        self.bomb2_sprite = arcade.SpriteList()

        self.speed = 5
        self.mousePres = False

    def setup(self):
        for y in range(ROW):
            for x in range(COLUMN):
                block = Map('Blocks/SolidBlock.png')
                block.center_x = x * CELL_W + CELL_W / 2
                block.center_y = y * CELL_H + CELL_H / 2
                # self.block_sprite.append(block)

                if random.random() < 0.3:
                    block = Block('Blocks/ExplodableBlock.png')
                    block.center_x = x * CELL_W + CELL_W / 2
                    block.center_y = y * CELL_H + CELL_H / 2
                    self.nebedroc_sprite.append(block)

    def on_draw(self):
        self.clear()

        for y in range(ROW):
            for x in range(COLUMN):
                arcade.draw_texture_rectangle(x * CELL_W + CELL_W / 2, y * CELL_H + CELL_H / 2, CELL_W, CELL_H,
                                              texture=self.pole)
        self.bedroc_sprite.draw()
        self.nebedroc_sprite.draw()


        self.bomber1_sprite.draw()
        self.bomber2_sprite.draw()

        self.bomb1_sprite.draw()
        self.bomb2_sprite.draw()

    def on_update(self, delta_time: float):
        self.bomber1_sprite.update()
        self.bomber2_sprite.update()
        self.bomb1_sprite.update()
        self.bomb2_sprite.update()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x // 60, y // 60)
        self.mousePres = True
        block = Map('Blocks/SolidBlock.png')
        block.center_x = x // 60 * CELL_W + CELL_W / 2
        block.center_y = y // 60 * CELL_H + CELL_H / 2
        self.bedroc_sprite.append(block)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.mousePres == True:
            block = Map('Blocks/SolidBlock.png')
            block.center_x = x // 60 * CELL_W + CELL_W / 2
            block.center_y = y // 60 * CELL_H + CELL_H / 2
            self.bedroc_sprite.append(block)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.mousePres = False

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.bomber1_sprite.change_y = 7
        elif symbol == arcade.key.S:
            self.bomber1_sprite.change_y = -7
        elif symbol == arcade.key.A:
            self.bomber1_sprite.change_x = -7
        elif symbol == arcade.key.D:
            self.bomber1_sprite.change_x = 7

        elif symbol == arcade.key.UP:
            self.bomber2_sprite.change_y = 7
        elif symbol == arcade.key.DOWN:
            self.bomber2_sprite.change_y = -7
        elif symbol == arcade.key.LEFT:
            self.bomber2_sprite.change_x = -7
        elif symbol == arcade.key.RIGHT:
            self.bomber2_sprite.change_x = 7

        elif symbol ==arcade.key.E:
            bomb = Bomb('Bomb/Bomb_f02.png')
            bomb.center_x = self.bomber1_sprite.center_x
            bomb.center_y = self.bomber1_sprite.center_y
            self.bomb1_sprite.append(bomb)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.bomber1_sprite.change_y = 0
        elif symbol == arcade.key.S:
            self.bomber1_sprite.change_y = 0
        elif symbol == arcade.key.A:
            self.bomber1_sprite.change_x = 0
        elif symbol == arcade.key.D:
            self.bomber1_sprite.change_x = 0

        elif symbol == arcade.key.UP:
            self.bomber2_sprite.change_y = 0
        elif symbol == arcade.key.DOWN:
            self.bomber2_sprite.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.bomber2_sprite.change_x = 0
        elif symbol == arcade.key.RIGHT:
            self.bomber2_sprite.change_x = 0


okno = MyGame(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
okno.setup()
arcade.run()