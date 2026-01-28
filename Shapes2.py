import pgzrun
WIDTH=800
HEIGHT=600
def draw():
    screen.clear()
    x=1
    for i in range(50):
        rect=Rect((20,20),(30+x,30+x))
        screen.draw.rect(rect,"blue")
        x=x+10
pgzrun.go()
