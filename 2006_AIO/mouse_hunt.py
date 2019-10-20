f = open("mousein.txt", "r")
xCord = []
yCord = []

for i in range(8):
    x, y = list(f.readline().split())
    xCord.append(int(x))
    yCord.append(int(y))

f.close()

if len(set(xCord)) == 4:
    if yCord.count(max(yCord)) == 4:
        answer = "N"
    else:
        answer = "S"
else:
    if xCord.count(max(xCord)) == 4:
        answer = "E"
    else:
        answer = "W"

f = open("mouseout.txt", "w")
f.write(str(answer))
f.close()
