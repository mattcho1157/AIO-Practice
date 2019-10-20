f = open("antsin.txt", "r")
data = list(map(int, f.readlines()))
f.close()
days = data[0]
ants = data[1:] + [0]
answer = 0

for i in range(1, days):
    if ants[i-1] < ants[i] and ants[i] >= ants[i + 1]:
        answer += 1

f = open("antsout.txt", "w")
f.write(str(answer))
f.close()
