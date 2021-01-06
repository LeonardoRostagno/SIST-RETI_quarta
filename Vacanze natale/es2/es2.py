"""
Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato 
dal produttore, a una NIC, composto da 6 coppie di cifre esadecimali separate da due punti.
Un esempio di MAC è 02:FF:A5:F2:55:12.
Scrivi una funzione genera_mac che generi degli indirizzi MAC pseudo casuali.
"""
import random

carattere = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'] # caratteri usati per l'indirizzo MAC

def genera_mac () : # funzione per assegnamento indirizzo MAC
    indirizzo = ''
    # lunghezza indirizzo MAC -> 12   con ':' -> 17
    for a in range(17):    
        if (a + 1) % 3 == 0 : # inserisco i ':' alla posizione 3, 6, 9, 12, 15
            indirizzo += ':' # inserisco i ':'
        else: 
            indirizzo += carattere[random.randint(0, 15)] # inserisco un carattere casuale
    return indirizzo

def main () : 
    lista = [] # lista per il main 
    lista = genera_mac() # richiamo alla finzione

    print(f"Generazione indirizzo MAC: {lista}") # stampa indirizzo MAC

    pass


if __name__ == "__main__" :
    main()