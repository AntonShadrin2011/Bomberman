from time import process_time_ns

import arcade

CELL_W, CELL_H = 60, 60
ROW, COLUMN = 15, 17

SCREEN_WIDTH = CELL_W * COLUMN
SCREEN_HEIGHT = CELL_H * ROW
SCREEN_TITLE = 'BOMBERMAN'

class Map(arcade.Sprite):
    def __init__(self,pic ):
        super().__init__(pic)

class Bombery(arcade.Sprite):
    def __init__(self,pic ):
        super().__init__(pic)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.pole = arcade.load_texture('Blocks/BackgroundTile.png')

        self.bomber1_sprite = Bombery('Bomberman/Front/Bman_F_f00.png')
        self.bomber2_sprite = Bombery('Bomberman/Front/Bman_F_f00.png')

        self.bomber1_sprite.center_x = CELL_W
        self.bomber1_sprite.center_y = CELL_H
        self.bomber2_sprite.center_x = SCREEN_WIDTH - CELL_W
        self.bomber2_sprite.center_y = SCREEN_HEIGHT - CELL_H

        self.block_sprite = arcade.SpriteList()

        self.speed = 5
        self.mousePres = False
    def setup(self):
        for y in range(ROW):
            for x in range(COLUMN):
                block = Map('Blocks/SolidBlock.png')
                block.center_x = x * CELL_W + CELL_W / 2
                block.center_y = y * CELL_H + CELL_H / 2
                #self.block_sprite.append(block)

    def on_draw(self):
        self.clear()

        for y in range(ROW):
            for x in range(COLUMN):
                arcade.draw_texture_rectangle(x * CELL_W + CELL_W / 2,y * CELL_H + CELL_H / 2, CELL_W, CELL_H,
                                      texture=self.pole)
        self.block_sprite.draw()

        self.bomber1_sprite.draw()
        self.bomber2_sprite.draw()

    def on_update(self, delta_time: float):
        pass


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x // 60,y // 60)
        self.mousePres = True
        block = Map('Blocks/SolidBlock.png')
        block.center_x = x // 60 * CELL_W + CELL_W / 2
        block.center_y = y // 60 * CELL_H + CELL_H / 2
        self.block_sprite.append(block)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.mousePres == True:
            block = Map('Blocks/SolidBlock.png')
            block.center_x = x // 60 * CELL_W + CELL_W / 2
            block.center_y = y // 60 * CELL_H + CELL_H / 2
            self.block_sprite.append(block)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.mousePres = False


    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.W:
            self.bomber1_sprite.center_y += self.speed
        elif symbol == arcade.key.S:
            self.bomber1_sprite.center_y -= self.speed
        elif symbol == arcade.key.A:
            self.bomber1_sprite.center_x -= self.speed
        elif symbol == arcade.key.D:
            self.bomber1_sprite.center_x += self.speed


        elif symbol == arcade.key.UP:
            self.bomber2_sprite.center_y += self.speed
        elif symbol == arcade.key.DOWN:
            self.bomber2_sprite.center_y -= self.speed
        elif symbol == arcade.key.LEFT:
            self.bomber2_sprite.center_x -= self.speed
        elif symbol == arcade.key.RIGHT:
            self.bomber2_sprite.center_x += self.speed

    def on_key_release(self, symbol: int, modifiers: int):
        pass


okno = MyGame(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
okno.setup()
arcade.run()


"""
У нас есть функция сетап, где выставлялись бедрок блоки  (которые нельзя сломать), там немного заменить код
И сделать обычные блоки, которые будут выставлять автоматически, заполняя всё или некоторую часть поля

Короче говоря - создать класс для обычных блоков (которые можно взорвать) и закинуть их в сетап

2. Подумать, как сделать так, чтобы можно было при нажатии на какую-то клавишу - просто сохранять нарисованную карту


"""