"""
Implementare il videogioco snake tramite il modulo turtle.
"""

import turtle
import time
import random

delay = 0.1

# variabili dei punteggi
punt = 0
punt_best = 0

# impostazioni della finestra
win = turtle.Screen()

win.title("Snake") # titolo
win.bgcolor('cadetblue') # colore del campo di gioco
win.setup(width = 600, height = 600) # dimensioni campo
win.tracer(0) # abilita i ritardi delle varie animazioni

#impostazioni della testa dello snake 
head = turtle.Turtle()

head.shape("square") # forma della testa dello snake
head.color("black") # colore dello snake 
head.speed(0) # velocità dello snake
head.penup() # alza la penna 
head.goto(0, 0) # sposta la testa in un punto assoluto
head.direction = "stop" 

# impostazioni del cibo
food= turtle.Turtle()

food.shape("circle") # forma del cibo
food.color("firebrick") # colore del cibo
food.speed(0) # velocità del cibo
food.penup() # alza la penna
food.goto(0, 100) # sposta il cib in un punto assoluto

segments = []

# impostazioni dei punteggi 
sc = turtle.Turtle() 

sc.speed(0) # velocità dei punteggi
sc.shape("square") # forma dello spazio per i punteggi
sc.color("black") # colore delle scritte
sc.penup() # alza la penna
sc.hideturtle() #rende invisibile 
sc.goto(0, 260) #posizione assoluta dei punteggi
sc.write("Punteggio : 0  The Best : 0", align = "center", font=("Magneto", 20, "normal"))

# funzioni per il movimento
def go_up(): # funzione su
    if head.direction != "down":
        head.direction = "up"

def go_down(): # funzione giù
    if head.direction != "up":
        head.direction = "down"

def go_left(): # funzione sinistra
    if head.direction != "right":
        head.direction = "left"

def go_right(): # funzione destra
    if head.direction != "left":
        head.direction = "right"

def move(): # funzione per il movimento dello snake
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_left, "a")
win.onkeypress(go_down, "s")
win.onkeypress(go_right, "d")

# è una sorta di main
while True:
    win.update() #aggiorna il campo da gioco

    # controllo se sono stati toccati i bordi, con la terminazione del gioco
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # ciclo che nasconde i segmenti dello snake
        for segment in segments:
            segment.goto(1000, 1000) # è fuori dallo schermo
        
        segments.clear() # ripulisce lo schermo da tutti i segmenti 
        punt = 0 # reset del punteggio
        delay = 0.1 # reset del delay

        sc.clear() # ripulisco i punteggi
        sc.write("Punteggio : {}  The Best : {}".format(punt, punt_best), align="center", font=("Magneto", 20, "normal"))

    # se mi trovo dal cibo
    if head.distance(food) <20:
        # genero coordinate casuali all'interno del campo da gioco e genero un altro cibo
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # aggiungo un segmento alla testa dello snake con le stesse impostazioni della testa
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001 # accorcio il delay
        punt += 5 # incremeto i punteggi

        if punt > punt_best: # se supero il punteggio migliore aggiorno il risultato
            punt_best = punt

        sc.clear()
        sc.write("Punteggio : {}  The Best : {}".format(punt,punt_best), align="center", font=("Magneto", 20, "normal")) 

    # muovo i segmenti nell'ordine inverso
    for index in range (len (segments) -1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    #muovo il segmento 0 verso la testa dello snake
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move() # richiamo della funzione move

    # controllo tutti i segmenti
    for segment in segments:

        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # ciclo che nasconde i segmenti dello snake
            for segment in segments:
                segment.goto(1000, 1000) # è fuori dallo schermo

            segments.clear() # ripulisce lo schermo da tutti i segmenti 
            punt = 0 # reset del punteggio
            delay = 0.1 # reset del delay

            # aggiorno i punteggi     
            sc.clear()
            sc.write("Punteggio : {}  The Best : {}".format(punt,punt_best), align="center", font=("Magneto", 20, "normal"))

    time.sleep(delay) # metto in pausa il gioco

win.mainloop() # richiamo il loop di tutto il programma