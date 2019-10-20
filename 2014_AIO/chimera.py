f = open("chimin.txt", "r")
length = int(f.readline())
lion = list(f.readline())
snake = list(f.readline())
goat = list(f.readline())
f.close()

ch = []

for x in range(length):
    if lion[x] == snake[x] == goat[x]:
        ch.append("a")
    elif lion[x] == snake[x]:
        ch.append("ls")
    elif lion[x] == goat[x]:
        ch.append("lg")
    elif snake[x] == goat[x]:
        ch.append("sg")
    else:
        ch.append("n")

liony = ch.count("ls") + ch.count("lg") + ch.count("a")
snaky = ch.count("ls") + ch.count("sg") + ch.count("a")
goaty = ch.count("lg") + ch.count("sg") + ch.count("a")
none = ch.count("n")
animals = sorted([liony, snaky, goaty])

counting = 0

if counting != none:
    while animals[0] < animals[1]:
        animals.insert(0,animals.pop(0)+1)
        counting += 1
        if counting == none:
            break
if counting != none:
    while animals[0] == animals[1] < animals[2]:
        animals.insert(0,animals.pop(0)+1)
        counting += 1
        if counting == none:
            break
        animals.insert(1,animals.pop(1)+1)
        counting += 1
        if counting == none:
            break

if counting != none:
        while animals[0] == animals[1] == animals[2]:
            animals.insert(0,animals.pop(0)+1)
            counting += 1
            if counting == none:
                break
            animals.insert(1,animals.pop(1)+1)
            counting += 1
            if counting == none:
                break
            animals.insert(2,animals.pop(2)+1)
            counting += 1
            if counting == none:
                break

print(animals)
answer = min(animals)

f = open("chimout.txt", "w")
f.write(str(answer) + "\n")
f.close()
