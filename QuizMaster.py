import pgzrun

WIDTH = 500
HEIGHT = 350

# Rectangle definitions
question_box = Rect((20, 60), (370, 75))

answer_box1 = Rect((20, 140), (170, 75))
answer_box2 = Rect((215, 140), (170, 75))
answer_box3 = Rect((20, 230), (170, 75))
answer_box4 = Rect((215, 230), (170, 75))

score_box = Rect((415, 60), (70, 75))
skip_box = Rect((415, 140), (70, 165))

def draw():
    screen.clear()
    screen.fill("black")

    # Title
    screen.draw.text("Welcome To Quiz Master...",(10, 15),color="white",fontsize=36)

    # Question box
    screen.draw.filled_rect(question_box, "darkblue")
    screen.draw.text( "Game over!\nYou got 2 questions correct!",center=question_box.center,color="white",fontsize=24)

    # Answer boxes
    for box in [answer_box1, answer_box2, answer_box3, answer_box4]:
        screen.draw.filled_rect(box, "orange")
        screen.draw.text("-",center=box.center,color="black",fontsize=50)

    # Score box
    screen.draw.filled_rect(score_box, "yellow")
    screen.draw.text("0",center=score_box.center,color="lightgray",fontsize=60)

    # Skip box
    screen.draw.filled_rect(skip_box, "green")
    screen.draw.text("Skip",center=skip_box.center,color="black",fontsize=40,angle=90)

pgzrun.go()