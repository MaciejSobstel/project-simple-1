#to jest komentarz
import pgzrun

WIDTH = 1280
HEIGHT = 720
PALETKA_WIDTH = 150
STEP = 10
class Paletka:

    def __init__(self, paletka, pozycja, direction):
        self.paletka = paletka
        self.paletka.x = pozycja[0]
        self.paletka.y = pozycja[1]
        self.direction = direction
    def drawing(self):
        self.paletka.draw()
    def left(self):
        if (self.paletka.x > (PALETKA_WIDTH/2)):
            self.paletka.x -= STEP
    def right(self):
        if (self.paletka.x < (WIDTH - (PALETKA_WIDTH/2))):
            self.paletka.x += STEP
    def set_direction(self, direction):
        self.direction = direction
    def stop (self, direction):
        if (self.direction == direction):
            self.direction ="stop"

paletka_a = Paletka(Actor("pallette.jpg"), (360,20), "stop")
paletka_b = Paletka(Actor("pallette.jpg"), (360,700), "stop")

def on_key_down(key):
    if (key == keys.RIGHT):
        paletka_a.set_direction("right")
    elif (key == keys.LEFT):
        paletka_a.set_direction("left")

    if (key == keys.D):
        paletka_b.set_direction("right")
    elif (key == keys.A):
        paletka_b.set_direction("left")

def on_key_up(key):
    if (key == keys.RIGHT):
        paletka_a.stop("right")
    elif(key == keys.LEFT):
        paletka_a.stop("left")

    if (key == keys.D):
        paletka_b.stop("right")
    elif(key == keys.A):
        paletka_b.stop("left")

def update():
    if (paletka_a.direction == "right"):
        paletka_a.right()
    elif (paletka_a.direction == "left"):
        paletka_a.left()

    if (paletka_b.direction == "right"):
        paletka_b.right()
    elif (paletka_b.direction == "left"):
        paletka_b.left()



def draw():
    screen.blit("background.jpeg", (0,0))
    paletka_a.drawing()
    paletka_b.drawing()
pgzrun.go()
