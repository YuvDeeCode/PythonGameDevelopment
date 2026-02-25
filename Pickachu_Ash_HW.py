import pgzrun, random
WIDTH = 800
HEIGHT = 600
TITLE = "Pickachu and Ash Game"
score = 0
game_over = False
ash=Actor("pokemonchar")
pikachu=Actor("pikachu")
ash.pos = (234,563)
pikachu.pos = (345,23)
def draw():
    global score
    screen.clear()
    screen.blit("pokemonbackground2",(0,0))
    ash.draw()
    pikachu.draw()
    screen.draw.text("Score: "+str(score),(400,10),fontsize=40)
    if game_over==True:
        screen.fill((255,0,0))
        screen.draw.text("Time's up!\nScore: "+str(score))

def placing_pikachu():
    pikachu.x=random.randint(50,WIDTH-50)
    pikachu.y=random.randint(50,HEIGHT-50)

def time_up():
    global game_over
    game_over=True

def update():
    global score
    if keyboard.left:
        ash.x=ash.x-2
    if keyboard.right:
        ash.x=ash.x+2
    if keyboard.up:
        ash.y=ash.y-2
    if keyboard.down:
        ash.y=ash.y+2
    pikachu_caught = ash.colliderect(pikachu)
    if pikachu_caught==True:
        score=score+10
        placing_pikachu()

clock.schedule(time_up,60.0)

pgzrun.go()