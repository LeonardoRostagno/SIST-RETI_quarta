import pygame # installata da noi
import sys # nativa = preinstallata

DIMENSIONI = (300, 250)
NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)

OSTACOLO = -1

CELLE_ADIACENTI = [[-1, 0], [0, -1], [1, 0], [0, 1]]

# lista di liste dove metto la mappa del pavimento, 1 --> cella occupata da ostacolo    0 --> cella libera 
pavimento = [[1, 1, 0, 0, 0, 0], 
            [0, 0, 0, 0, 1, 0], 
            [1, 0, 1, 0, 0, 0], 
            [0, 0, 1, 0, 1, 0], 
            [0, 0, 1, 0, 0, 0]] 

Ncol = len(pavimento[0])
Nrig = len(pavimento)

def drawgrid() :
    dimensioneX = DIMENSIONI[0] // Ncol
    dimensioneY = DIMENSIONI[1] // Nrig

    for x in range(0, DIMENSIONI[0], dimensioneX) :
        for y in range(0, DIMENSIONI[1], dimensioneY) :
            piastrella = pygame.Rect(x, y, dimensioneX, dimensioneY)
            pygame.draw.rect (finestra, BIANCO, piastrella, 1)

    contY = 0

    for Y in range(0, DIMENSIONI[1], dimensioneY):
        riga = pavimento[contY]
        contY += 1
        contX = 0

        for X in range(0, DIMENSIONI[0], dimensioneX):
            colonna = riga[contX]
            contX += 1

            if colonna == 1 : # piastrella occupata
                ostacolo = pygame.Rect(X, Y, dimensioneX, dimensioneY)
                pygame.draw.rect(finestra, ROSSO, ostacolo)

def numera_pastrelle (p): # numera le piastrelle libere e gli ostacoli
    pavimento_numerato = []
    cont = -1 # contatore

    for riga in p :
        nuova_riga = [] # lista vuota

        for piastrella in riga :
            if piastrella == 0 : # libera
                cont = cont + 1 # incremento il contatore
                nuova_riga.append(cont) # cella libera
            else :
                nuova_riga.append(OSTACOLO) # ostacolo
        
        pavimento_numerato.append(nuova_riga)

    return pavimento_numerato


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

"""
generatore di ostacli casuali
x = random.random()
            if x<PROBABILITA_OSTACOLO:
                riga.append(1)
            else:
                riga.append(0)
"""