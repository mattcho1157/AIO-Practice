days = 0
loaded = 0

f = open("rainin.txt","r")
firstLine = f.readline().split(" ")
capacity = int(firstLine[1])

while loaded < capacity:

    loaded += int(f.readline())
    days +=1

    if loaded >= capacity:
        break

f.close()

f = open("rainout.txt","w")
f.write(str(days) + "\n")
f.close()
