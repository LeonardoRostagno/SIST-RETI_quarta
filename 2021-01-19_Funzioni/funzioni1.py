def somma (a, b) :
    return a + b

def moltiplicazione (a, b) :
    return a * b

dizionario_funzioni = {0: somma, 1: moltiplicazione}

def main () :
    scelta = int(input("0--> somma  1-->moltiplicazione : "))

    a = int(input("Primo numero: "))
    b = int(input("Secondo numero: "))

    # Metodo di verifica con le eccezioni
    try: 
        x = dizionario_funzioni[scelta](a, b)
        print(x)

    except:
        print("Hai inserito un valore errato")

    pass

if __name__ == "__main__" :
    main()
