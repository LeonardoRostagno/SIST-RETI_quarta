def laMiaFunzione (argomento1, argomento2):
	#codice della funzione indentato
	return argomento1 + argomento2

print(f"La somma è: {laMiaFunzione(3, 4)}")
print(laMiaFunzione("Ciao ", "Mario"))

print("---------------")

lista = [3, 5, 1, 6, 7]
print(f"La lista è: {lista}") #stampa tutta la lista

print("---------------")

#python style =)
for elemento in lista:
    print(elemento) #stampa la lista elemento per elemento

for indice, elemento in enumerate(lista):
    print(f"indice: {indice} - elemento: {lista[indice]}") #stampa la lista in indice

print("---------------")

#C style =(
lunghezza = len(lista)
for indice in range(0,lunghezza):
    print(f"indice: {indice} - elemento: {lista[indice]}") #stampa la lista in indice

print("---------------")

# inserire valori dell'utente caricati su una lista

lista_l = []
valore = input("Inserisci un valore: ")

lista_l.append(int(valore))

print(lista_l)

# slice di liste 
lista_a = [23, 43, 11, 2, 1, 5, 6, -8, 13]

print(lista[4])
print(lista[2:5]) # slicing dall'elemento 2 incluso all' 5 escluso
print(lista[-1]) # richiama l'ultimo elemento 
print(lista[0:-1]) # stampa tutto il vettore tranne l'ultimo elemento

print("---------------")

stringa = "Itis Delpozzo"

print(stringa[1:5]) #stampa Itis