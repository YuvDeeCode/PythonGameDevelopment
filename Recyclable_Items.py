import pgzrun, random
WIDTH=600
HEIGHT=400
TITLE = "Recyclable_Items"
bin = Actor("bin")
waste_types = ["paper","battery","waterbottle","lightbulb"]
item = Actor(random.choice(waste_types))
item.pos = random.randint(50,500),10
bin.pos = 350,300
score = 0
def draw():
    screen.clear()
    screen.fill((23,123,255))
    item.draw()
    bin.draw()
    screen.draw.text("Score: "+str(score),(20,20))
pgzrun.go()
