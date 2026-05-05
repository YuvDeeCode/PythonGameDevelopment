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
    screen.draw.fill_rect(markbox,"blue")
    screen.draw.fill_rect(questionbox,"red")
    screen.draw.fill_rect(timerbox,"orange")
    screen.draw.fill_rect(skipbox,"green")
    for answerbox in answerboxes:
        screen.draw.fill_rect (answerbox,"yellow")
    markmessage = "Welcome to Quiz Master!"
    markmessage = markmessage + f"Q:{question_index} of {question_count}"
    screen.draw.textbox(markmessage,markbox,color = "white")
    

