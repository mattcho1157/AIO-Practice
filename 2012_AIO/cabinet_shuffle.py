f = open("shufflein.txt", "r")
chairs, ministers = list(map(int,f.readline().split()))
chairp = list(map(int,f.readline().split()))
ministerp = list(map(int,f.readline().split()))
order = list(range(1,ministers+2))                  
f.close()

while True:
    a = (set(chairp) & set(ministerp))
    if len(a) > 0:
        for common in a:
            if common == chairp[0]:
                primeminister = order[ministerp.index(common)]
            order.pop(ministerp.index(common))
            chairp.remove(common)
            ministerp.remove(common)
            
    if len(ministerp) == 1:
        break
    ministerp = [x+1 for x in ministerp]
    for index,item in enumerate(ministerp):
        if item > chairs:
            ministerp[index] = 1

booted = order[0]
f = open("shuffleout.txt", "w")
f.write(str(primeminister) + "\n")
f.write(str(booted) + "\n")
f.close()
