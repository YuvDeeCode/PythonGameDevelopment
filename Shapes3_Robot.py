import pgzrun
WIDTH=800
HEIGHT=600
def draw():
    screen.clear()
    rect=Rect((120,120),(345,270))
    screen.draw.rect(rect,"purple")
    screen.draw.circle((195,190),40,"blue")
    screen.draw.circle((390,190),40,"blue")
    screen.draw.line((195,300),(390,300),"blue")
pgzrun.go()