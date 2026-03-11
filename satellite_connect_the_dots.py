import pgzrun, random, time
WIDTH=800
HEIGHT=600
TITLE = "Satellite Game"
satellites = []
lines = []
next_satellite = 0
start_time = 0
end_time = 0
total_time = 0
satellite_numbers = 8
def create_satellites():
    global start_time
    for i in range(satellite_numbers):
        satellite = Actor("satellite")
        satellite.pos=(random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40))
        satellites.append(satellite)
    start_time = time.time()
    
def draw():
    global total_time
    screen.clear()
    screen.blit("satellite_background",(0,0))
    number = 1
    for satellite in satellites:
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20))
        satellite.draw()
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    if next_satellite < satellite_numbers:
        end_time = time.time()
        total_time = end_time - start_time
        screen.draw.text(str(total_time),(30,30), fontsize = 40)
    else:
        screen.draw.text(str(total_time),(30,30), fontsize = 40)
