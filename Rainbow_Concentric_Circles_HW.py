import pgzrun
import random
WIDTH = 800
HEIGHT = 600
def draw():
    screen.clear()
    x=20
    for i in range (9):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        screen.draw.circle((350,250),x,(r,g,b))
        x=x+20
pgzrun.go()
