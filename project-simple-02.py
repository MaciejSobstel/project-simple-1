#to jest komentarz
import pgzrun

class Paletka:

    def __init__(self, paletka, pozycja):
        self.paletka = paletka
        self.paletka.x = pozycja[0]
        self.paletka.y = pozycja[1]
    def drawning(self):
        self.paletka.draw()
WIDTH = 1280
HEIGHT = 720

paletka_a = Paletka(Actor("pallette.jpg"), (100,20))
paletka_b = Paletka(Actor("pallette.jpg"), (100,700))

def draw():
    screen.blit("background.jpeg", (0,0))
    paletka_a.drawning()
    paletka_b.drawning()
pgzrun.go()
