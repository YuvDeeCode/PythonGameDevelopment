import pgzrun
WIDTH=800
HEIGHT=600
def draw():
    screen.clear() #Optional
    screen.draw.line((0,0),(800,600),"blue")
    screen.draw.circle((410,310),50,"orange")
    screen.draw.filled_circle((200,200),50,"green")
    rect=Rect((20,20),(500,300))
    screen.draw.rect(rect,"yellow")
    screen.draw.filled_rect(rect,"red")
pgzrun.go()

