import pgzrun, random, time
WIDTH=800
HEIGHT=600
TITLE = "Connect The Stars Game"
stars = []
lines = []
next_star = 0
start_time = 0
end_time = 0
total_time = 0
star_numbers = 8
def create_stars():
    global start_time
    for i in range(star_numbers):
        star = Actor("star2-removebg-preview")
        star.pos=(random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40))
        stars.append(star)
    start_time = time.time()
    
def draw():
    global total_time
    screen.clear()
    screen.blit("satellite_background",(0,0))
    number = 1
    for star in stars:
        screen.draw.text(str(number),(star.pos[0],star.pos[1]+40))
        star.draw()
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    if next_star < star_numbers:
        end_time = time.time()
        total_time = end_time - start_time
        screen.draw.text(str(round(total_time,2)),(30,30), fontsize = 40)
    else:
        screen.draw.text(str(round(total_time,2)),(30,30), fontsize = 40)

def on_mouse_down(pos):
    global next_star
    global lines
    if next_star < star_numbers:
        if stars[next_star].collidepoint(pos):
            if next_star:
                lines.append((stars[next_star-1].pos,stars[next_star].pos))
            next_star = next_star + 1
    else:
        lines = []
        next_star = 0
    
create_stars()
pgzrun.go()