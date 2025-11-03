import random
import time

import arcade

CELL_W, CELL_H = 60, 60
ROW, COLUMN = 15, 17

SCREEN_WIDTH = CELL_W * COLUMN
SCREEN_HEIGHT = CELL_H * ROW
SCREEN_TITLE = 'BOMBERMAN'


class Boost(arcade.Sprite):
    def __init__(self, pic):
        super().__init__(pic, scale= 0.7)
        self.timer = time.time()
        print(self.timer)
    def update(self):
        pass


class Babax(arcade.Sprite):
    def __init__(self, pic):
        super().__init__(pic)
        self.timer = time.time()
        print(self.timer)
    def update(self):
        if time.time() - self.timer >= 5:
            self.kill()


class Map(arcade.Sprite):
    def __init__(self, pic):
        super().__init__(pic)


class Bombery(arcade.Sprite):
    def __init__(self, pic):
        super().__init__(pic,scale=0.7)
        self.move = False

    def update(self, delta_time: float = 1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT


class Block(arcade.Sprite):
    def __init__(self, pic):
        super().__init__(pic)


class Bomb(arcade.Sprite):
    def __init__(self, pic):
        super().__init__(pic, scale= 0.7)
        self.timer = time.time()
        print(self.timer)
    def update(self):
        if time.time() - self.timer >= 10:
            self.kill()
            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x
            bax.center_y = self.center_y
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x - 60
            bax.center_y = self.center_y + 60
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x
            bax.center_y = self.center_y + 60
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x + 60
            bax.center_y = self.center_y + 60
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x - 60
            bax.center_y = self.center_y
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x + 60
            bax.center_y = self.center_y
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x - 60
            bax.center_y = self.center_y - 60
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x
            bax.center_y = self.center_y - 60
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x + 60
            bax.center_y = self.center_y - 60
            okno.babax_sprite.append(bax)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, update_rate=1 / 1000)
        self.pole = arcade.load_texture('Blocks/BackgroundTile.png')

        self.bomber1_sprite = Bombery('Bomberman/Front/Bman_F_f00.png')
        self.bomber2_sprite = Bombery('Bomberman/Front/Bman_F_f00.png')

        self.coords = [
            [random.randint(0, 4), random.randint(0,4)],
            [random.randint(5, 9), random.randint(0,4)],
            [random.randint(10, 14), random.randint(0,4)],
            [random.randint(15, 16), random.randint(0,4)],

            [random.randint(0, 4), random.randint(5,9)],
            [random.randint(5, 9), random.randint(5,9)],
            [random.randint(10, 14), random.randint(5,9)],
            [random.randint(15, 16), random.randint(5,9)],

            [random.randint(0, 4), random.randint(10,14)],
            [random.randint(5, 9), random.randint(10,14)],
            [random.randint(10, 14), random.randint(10,14)],
            [random.randint(15, 16), random.randint(10,14)],


        ]

        self.bomber1_sprite.center_x = CELL_W
        self.bomber1_sprite.center_y = CELL_H
        self.bomber2_sprite.center_x = SCREEN_WIDTH - CELL_W
        self.bomber2_sprite.center_y = SCREEN_HEIGHT - CELL_H

        self.bedroc_sprite = arcade.SpriteList()
        self.nebedroc_sprite = arcade.SpriteList()

        self.bomb1_sprite = arcade.SpriteList()
        self.bomb2_sprite = arcade.SpriteList()

        self.babax_sprite = arcade.SpriteList()

        self.bomb_sprite = arcade.SpriteList()
        self.flame_sprite = arcade.SpriteList()
        self.speed_sprite = arcade.SpriteList()

        self.speed = 5
        self.mousePres = False


        self.bomb_sound = arcade.load_sound("bombpl.mp3")

    def setup(self):
        for y in range(ROW):
            for x in range(COLUMN):
                block = Map('Blocks/SolidBlock.png')
                block.center_x = x * CELL_W + CELL_W / 2
                block.center_y = y * CELL_H + CELL_H / 2

                if random.random() < 0.3:
                    block = Block('Blocks/ExplodableBlock.png')
                    block.center_x = x * CELL_W + CELL_W / 2
                    block.center_y = y * CELL_H + CELL_H / 2
                    self.nebedroc_sprite.append(block)
                    if [x,y] in self.coords:
                        random_boost = random.randint(a = 1,b = 3)
                        if random_boost == 1:
                            boost = Boost('Powerups/BombPowerup.png')
                            boost.center_x = x * CELL_W + CELL_W / 2
                            boost.center_y = y * CELL_H + CELL_H / 2
                            self.bomb_sprite.append(boost)

                        if random_boost == 2:
                            boost = Boost('Powerups/FlamePowerup.png')
                            boost.center_x = x * CELL_W + CELL_W / 2
                            boost.center_y = y * CELL_H + CELL_H / 2
                            self.flame_sprite.append(boost)

                        if random_boost == 3:
                            boost = Boost('Powerups/SpeedPowerup.png')
                            boost.center_x = x * CELL_W + CELL_W / 2
                            boost.center_y = y * CELL_H + CELL_H / 2
                            self.speed_sprite.append(boost)


    def on_draw(self):
        self.clear()

        for y in range(ROW):
            for x in range(COLUMN):
                arcade.draw_texture_rectangle(x * CELL_W + CELL_W / 2, y * CELL_H + CELL_H / 2, CELL_W, CELL_H,
                                              texture=self.pole)
        self.nebedroc_sprite.draw()
        self.bedroc_sprite.draw()

        self.bomber1_sprite.draw()
        self.bomber2_sprite.draw()

        self.bomb1_sprite.draw()
        self.bomb2_sprite.draw()

        self.babax_sprite.draw()

        self.bomb_sprite.draw()
        self.flame_sprite.draw()
        self.speed_sprite.draw()

        arcade.draw_rectangle_outline(CELL_W * 5 / 2, CELL_H * 5 / 2, CELL_W * 5, CELL_H * 5, arcade.color.RED)
        arcade.draw_rectangle_outline(CELL_W * 15 / 2, CELL_H * 5 / 2, CELL_W * 5, CELL_H * 5, arcade.color.RED)
        arcade.draw_rectangle_outline(CELL_W * 25 / 2, CELL_H * 5 / 2, CELL_W * 5, CELL_H * 5, arcade.color.RED)


        arcade.draw_rectangle_outline(CELL_W * 5 / 2, CELL_H * 15 / 2, CELL_W * 5, CELL_H * 5, arcade.color.RED)
        arcade.draw_rectangle_outline(CELL_W * 5 / 2, CELL_H * 25 / 2, CELL_W * 5, CELL_H * 5, arcade.color.RED)


    def on_update(self, delta_time: float):
        self.bomber1_sprite.update()
        self.bomber2_sprite.update()

        self.bomb1_sprite.update()
        self.bomb2_sprite.update()

        self.babax_sprite.update()

        self.bomb_sprite.update()
        self.flame_sprite.update()
        self.speed_sprite.update()

        for flame in self.babax_sprite:
            for block in self.nebedroc_sprite:
                if arcade.check_for_collision(flame, block):
                    block.kill()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x // 60, y // 60)
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mousePres = True
            block = Map('Blocks/SolidBlock.png')
            block.center_x = x // 60 * CELL_W + CELL_W / 2
            block.center_y = y // 60 * CELL_H + CELL_H / 2
            self.bedroc_sprite.append(block)

        if button == arcade.MOUSE_BUTTON_RIGHT:
            center_x = x // 60 * CELL_W + CELL_W / 2
            center_y = y // 60 * CELL_H + CELL_H / 2

            for i in range(len(self.bedroc_sprite)):
                if self.bedroc_sprite[i].center_x == center_x and self.bedroc_sprite[i].center_y == center_y:
                    self.bedroc_sprite.remove(self.bedroc_sprite[i])

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.mousePres == True:
            block = Map('Blocks/SolidBlock.png')
            block.center_x = x // 60 * CELL_W + CELL_W / 2
            block.center_y = y // 60 * CELL_H + CELL_H / 2
            self.bedroc_sprite.append(block)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.mousePres = False

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W and self.bomber1_sprite.move == False:
            self.bomber1_sprite.change_y = 7
            self.bomber1_sprite.move = True
        elif symbol == arcade.key.S and self.bomber1_sprite.move == False:
            self.bomber1_sprite.change_y = -7
            self.bomber1_sprite.move = True
        elif symbol == arcade.key.A and self.bomber1_sprite.move == False:
            self.bomber1_sprite.change_x = -7
            self.bomber1_sprite.move = True
        elif symbol == arcade.key.D and self.bomber1_sprite.move == False:
            self.bomber1_sprite.change_x = 7
            self.bomber1_sprite.move = True

        elif symbol == arcade.key.UP and self.bomber2_sprite.move == False:
            self.bomber2_sprite.change_y = 7
            self.bomber2_sprite.move = True
        elif symbol == arcade.key.DOWN and self.bomber2_sprite.move == False:
            self.bomber2_sprite.change_y = -7
            self.bomber2_sprite.move = True
        elif symbol == arcade.key.LEFT and self.bomber2_sprite.move == False:
            self.bomber2_sprite.change_x = -7
            self.bomber2_sprite.move = True
        elif symbol == arcade.key.RIGHT and self.bomber2_sprite.move == False:
            self.bomber2_sprite.change_x = 7
            self.bomber2_sprite.move = True

        elif symbol == arcade.key.E:
            bomb = Bomb('Bomb/Bomb_f02.png')
            bomb.center_x = self.bomber1_sprite.center_x // 60 * CELL_W + CELL_W / 2
            bomb.center_y = self.bomber1_sprite.center_y // 60 * CELL_W + CELL_W / 2
            self.bomb1_sprite.append(bomb)

            arcade.play_sound(self.bomb_sound)

        elif symbol == arcade.key.RCTRL:
            bomb = Bomb('Bomb/Bomb_f02.png')
            bomb.center_x = self.bomber2_sprite.center_x // 60 * CELL_W + CELL_W / 2
            bomb.center_y = self.bomber2_sprite.center_y // 60 * CELL_W + CELL_W / 2
            self.bomb2_sprite.append(bomb)

            arcade.play_sound(self.bomb_sound)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.bomber1_sprite.move = False
            self.bomber1_sprite.change_y = 0
        elif symbol == arcade.key.S:
            self.bomber1_sprite.move = False
            self.bomber1_sprite.change_y = 0
        elif symbol == arcade.key.A:
            self.bomber1_sprite.move = False
            self.bomber1_sprite.change_x = 0
        elif symbol == arcade.key.D:
            self.bomber1_sprite.move = False
            self.bomber1_sprite.change_x = 0

        elif symbol == arcade.key.UP:
            self.bomber2_sprite.change_y = 0
            self.bomber2_sprite.move = False
        elif symbol == arcade.key.DOWN:
            self.bomber2_sprite.change_y = 0
            self.bomber2_sprite.move = False
        elif symbol == arcade.key.LEFT:
            self.bomber2_sprite.change_x = 0
            self.bomber2_sprite.move = False
        elif symbol == arcade.key.RIGHT:
            self.bomber2_sprite.change_x = 0
            self.bomber2_sprite.move = False


okno = MyGame(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
okno.setup()
arcade.run()


"""
Пофиксить проблему с бустами (спавн бустов)

Сделать так, что если коснулись бустов - они должны нам что-то менять (скорость, кол-во бомб и т.д.)

"""