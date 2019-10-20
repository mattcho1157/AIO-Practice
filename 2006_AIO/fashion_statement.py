f = open("fashin.txt", "r")
money = int(f.readline())
f.close()

remainder = money
answer = 0

for i in [100, 20, 5, 1]:
    answer += remainder//i
    remainder = remainder%i

f = open("fashout.txt", "w")
f.write(str(answer))
f.close()
