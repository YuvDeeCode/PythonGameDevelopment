import pgzrun
WIDTH = 900
HEIGHT = 700
TITLE = "Quiz"

markbox = Rect(0,0,800,80)
questionbox = Rect(0,0,650,150)
timerbox = Rect(0,0,150,150)
answerbox1 = Rect(0,0,300,150)
answerbox2 = Rect(0,0,300,150)
answerbox3 = Rect(0,0,300,150)
answerbox4 = Rect(0,0,300,150)
skipbox = Rect(0,0,300,150)
score=0
timeleft=10
questionsfile = "Questions.txt"
markmessage = ""
game_over = False
answerboxes = [answerbox1,answerbox2,answerbox3,answerbox4]
questions = []
question = []
question_count = 0
question_index = 0
markbox.move_ip(0,0)
questionbox.move_ip(20,100)
timerbox.move_ip(700,100)
answerbox1.move_ip(20,270)
answerbox2.move_ip(370,270)
answerbox3.move_ip(20,450)
answerbox4.move_ip(370,450)
skipbox.move_ip(700,270)

def draw():
    global markmessage
    screen.clear()
    screen.fill((100,100,100))
    screen.draw.filled_rect(markbox,"blue")
    screen.draw.filled_rect(questionbox,"red")
    screen.draw.filled_rect(timerbox,"orange")
    screen.draw.filled_rect(skipbox,"green")
    for answerbox in answerboxes:
        screen.draw.filled_rect (answerbox,"black")
    markmessage = "Welcome to Quiz Master!"
    markmessage = markmessage + f"Q:{question_index} of {question_count}"
    screen.draw.text(markmessage,(20,20),color = "white",fontsize=30)
    screen.draw.text(str(timeleft),(740,140),color = "white",fontsize =30)
    screen.draw.text("Skip",(740,400),color="white",fontsize=30)
    if question:
        screen.draw.text(question[0],(40,130),color="white",fontsize=30)
        screen.draw.text(question[1],(50,320),color="white",fontsize=30)
        screen.draw.text(question[2],(400,320),color="white",fontsize=30)
        screen.draw.text(question[3],(50,500),color="white",fontsize=30)
        screen.draw.text(question[4],(400,500),color="white",fontsize=30)
#
def move_mark():
    markbox.x=markbox.x-2
    if markbox.right<0:
        markbox.left=WIDTH
def update():
    move_mark()
def read_question_file():
    global question_count
    global questions 
    with open(questionsfile,"r") as file:
        for i in file:
            questions.append(i.strip())
        question_count = len(questions)
def read_next_question():
    global question_index
    question_index = question_index+1
    if questions:
        return questions.pop(0).split(",")
    return None
def on_mouse_down(pos):
    index = 1
    for box in answerboxes:
        if box.collidepoint(pos):
            if index == int(question[5]):
                correct_answer()
            else:
                game_over()
        index=index+1
        if skipbox.collidepoint(pos):
            skip_question()
def correct_answer():
    global score
    global question
    global timeleft
    global questions
    score = score+1
    if questions:
        question = read_next_question()
        timeleft=10
    else:
        gameover()
def gameover():
    global question
    global game_over
    global timeleft
    message = f"Game Over. You got {score} questions correct!"
    question = [message,"-","-","-","-",5]
    timeleft = 0
    game_over = True
def skip_question():
    global question
    global timeleft
    if questions and not game_over:
        question = read_next_question()
        timeleft = 10
    else:
        gameover()
def update_timeleft():
    global timeleft
    if timeleft:
        timeleft = timeleft - 1
    else:
        gameover()

read_question_file()
question = read_next_question()
clock.schedule_interval(update_timeleft,1)
pgzrun.go()
    
    

