lista = []

n = int(input("Quanti elementi vuoi inserire nella lista? ")) # chiedo quanti elementi si desiderano

for a in range(n): # ciclo for che mi permette di inserire n elementi
    valore = int(input("Inserire gli elemnti numerici della lista: ")) # valore dell'elemento 
                                                                       # int(input()) mi dice fin da subito che valore è un intero
    lista.append(valore) # inserisco in lista il valore

print(f"La lista è: {lista}")

lung = len(lista) # salvo la lunghezza della lista in lung

for indice in range (lung - 1): # ciclo for che scorre tutta la lista

    for cont in range (0, lung - indice - 1) : # ciclo for che scorre la lista fino a lung - indice - 1

        if (lista[cont] > lista[cont + 1]) : # se il primo elemento analizzato è > del secondo
            lista[cont], lista[cont + 1] = lista[cont + 1], lista[cont] # inverto i 2 elementi

print(f"La bubble list è: {lista}")

