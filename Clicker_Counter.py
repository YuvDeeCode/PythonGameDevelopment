import pgzrun,random
WIDTH=800
HEIGHT=600
TITLE="Clicker Counter Game"
clicks=0
mario=Actor("mario2",(50,50))
def draw():
    screen.clear()
    screen.fill((200,100,150))
    mario.draw()
    screen.draw.text("Clicks: "+ str(clicks),(200,10),fontsize=40)
def place_mario():
    mario.x= random.randint(50,WIDTH-50)
    mario.y= random.randint(50,HEIGHT-50)
def on_mouse_down():
    global clicks
    place_mario()
    clicks=clicks+1
    
pgzrun.go()