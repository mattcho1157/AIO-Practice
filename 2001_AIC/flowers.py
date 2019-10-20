f = open("flowin.txt", "r")
grid = int(f.readline())
flowers = int(f.readline())
data = list(map(int, f.read().split()))
f.close()

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for i in range(flowers):
    y = data[2*i+1]
    x = data[2*i]
    if x <= grid:
        if y <= grid:
            q1 += 1
        else:
            q3 += 1
    else:
        if y <= grid:
            q2 += 1
        else:
            q4 += 1
    
maximum = max(q1, q2, q3, q4)
if maximum == q1:
    answer = 1
elif maximum == q2:
    answer = 2
elif maximum == q3:
    answer = 3
else:
    answer = 4

f = open("flowout.txt", "w")
f.write(str(answer) + " " + str(maximum))
f.close()
