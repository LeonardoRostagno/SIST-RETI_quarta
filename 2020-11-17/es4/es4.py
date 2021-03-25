lista = [3,2,-1,6,5]

#python style
for elemento in lista:
    print(elemento)
# stampa tutti gli elementi della lista

#C style
for a in range(0, len(lista)):
    print(lista[a])
# stampa degli elementi della lista

#python style con enumerate
for a, elemento in enumerate(lista):
    print(f"{a} + {elemento}")
#ritorna sia indice sia l'elemento

#while, molto C style
contatore = 0

while (contatore < len(lista)):
    print(lista[contatore])
    contatore = contatore + 1

#-----------------------------------------------------------------------------------

# DIZIONARIO
# un dizionario è una collezone non ordinata di elementi
# ogni elemento di un dizionario è una coppia di valori
# chiave:valore
dizionario = {1:"Cerutti", 2:"Dutto", 3:"Martini", 4:"Mellano", 5:"Rostagno"}

# per accedere al valore di un elemento del dizionario si utilizza la notazione
# nome_dizionario[chiave]

print(dizionario[2]) # sacro compito giornaliero del Python, EEEEEE
print(dizionario[4])

# per aggiungere elementi al dizionario si indica 
# la chiave e il valore da mettere al interno
# dizionario[17:"Conradi"]

#stampo tutto il dizionario
print(dizionario)

#-------------------------------------------------------------------------------

# nuovo dizionario
canzone = {"numero":1, "titolo":"Francesco Totti", "autore":"Bello Figo"}
# cit. Grande Conradi

print(canzone["numero"])
print(canzone["titolo"])
print(canzone["autore"])

#-------------------------------------------------------------------------------

#lettura di un file su python
file = open("instagram.csv", "r")

for riga in file:
    print(riga, end="") #usiamo end xé stampa una riga vuota, con end NO

file.close()