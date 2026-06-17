import pgzrun, random
WIDTH = 900
HEIGHT = 700
TITLE = " "#

numberbox = Rect(0,0,200,200)
answerbox1 = Rect(0,0,300,150)
answerbox2 = Rect(0,0,300,150)
answerbox3 = Rect(0,0,300,150)
questionbox = Rect(0,0,650,150)
#messagebox = ()
game_over = False
number = 0
var = 0
answerboxes = [answerbox1,answerbox2,answerbox3]
answerbox1.move_ip(20,270)
answerbox2.move_ip(370,270)
answerbox3.move_ip(20,450)
questionbox.move_ip(20,100)
question1 = "Would you like to start, or would you like to the computer to start?"
question2 = "How many numbers would you like to enter?"
questions = [question1,question2]
def draw():
    global number
    screen.clear()
    screen.fill((100,100,100))
    screen.draw.filled_rect(questionbox,"red")
    for answerbox in answerboxes:
        screen.draw.filled_rect(answerbox,"black")
    screen.draw.text(questions[0],(40,130),color = "white",fontsize = 30)
    screen.draw.text("Yes",(50,320),color = "white",fontsize = 30)
    screen.draw.text("No",(400,320),color = "white",fontsize = 30)
#How to include logic in draw function.
#while game_over == False:
def player_start():
    screen.draw.text(questions[1],(40,130),color = "white",fontsize = 30)
    screen.draw.text("1",(50,320),color = "white",fontsize = 30)
    screen.draw.text("2",(400,320),color = "white",fontsize = 30)
    screen.draw.text("3",(50,500),color="white",fontsize = 30)
    for box in answerboxes:
        if box.collidepoint(pos):
            if answerboxes[0]:
                number+=1
                screen.draw.text(str(number),(100,100),color = "white",fontsize = 30)
            elif answerboxes[1]:
                number+=2
                screen.draw.text(str(number),(100,100),color = "white",fontsize = 30)
            elif answerboxes[2]:
                number+=3
                screen.draw.text(str(number),(100,100),color = "white",fontsize = 30)
def computer_start():
    number+=random.randint(1,3)
    screen.draw.text(str(number),(100,100),color = "white",fontsize = 30)
def on_mouse_down(pos):
    global number
    global var
    for box in answerboxes:
        if box.collidepoint(pos):
            if answerboxes[0]:
                player_start()
                var = 1
            elif answerboxes[1]:
                computer_start()
                var = 2
def check(number):
    if number<21:
        game_over = False
    else:
        game_over = True

    while game_over == False:
        if var == 1:
            player_start()
            computer_start()
        elif var == 2:
            computer_start()
            player_start()
    print("Game Over!")
#How do you know who won?
#Indentation
pgzrun.go()

    