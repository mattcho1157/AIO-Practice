f = open("manin.txt", "r")
a, b = list(map(int, f.readline().split()))
people = list(map(int, f.readlines()))
f.close()
value = sum(people[0:b])
answer = value
for i in range(b, a):
    value = value - people[i-b] + people[i]
    answer = max(answer, value)

f = open("manout.txt", "w")
f.write(str(answer))
f.close()
