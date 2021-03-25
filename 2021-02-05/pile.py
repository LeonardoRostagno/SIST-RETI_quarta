# stiamo creando dei wrapper (un metodo avvolto in una funzione)

# funzione push
def push_(pila, elemento) :
    pila.append(elemento)

# funzione pop
def pop_(pila) : 
    return pila.pop()


def main() :
    stack = ["a", "b", "c", "d"]

    # push
    push_(stack, "z")
    print(stack)

    # pop
    x = pop_(stack)
    print(x)
    
    pass

if __name__ == "__main__":
    main()