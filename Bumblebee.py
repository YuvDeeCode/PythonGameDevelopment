import pgzrun,random
WIDTH = 800
HEIGHT = 600
TITLE = "Bumblebee Game"
score=0
game_over=False
bee=Actor("bee")
flower=Actor("flower")
flower.pos=(385,593)
bee.pos=(285,408)
def draw():
    screen.clear()
    screen.blit("background",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score: "+str(score),(400,10),fontsize=40)
    if game_over==True:
        screen.fill((255,0,0))
        screen.draw.text("Time's up! Your score was "+str(score),(200,200),fontsize=40)

def placing_flower():
    flower.x=random.randint(50,WIDTH-50)
    flower.y=random.randint(50,HEIGHT-50)

def time_up():
    global game_over
    game_over=True

def update():
    global score
    if keyboard.left:
        bee.x=bee.x -2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
        bee.y=bee.y+2
    flower_collected = bee.colliderect(flower)
    if flower_collected==True:
        score=score+10
        placing_flower()

clock.schedule(time_up,60.0)
pgzrun.go()
    