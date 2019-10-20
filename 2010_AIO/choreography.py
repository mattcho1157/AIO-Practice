f = open('dancein.txt', 'r')
length = list(map(int, f.readline().split()))[1]
throws = list(map(int, f.read().split()))
f.close()

received = []
answer = 0

for i in range(length):
    value = throws[2*i]
    try:
        received.remove(value)
    except:
        answer += 1
    received.append(throws[2*i+1])

f = open('danceout.txt', 'w')
f.write(str(answer))
f.close()
