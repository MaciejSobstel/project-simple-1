#to jest komentarz
import pgzrun
import random
import time
WIDTH = 1280
HEIGHT = 720
PALETKA_WIDTH = 200
BALL_WIDTH = 48
STEP = 12



class Paletka:

    def __init__(self, paletka, pozycja, direction):
        self.paletka = paletka
        self.paletka.x = pozycja[0]
        self.paletka.y = pozycja[1]
        self.direction = direction
        self.list = ["pallettes/pallette.jpg", "pallettes/pallette_00.jpg", "pallettes/pallette_01.jpg",
                "pallettes/pallette_02.jpg", "pallettes/pallette_03.jpg", "pallettes/pallette_04.jpg",
                "pallettes/pallette_05.jpg", "pallettes/pallette_06.jpg",]
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
        index = (self.list.index(self.paletka.image) + 1) % len(self.list)
        self.paletka.image = self.list[index]
        self.paletka.x = x
        self.paletka.y = y



paletka_a = Paletka(Actor("pallettes/pallette.jpg"), ((WIDTH/2),20), "stop")
paletka_b = Paletka(Actor("pallettes/pallette.jpg"), ((WIDTH/2),700), "stop")


class Ball:

    def __init__(self, ball, pozycja, direction, direction_y):
        self.BALL_STEP_X = 0
        self.BALL_STEP_Y = 6
        self.MIN_STEP_X = 1
        self.MAX_STEP_X = 8
        self.MIN_STEP_Y = 3
        self.MAX_STEP_Y = 10
        self.ball = ball
        self.ball.x = pozycja[0]
        self.ball.y = pozycja[1]
        self.direction=direction
        self.direction_y=direction_y
        self.START = False
        self.ball_list =["ball/ball_0.png", "ball/ball_1.png", "ball/ball_2.png", "ball/ball_3.png", "ball/ball_4.png", "ball/ball_5.png", "ball/ball_6.png", "ball/ball_7.png"]
        self.roll_speed = 0
        random.seed()
    def drawing(self):
        self.ball.draw()

    def ball_spin(self):
        self.roll_speed += 1
        if (self.roll_speed == 5):
            index = (self.ball_list.index(self.ball.image) + 1) % len(self.ball_list)
            self.ball.image = self.ball_list[index]
            self.roll_speed = 0

    def bouncing_x (self):
        global BALL_STEP
        if (self.ball.x >= (WIDTH-(BALL_WIDTH/2))):
                self.direction = "left_ball"
                self.ball.x -= self.BALL_STEP_X


        if (self.ball.x <= (BALL_WIDTH/2)):
                self.direction = "right_ball"
                self.ball.x += self.BALL_STEP_X


        if (self.ball.x < (WIDTH-(BALL_WIDTH/2)) and self.ball.x > (BALL_WIDTH/2)):
            if (self.direction == "right_ball"):
                self.ball.x += self.BALL_STEP_X
            elif (self.direction == "left_ball"):
                self.ball.x -= self.BALL_STEP_X


    def bouncing_y (self, paletka_a, paletka_b, point_a, point_b):
        BRZEG_LEWY_A = (paletka_a.paletka.x - (PALETKA_WIDTH/2) - STEP)
        BRZEG_PRAWY_A = (paletka_a.paletka.x + (PALETKA_WIDTH/2) + STEP)

        BRZEG_LEWY_B = (paletka_b.paletka.x - (PALETKA_WIDTH/2) - STEP)
        BRZEG_PRAWY_B = (paletka_b.paletka.x + (PALETKA_WIDTH/2) + STEP)


        if (self.ball.y >= (HEIGHT-(BALL_WIDTH/2) - 28)):
            if ((self.ball.x >= BRZEG_LEWY_B) and (self.ball.x <= BRZEG_PRAWY_B)):
                self.direction_y = "down_ball"
                self.BALL_STEP_X = random.randrange(self.MIN_STEP_X, self.MAX_STEP_X + 1, 1)
                self.BALL_STEP_Y = random.randrange(self.MIN_STEP_Y, self.MAX_STEP_Y + 1, 1)
                self.ball.y -= self.BALL_STEP_Y
                if __debug__:
                    print("piłka: ", self.ball.x, self.ball.y, "      paletka: ", paletka_a.paletka.x, paletka_b.paletka.x, "     predkosci: ",  self.BALL_STEP_X, self.BALL_STEP_Y,  )
            else:
                if __debug__:
                    print("piłka: ", self.ball.x, self.ball.y, "      paletka: ", paletka_a.paletka.x, paletka_b.paletka.x, "     predkosci: ",  self.BALL_STEP_X, self.BALL_STEP_Y,  )
                self.ball.x = (WIDTH/2)
                self.ball.y = (HEIGHT/2)
                self.START = False
                self.BALL_STEP_X = 0
                self.BALL_STEP_Y = 6
                point_b.change_point()

        if (self.ball.y <= ((BALL_WIDTH/2) + 28)):
            if ((self.ball.x >= BRZEG_LEWY_A) and (self.ball.x <= BRZEG_PRAWY_A)):
                self.direction_y = "up_ball"
                self.BALL_STEP_X = random.randrange(self.MIN_STEP_X, self.MAX_STEP_X + 1, 1)
                self.BALL_STEP_Y = random.randrange(self.MIN_STEP_Y, self.MAX_STEP_Y + 1, 1)
                self.ball.y += self.BALL_STEP_Y
                if __debug__:
                    print("piłka: ", self.ball.x, self.ball.y, "      paletka: ", paletka_a.paletka.x, paletka_b.paletka.x, "     predkosci: ",  self.BALL_STEP_X, self.BALL_STEP_Y,  )
            else:
                if __debug__:
                    print("piłka: ", self.ball.x, self.ball.y, "      paletka: ", paletka_a.paletka.x, paletka_b.paletka.x, "     predkosci: ",  self.BALL_STEP_X, self.BALL_STEP_Y,  )
                self.ball.x = (WIDTH/2)
                self.ball.y = (HEIGHT/2)
                self.START = False
                self.BALL_STEP_X = 0
                self.BALL_STEP_Y = 6
                point_a.change_point()

        if (self.ball.y < (HEIGHT-(BALL_WIDTH/2)) and self.ball.y > (BALL_WIDTH/2)):
            if (self.direction_y == "up_ball"):
                self.ball.y += self.BALL_STEP_Y
            elif (self.direction_y == "down_ball"):
                self.ball.y -= self.BALL_STEP_Y



ball = Ball (Actor("ball/ball_0.png"), ((WIDTH/2), (HEIGHT/2)), "right_ball", "up_ball")

class Points:
    def __init__(self, point, point10, pozycja, value):
        self.point = point
        self.point.x = pozycja[0]
        self.point.y = pozycja[1]
        self.point10 = point10
        self.point10.x = pozycja[0] - 200
        self.point10.y = pozycja[1]
        self.value = value
        self.point_list = ["numbers/0.png", "numbers/1.png", "numbers/2.png", "numbers/3.png", "numbers/4.png", "numbers/5.png", "numbers/6.png", "numbers/7.png", "numbers/8.png", "numbers/9.png"]
    def drawing(self):
        self.point.draw()
        self.point10.draw()
    def change_point(self):
        self.value += 1
        self.point.image = self.point_list[self.value % 10]
        self.point10.image = self.point_list[int(self.value / 10)]


point_a = Points(Actor("numbers/0.png"), Actor("numbers/0.png"), ((WIDTH/2), (HEIGHT/2)+200), 0)
point_b = Points(Actor("numbers/0.png"), Actor("numbers/0.png"), ((WIDTH/2), (HEIGHT/2)-200), 0)
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
        ball.bouncing_y(paletka_a, paletka_b, point_a, point_b)
        ball.ball_spin()

def draw():
    screen.blit("background.jpeg", (0,0))
    point_a.drawing()
    point_b.drawing()
    paletka_a.drawing()
    paletka_b.drawing()
    ball.drawing()

pgzrun.go()
