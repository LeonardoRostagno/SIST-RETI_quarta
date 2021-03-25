#dato in I un num N, tracciare le linee di lunghezza N

# import turtle , ovvero importa turtle e tutto ciò che contiene
from turtle import * # importa turtle e tuto quello che contiene e posso usare direttamente il loro nome

color('red', 'yellow')

n = int(input("Inserire la lenghezza di un lato N: "))
cont = n
c = 0

begin_fill()

while (cont > 0):
    forward(10)

    rotate = 360 / n

    left(rotate)

    cont = cont - 1
    c = c + 1
    print(f"Parti eseguite {c}")

end_fill()

done()