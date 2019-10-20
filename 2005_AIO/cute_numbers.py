f = open("cutein.txt", "r")
data = int(f.readline())
number = list(map(int, f.readlines()))
found = False
value = 1
answer = 0
while not found:
    if number[data - value] == 0:
        answer += 1
    else:
        found = True
    value += 1
f = open("cuteout.txt", "w")
f.write(str(answer))
f.close()
