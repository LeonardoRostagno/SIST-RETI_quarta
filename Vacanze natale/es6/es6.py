"""
Il file annual.csv (allegato) contiene la anomalia della temperatura globale del pianeta 
Terra dal 1880 ad oggi, proveniente da varie fonti (colonna “Source”). Scrivere un programma 
che generi un dizionario che abbia come chiave l’anno (“Year”) e valore la media aritmetica 
delle anomalie registrate dalle varie fonti durante quell’anno.
Inoltre scrivere una funzione che dati in input due anni diversi (anno_1 e anno_2) trovi la 
anomalia massima e minima nel periodo compreso tra anno_1 e anno_2.
"""
import csv

def maxMin(anno1, anno2):
    anMax = -10000
    anMin = 10000
    if (anno1 > anno2):
        cont = anno2
        while (cont < anno1):
            if(diz[cont] > anMax): #prima volta sempre vero
                anMax = diz[cont]
            if(diz[cont] < anMin): #prima volta sempre vero
                anMin = diz[cont]
            cont+=1                #avanza di anno in anno, fino ad arrivare all'anno maggiore tra anno1 e anno2
    else:
        cont = anno1
        while (cont < anno2):
            if(diz[cont] > anMax): #prima volta sempre vero
                anMax = diz[cont]
            if(diz[cont] < anMin): #prima volta sempre vero
                anMin = diz[cont]
            cont+=1
    print(f"l'anomalia massima registrata e': {anMax}")
    print(f"l'anomalia minima registrata e': {anMin}")
    
with open("annual.csv", mode='r') as csv_file:      #si apre il file come csv
    file = csv.DictReader(csv_file)                 #si legge il file
    cont = 0
    diz = {}
    somma = 0
    anno1 = int(input("inserire un primo anno: "))
    while (anno1 > 2016 or anno1 < 1880):
        anno1 = int(input("anno fuori scala, reinserirlo: "))
    anno2 = int(input("inserire un secondo anno: "))
    while (anno2 > 2016 or anno2 < 1880):
        anno2 = int(input("anno fuori scala, reinserirlo: "))
    for riga in file:
        if (cont == 0):                 #prima riga (spiegazione contenuto file)
            cont += 1
        anno = riga["Year"]             #si prende l'anno 
        mean = float(riga["Mean"])      #si prende la riga
        diz[int(anno)] = float(mean)    #si crea il dizionario       
        cont += 1 
    maxMin(anno1, anno2)                #si richiama la funzione