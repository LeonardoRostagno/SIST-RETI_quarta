import pygame 
import sys
import csv
import random

movimenti = {} # dizionario per salvataggio coordinate, chiave = minuto, valore = coord X e coord Y (es.: {0:[0,0], 1:[10,0]} )

TIME = 60 # tempo
DIMENSIONI = (600, 00) # dimensioni finestra
NERO = (0, 0, 0) 
ROSSO = (255, 0, 0)

# COORDINATE
NORD = 10 
SUD = -10
EST = 10
OVEST = -10

def scrivi() :
    csvfile = open ('file.csv', 'w') # apertura file.csv per scrittura
    csvwriter = csv.writer(csvfile) # permette di scrivere

    for chiave, valore in movimenti.items() :
        lista = [chiave, valore[0], valore[1]]

        csvwriter.writerow() 

def disegna(cont):
    pygame.draw.line(finestra, ROSSO, (movimenti[cont - 1][0] + DIMENSIONI[0] / 2, movimenti[cont - 1][1] + DIMENSIONI[1] / 2), (movimenti[cont][0] + DIMENSIONI[0] / 2, movimenti[cont][1] + DIMENSIONI[1] / 2), 1)

def main():
    pygame.init()

    global finestra # finestra è una variabile globale

    finestra = pygame.display.set_mode(DIMENSIONI) # crea una finestra
    finestra.fill(NERO) # colore finestra -> nero

    cordX = 0 # coordinata X
    cordY = 0 # coordinata Y

    movimenti[0] = (0, 0)

    for cont in range(1, TIME) :
        casuale = random.randint(0, 4)

        if casuale == 0: # è uscito NORD
            cordY += NORD # aggiungo NORD a cordY
            
        elif casuale == 1: # è uscito SUD
            cordY += SUD # aggiungo SUD a cordY

        elif casuale == 2: # è uscito EST
            cordX += EST # aggiungo EST a cordX

        elif casuale == 3: # è uscito OVETST
            cordX += OVEST # aggiungo OVEST a cordX

        movimenti[cont] = (cordX, cordY)
        disegna(cont)
        
    print(f"Dizionario: {movimenti}")

    while True:
        for event in pygame.event.get() : # ritorna gli eventi di pygame
            if event.type == pygame.QUIT : # QUIT attributo, quit metodo
                pygame.quit()
                sys.exit() # permette di terminare i programmi

        pygame.display.update() 


    #csvfile.close()


if __name__ == "__main__" :
    main()
