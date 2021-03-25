#argonmenti di default in input alle funzioni

def fun (lista = [10, 11], stampa = False) : # default di valori di lista e dello stato della lista
    lista_quadrati = [x * x for x in lista] #compressione di liste, è la stessa cosa di righe 3 - 8
    """
   lista_quadrati = []

    for x in lista:
        lista_quadrati.append(x * x)
    """
    if stampa:
        print(lista_quadrati)

    return lista_quadrati

def main () :
    fun(lista = [1, 2, 3, 4], stampa = True)

    pass

if __name__ == "__main__" :
    main()
