f = open("wetin.txt", "r")
water = [int(f.readline()) for x in range(8)]
f.close()

answer = 0

for i in range(8):
    answer = max(0, answer + water[i] - 10)

f = open("wetout.txt", "w")
f.write(str(answer))
f.close()
