"""
Scrivi una funzione generatrice di password. La funzione deve generare una stringa 
alfanumerica di 8 caratteri qualora l'utente voglia una password semplice, o di 
20 caratteri ascii qualora desideri una password più complicata.
"""

lista = [] # creazione lista

def password (n) : # funzione per la password
    if n == 0 : # se hai scelto l'opsione 0 ovvero 8 caratteri
        print("Hai scelto l'opsione: 8 caratteri")

        for a in range(8) : # ciclo for che mi permette di inserire 8 elementi
            elemento = input("Inserisci un carattere: ") # valore dell'elemento
            lista.append(elemento) # inserisco in lista il valore

    elif n == 1 : # se hai scelto l'opsione 1 ovvero 20 caratteri
        print("Hai scelto l'opsione: 20 caratteri")

        for b in range(20) : # ciclo for che mi permette di inserire 8 elementi
            elemento = input("Inserisci un carattere: ") # valore dell'elemento 
            lista.append(elemento) # inserisco in lista il valore

    return lista

def main () :
    n = int(input("Inserire l'opsione per la sua password (0 --> password 8 caratteri   1 --> password 20 caratteri) "))

    lista_l  = [] # lista per il main
    lista_l = password(n) # richiamo alla funzione

    print(f"La password è: {lista_l}") # stampo della password

    pass

if __name__ == "__main__": # per il main
    main()