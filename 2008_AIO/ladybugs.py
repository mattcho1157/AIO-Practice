f = open("ladyin.txt", "r")
a = int(f.readline())
b = []
for i in range(a):
    b.append(int(f.readline()))
data = max(b) - min(b) + 1 
f.close()
f = open("ladyout.txt", "w")
f.write(str(data))
f.close()
