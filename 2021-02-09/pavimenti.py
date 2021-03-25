import pygame # installata da noi
import sys # nativa = preinstallata

DIMENSIONI = (300, 250)
NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)

def drawgrid() :
    dimensione = 50
    dimensione1 = 50
    dimensione2 = 50

    for x in range(0, DIMENSIONI[0], dimensione1) :
        for y in range(0, DIMENSIONI[1], dimensione2) :
            piastrella = pygame.Rect(x, y, dimensione, dimensione)

            pygame.draw.rect (finestra, BIANCO, piastrella, 1)

    ostacolo = pygame.Rect(0, 0, dimensione, dimensione)
    pygame.draw.rect(finestra, ROSSO, ostacolo)

    ostacolo = pygame.Rect(50, 0, dimensione, dimensione)
    pygame.draw.rect(finestra, ROSSO, ostacolo)

    ostacolo = pygame.Rect(200, 50, dimensione, dimensione)
    pygame.draw.rect(finestra, ROSSO, ostacolo)

    ostacolo = pygame.Rect(0, 100, dimensione, dimensione)
    pygame.draw.rect(finestra, ROSSO, ostacolo)

    ostacolo = pygame.Rect(100, 100, dimensione, dimensione)
    pygame.draw.rect(finestra, ROSSO, ostacolo)

    ostacolo = pygame.Rect(100, 150, dimensione, dimensione)
    pygame.draw.rect(finestra, ROSSO, ostacolo)

    ostacolo = pygame.Rect(100, 200, dimensione, dimensione)
    pygame.draw.rect(finestra, ROSSO, ostacolo)

    ostacolo = pygame.Rect(200, 150, dimensione, dimensione)
    pygame.draw.rect(finestra, ROSSO, ostacolo)
   

def main() :
    pygame.init()

    global finestra # finestra è una variabile globale

    finestra = pygame.display.set_mode(DIMENSIONI) # crea una finestra
    finestra.fill(NERO)

    while True:
        drawgrid()

        for event in pygame.event.get() : # ritorna gli eventi di pygame
            if event.type == pygame.QUIT : # QUIT attributo, quit metodo
                pygame.quit()
                sys.exit() # permette di terminare i programmi

        pygame.display.update() 

if __name__ == "__main__" :
    main()
