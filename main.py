import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



# creer la classe de balle
class balle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rayon = random.randint(10,30)
        self.change_x = 5
        self.change_y = 5
        self.color = (255,0,0)
    def update(self):

        self.x += self.change_x
        self.y += self.change_y

        # si la balle est au extremite de l'ecran, la balle passe d'un cote a l'autre
        if self.x < self.rayon:
            self.change_x *= -1
        if self.x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.y < self.rayon:
            self.change_y *= -1
        if self.y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1

# mettre des balles sur l'ecran
    def draw(self):
        #arcade.start_render()

        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


# creer la classe de rectangle
class rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = random.randint(10,30)
        self.height = random.randint(10,30)
        self.change_x = 5
        self.change_y = 5
        self.color = (255,0,0)
    def update(self):

        self.x += self.change_x
        self.y += self.change_y
        # si le rectangle est au extremite de l'ecran, la balle passe d'un cote a l'autre
        if self.x < self.width:
            self.change_x *= -1
        if self.x > SCREEN_WIDTH - self.width:
            self.change_x *= -1
        if self.y < self.height:
            self.change_y *= -1
        if self.y > SCREEN_HEIGHT - self.height:
            self.change_y *= -1

    # mettre des rectangles sur l'ecran
    def draw(self):
        #arcade.start_render()

        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)


COLORS = []

# creer la classe de mygame pour faire fonctionner le jeu
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.rectangle = []
        self.balle = []

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.balle.append(balle(x,y))
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.rectangle.append(rectangle(x,y))

    def on_draw(self):
        arcade.start_render()
        for i in self.rectangle:
            i.draw()
        for i in self.balle:
            i.draw()

    def on_update(self, delta_time: float):
        for i in self.rectangle:
            i.update()
        for i in self.balle:
            i.update()



# effectuer le programme
def main():
    my_game = MyGame()

    arcade.run()


main()