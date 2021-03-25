"""
Scrivere un programma che chieda all’utente una stringa 
composta da parentesi aperte e chiuse: (,),[,],{,} e
che verifichi se le coppie e l’ordine delle (,),[,],{,} 
sono corretti. Utilizzare uno stack.
"""
# funzione push
def push_(pila, elemento) :
    pila.append(elemento)

# funzione pop
def pop_(pila) : 
    return pila.pop()

def main() :
    stack = []
    corretto = True

    elem = input("Inserire stringa con parentesi: ")

    for a in elem:
        if (a == '(') or (a == '[') or (a == '{') :
            push_(stack, elem)        

    for b in stack :
        if (len(stack) != 0) :
            if b == ')' :                           
                if ('(' != pop_(stack)):
                    corretto = False

            elif b == ']' :
                if ('[' != pop_(stack)):
                    corretto = False

            elif  b == '}' :
                if ('{' != pop_(stack)):
                    corretto = False
    
    if len(stack) > 0 :
        corretto = False

    if (corretto):
        print("Sequenza corretta!")
    else :
        print("Sequenza errata!")

    pass

if __name__ == "__main__":
    main()