# sono wrapper

# enqueue, add elemento da dx
def enqueue(coda, elemento) :
    coda.append(elemento)

# dequeue, del elemento da sx
def dequeue(coda):
    return coda.pop(0)


def main() :
    queue = ["a", "b", "c", "d"]

    # enqueue
    enqueue(queue, "z")
    print(queue)

    # dequeue
    x = dequeue(queue)
    print(x)
    
    pass

if __name__ == "__main__":
    main()