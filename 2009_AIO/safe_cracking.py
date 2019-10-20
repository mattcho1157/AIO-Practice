f = open("safein.txt", "r")
data = list(map(int, f.read().split()))
f.close()
a = data.pop(0)
b = data.pop(0)
code = data[: a]
seen = data[-b:]
x = 0
while x <= a - b:
    differ = code[x] - seen[0]
    if differ >= 0:
        for i in range(1, b):
            if differ == code[x + i] - seen[i]:
                if i == b-1:
                    f = open("safeout.txt", "w")
                    for s in code:
                        f.write(str(s - differ) + "\n")
                    f.close()
            else:
               break 
    x += 1
