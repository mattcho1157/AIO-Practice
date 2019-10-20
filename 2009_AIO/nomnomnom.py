f = open("nomin.txt", "r")
data = int(f.readline())
food = [int(f.readline()) for x in range(data)]
f.close()

answer = 1
satisfy = food[0]
amount = 0
i = 1

while amount < satisfy:
    if i == data:
        break
    amount += food[i]
    i += 1
    if amount >= satisfy:
        satisfy = amount
        amount = 0
        answer += 1

f = open("nomout.txt", "w")
f.write(str(answer))
f.close()
