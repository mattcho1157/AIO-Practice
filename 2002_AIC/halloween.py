f = open("hallin.txt", "r")
lollies = int(f.readline())
f.close()
child = 0
answer = 0
add = 1


while child <= lollies:
    answer += 1
    child += add
    add += 1

f = open("hallout.txt", "w")
f.write(str(answer))
f.close()
