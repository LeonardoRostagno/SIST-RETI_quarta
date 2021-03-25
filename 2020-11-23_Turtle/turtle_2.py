import turtle 

robot = turtle.Turtle()
window = turtle.Screen()

robot.home()

print(f"Altezza -> {window.window_height()}")
print(f"Larghezza -> {window.window_width()}")

lung = 10

def controllo():
    ris = 0

    # controllo dei lati
    if (robot.ycor() + lung) > window.window_height() / 2:
        ris = 1

    elif (robot.ycor() - lung) < -1 * window.window_height() / 2: 
        ris = 2

    elif (robot.xcor() + lung) > window.window_width() / 2:
        ris = 3 

    elif (robot.xcor() - lung) < -1 * window.window_width() / 2:
        ris = 4
    
    # controllo angoli 
    if (robot.ycor() + lung) > window.window_height() / 2 and  (robot.xcor() - lung) < -1 * window.window_width() / 2:          #alto a sinistra 
        ris = 5

    if (robot.ycor() + lung) > window.window_height() / 2 and  (robot.xcor() + lung) > window.window_width() / 2:               #alto a destra
        ris = 6

    if (robot.ycor() - lung) < -1 * window.window_height() / 2 and (robot.xcor() + lung) > window.window_width() / 2:           #basso a destra 
        ris = 7
        
    if (robot.ycor() - lung) < -1 * window.window_height() / 2 and (robot.xcor() - lung) < -1 * window.window_width() / 2:      #basso a sinistra 
        ri = 8

    return ris 

def up():
    if controllo() != 1 and controllo() != 5 and controllo() != 6 :
        robot.forward(lung)
        print("Up")
    else :
        pass

def down():
    if controllo() != 2 and controllo() != 7 and controllo() != 8 :
        robot.back(lung)
        print("Down")
    else:
        pass

def right ():
    if controllo() != 3 and controllo() != 6 and controllo() != 7 :
        robot.right(90)
        print("Right")
    else :
        pass

def left ():
    if controllo() != 4 and controllo() != 5 and controllo() != 8 :
        robot.left(90)
        print("Left")
    else :
        pass

window.title("Turtle_2 game")
window.bgcolor("white")
window.setup(width= 768, height= 648)

window.listen()
window.onkey(up, "w")
window.onkey(left, "a")
window.onkey(down, "s")
window.onkey(right, "d")

window.mainloop()
