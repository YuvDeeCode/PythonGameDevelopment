import pgzrun, random
WIDTH=800
HEIGHT=600
TITLE="Alien Game"
score=0
message="Hello World"
alien=Actor("alien")
#alien.pos=(200,200)
def draw():
    screen.clear()
    screen.fill((100,100,100))
    alien.draw()
    screen.draw.text(message,(400,10),fontsize=40)
    screen.draw.text("Score: "+ str(score),(200,10),fontsize=40)
def place_alien():
    alien.x= random.randint(50,WIDTH-50)
    alien.y= random.randint(50,HEIGHT-50)
def on_mouse_down(pos):
    global message
    global score
    if alien.collidepoint(pos):
        message="Good Shot!"
        score=score+1
        place_alien()
    else:
        message="You missed."
        score=score-1

place_alien()    
pgzrun.go()