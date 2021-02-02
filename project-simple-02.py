#to jest komentarz
import pgzrun
WIDTH = 1280
HEIGHT = 720
PALETKA_WIDTH = 150
BALL_WIDTH = 48
STEP = 13
BALL_STEP_X = 10
BALL_STEP_Y = 12
'''
BRZEG_LEWY_A = ((WIDTH/2) - (PALETKA_WIDTH/2))
BRZEG_PRAWY_A = ((WIDTH/2) + (PALETKA_WIDTH/2))
BRZEG_LEWY_B = ((WIDTH/2) - (PALETKA_WIDTH/2))
BRZEG_PRAWY_B = ((WIDTH/2) + (PALETKA_WIDTH/2))
'''

list = ["pallettes/pallette.jpg", "pallettes/pallette_00.jpg", "pallettes/pallette_01.jpg",
        "pallettes/pallette_02.jpg", "pallettes/pallette_03.jpg", "pallettes/pallette_04.jpg",
        "pallettes/pallette_05.jpg", "pallettes/pallette_06.jpg",]

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
    def change_paletka(self):
        x = self.paletka.x
        y = self.paletka.y
        index = (list.index(self.paletka.image) + 1) % len(list)
        self.paletka.image = list[index]
        self.paletka.x = x
        self.paletka.y = y



paletka_a = Paletka(Actor(list[0]), ((WIDTH/2),20), "stop")
paletka_b = Paletka(Actor(list[0]), ((WIDTH/2),700), "stop")


class Ball:

    def __init__(self, ball, pozycja, direction, direction_y):
        self.ball = ball
        self.ball.x = pozycja[0]
        self.ball.y = pozycja[1]
        self.direction=direction
        self.direction_y=direction_y
        self.START = False
    def drawing(self):
        self.ball.draw()



    def bouncing_x (self):
        global BALL_STEP
        if (self.ball.x >= (WIDTH-(BALL_WIDTH/2))):
                self.direction = "left_ball"
                self.ball.x -= BALL_STEP_X


        if (self.ball.x <= (BALL_WIDTH/2)):
                self.direction = "right_ball"
                self.ball.x += BALL_STEP_X


        if (self.ball.x < (WIDTH-(BALL_WIDTH/2)) and self.ball.x > (BALL_WIDTH/2)):
            if (self.direction == "right_ball"):
                self.ball.x += BALL_STEP_X
            elif (self.direction == "left_ball"):
                self.ball.x -= BALL_STEP_X


    def bouncing_y (self, BRZEG_LEWY_A, BRZEG_PRAWY_A, BRZEG_LEWY_B, BRZEG_PRAWY_B):
        if (self.ball.y >= (HEIGHT-(BALL_WIDTH/2) - 28)):
            if ((self.ball.x >= BRZEG_LEWY_B) and (self.ball.x <= BRZEG_PRAWY_B)):
                self.direction_y = "down_ball"
                self.ball.y -= BALL_STEP_Y


        if (self.ball.y <= ((BALL_WIDTH/2) + 28)):
            if ((self.ball.x >= BRZEG_LEWY_A) and (self.ball.x <= BRZEG_PRAWY_A)):
                self.direction_y = "up_ball"
                self.ball.y += BALL_STEP_Y


        if (self.ball.y < (HEIGHT-(BALL_WIDTH/2)) and self.ball.y > (BALL_WIDTH/2)):
            if (self.direction_y == "up_ball"):
                self.ball.y += BALL_STEP_Y
            elif (self.direction_y == "down_ball"):
                self.ball.y -= BALL_STEP_Y



ball = Ball (Actor("ball.png"), ((WIDTH/2), (HEIGHT/2)), "right_ball", "up_ball")
def on_key_down(key):
    if (key == keys.RIGHT):
        paletka_a.set_direction("right")
    elif (key == keys.LEFT):
        paletka_a.set_direction("left")

    if (key == keys.D):
        paletka_b.set_direction("right")
    elif (key == keys.A):
        paletka_b.set_direction("left")

    if (key == keys.P):
        paletka_a.change_paletka()


    if (key == keys.O):
        paletka_b.change_paletka()

def on_key_up(key):
    if (key == keys.RIGHT):
        paletka_a.stop("right")
    elif(key == keys.LEFT):
        paletka_a.stop("left")

    if (key == keys.D):
        paletka_b.stop("right")
    elif(key == keys.A):
        paletka_b.stop("left")

    if (key == keys.SPACE):
        ball.START = True

def update():
    if (paletka_a.direction == "right"):
        paletka_a.right()
    elif (paletka_a.direction == "left"):
        paletka_a.left()

    if (paletka_b.direction == "right"):
        paletka_b.right()
    elif (paletka_b.direction == "left"):
        paletka_b.left()

    if (ball.START == True):
        ball.bouncing_x()
        BRZEG_LEWY_A = (paletka_a.paletka.x - (PALETKA_WIDTH/2))
        BRZEG_PRAWY_A = (paletka_a.paletka.x + (PALETKA_WIDTH/2))

        BRZEG_LEWY_B = (paletka_b.paletka.x - (PALETKA_WIDTH/2))
        BRZEG_PRAWY_B = (paletka_b.paletka.x + (PALETKA_WIDTH/2))
        ball.bouncing_y(BRZEG_LEWY_A, BRZEG_PRAWY_A, BRZEG_LEWY_B, BRZEG_PRAWY_B)



def draw():
    screen.blit("background.jpeg", (0,0))
    paletka_a.drawing()
    paletka_b.drawing()
    ball.drawing()
pgzrun.go()
