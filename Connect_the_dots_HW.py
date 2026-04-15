import pgzrun, random,time
WIDTH=800
HEIGHT=600
TITLE = "Make the shape"
dots = []
lines = []
next_dot = 0 
start_time = 0
end_time = 0 
total_time = 0

def create_dots():
    global start_time
    global dot_numbers
    dot_numbers = int(input("Pick a shape: Triangle, Rectangle or Pentagon(type 1,2 and 3 correspondingly i.e. triangle(you type 1)?"))
    if dot_numbers == 1:
            dot1 = Actor("satellite")
            dot1.pos=(240,200)
            dots.append(dot1)
            dot2 = Actor("satellite")
            dot2.pos=(340,200)
            dots.append(dot2)
            dot3 = Actor("satellite")
            dot3.pos=(290,300)
            dots.append(dot3)
    if dot_numbers == 2:
            dot1 = Actor("satellite")
            dot1.pos=(240,200)
            dots.append(dot1)
            dot2 = Actor("satellite")
            dot2.pos=(340,200)
            dots.append(dot2)
            dot3 = Actor("satellite")
            dot3.pos=(340,300)
            dots.append(dot3)
            dot4 = Actor("satellite")
            dot4.pos=(240,300)
            dots.append(dot4)
    if dot_numbers == 3:
            dot1 = Actor("satellite")
            dot1.pos=(240,200)
            dots.append(dot1)
            dot2 = Actor("satellite")
            dot2.pos=(340,200)
            dots.append(dot2)
            dot3 = Actor("satellite")
            dot3.pos=(340,300)
            dots.append(dot3)
            dot4 = Actor("satellite")
            dot4.pos=(290,400)
            dots.append(dot4)
            dot5 = Actor("satellite")
            dot5.pos=(240,300)
            dots.append(dot5)
    start_time = time.time()

def draw():
    global total_time
    screen.clear()
    screen.blit("satellite_background",(0,0))
    number=1
    for dot in dots:
        screen.draw.text(str(number),(dot.pos[0],dot.pos[1]+20))
        dot.draw()
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    if next_dot < dot_numbers:
        end_time = time.time()
        total_time = end_time - start_time
        screen.draw.text(str(round(total_time,2)),(30,30), fontsize = 40)
    else:
        screen.draw.text(str(round(total_time,2)),(30,30), fontsize = 40)

def on_mouse_down(pos):
    global next_dot
    global lines
    if next_dot < dot_numbers+2:
        if dots[next_dot].collidepoint(pos):
            if next_dot:
                lines.append((dots[next_dot-1].pos,dots[next_dot].pos))
            next_dot = next_dot+1
    else:
        lines=[]
        next_dot = 0
create_dots()
pgzrun.go()