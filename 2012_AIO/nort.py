f = open("nortin.txt", "r")
w,h = map(int,f.readline().split())
f.close()
area = w * h
if area % 2 == 0:
    answer = area
else:
    answer = area - 1
f = open("nortout.txt", "w")
f.write(str(answer))
f.close()
