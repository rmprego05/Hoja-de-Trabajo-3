import random

def maximo():
    randomlist = random.sample(range(1, 1000), 100)
    print(randomlist)

    maximo = None
    for num in randomlist:
        if (maximo is None or num > maximo):
            maximo = num

    print("Valor maximo", maximo)

