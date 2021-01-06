"""
Il ROT-15 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da 
cifrare viene sostituita con quella posta 15 posizioni più avanti nell'alfabeto.
Scrivi una semplice funzione in grado di criptare una stringa passata, o decriptarla 
se la stringa è già stata precedentemente codificata.
"""

dizionario = {'a': 'p', 'b': 'q', 'c': 'r', 'd': 's', 'e': 't', 'f': 'u', 'g': 'v', 'h': 'w',
              'i': 'x', 'j': 'y', 'k': 'z', 'l': 'a', 'm': 'b', 'n': 'c', 'o': 'd', 'p': 'e',
              'q': 'f', 'r': 'g', 's': 'h', 't': 'i', 'u': 'j', 'v': 'k', 'w': 'l', 'x': 'm',
              'y': 'n', 'z': 'o'}

def ROT (string, scelta):
    new_string = ''

    for a in string: # ciclo che si ripete fino alla fine della stringa
        if scelta == 0 and a in dizionario: # se ho scelto di criptare la stringa e ho ancora delle lettere da criptare
            new_string += dizionario[a] # inserisco in new_stringa la lettera corrispondente dal dizionario

        elif scelta == 1: #se ho scelto di decriptare la stringa
            new_string += a # inserisco in new_stringa la lettera presa in esame

        else: # vado a prendere in esame spazi e numeri
            new_string += a # riporto in new_string lo spazio o il numero
    
    return new_string    

def main () :
    string = input("Inserire una stringa: ")
    scelta = int(input("Inserire una scelta:  0 -> criptare  1 -> decriptare : "))

    stringa = ROT(string, scelta) # richamo alla funzione 

    print(f"Soluzione: {stringa}") # stampo il risultato

    pass

if __name__ == "__main__" :
    main()