"""
Nella serie di Fibonacci, ciascun numero della serie 
è la somma dei due numeri nella serie che lo precedono, 
ad esempio: 1, 1, 2, 3, 5, 8, 13 (...)
Scrivi una funzione ricorsiva che restituisce in output 
i numeri della sequenza di Fibonacci, entro una soglia 
specifica impostata dall'utente.
"""

def serie (num1, num2, cont1, cont2):
    aux = num1 + num2
    num1 = num2
    num2 = aux

    print(f" {aux}") # stampa del numero della serie

    if cont1 < cont2 : # evito i loop 
        cont1 = cont1 + 1 # incremento di 1 cont1
        serie (num1, num2, cont1, cont2) # richiamo la funzione ricorsivamente


def main () :
    num = int(input("Inserire un numero di numeri da stampare: "))
    
    while ( num <= 0): # verifico se è stato inderito un numero positivo
        num = int(input("Inserire un numero intero e positivo di numeri da stampare: "))

    serie(1 ,1, 0, num - 1) # chiamata della funzione, inserisco num - 1 altrimenti vuene stampato un numero in +

    pass

if __name__ == "__main__" :
    main()